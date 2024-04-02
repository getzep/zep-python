import json
import ast
from zep_python import ZepClient
from zep_python.memory import Memory, Session
from zep_python.message import Message
from zep_python.user import CreateUserRequest
import os
from openai import AsyncOpenAI
from config import openai_api_key, ZEP_API_KEY, OPENAI_MODEL
from chainlit.playground.providers.openai import stringify_function_call
import chainlit as cl
from schema import get_flight_results, book_flight, fight_booking
from datetime import date
import uuid
import asyncio

# Initialize the OpenAI and Zep clients with API keys from the environment/config file.
client = AsyncOpenAI(api_key=openai_api_key)
zep = ZepClient(api_key=ZEP_API_KEY)

MAX_ITER = 5

# A system prompt setting the context for AI's function in the conversation
system_prompt = f"""Today is {date.today()}, You are a helpful assistant, your task is to understand user queries related to flight bookings only, provide information on available flights, prices, leg room, layover and duration, and help users make reservations. Don't answer to any query or question that isn't related to flight booking. Use the tips below as a guide.

Tips:
- Always ask one question at a time.
- Always ask customer for departure airport/city, destination city/airport, departure date and return dates.
- Always ask customer for their budget before finding a flight.
- Always ask if a customer want return on one way flight.
- Always suggest an alternative preference from the customer data if their current flight choice is unavailable.
- Always ask customer for the class they prefer, and the number of stops.


"""


@cl.on_chat_start
async def start_chat():
    """Initializes a chat session when a new chat is started."""

    user_id = str(uuid.uuid4())  # Generate a unique user ID.
    session_id = str(uuid.uuid4())  # Generate a unique session ID.
    cl.user_session.set("user_id", user_id)  # Store user ID in the session.
    cl.user_session.set("session_id", session_id)  # Store session ID in the session.

    # Create a new user in Zep with the generated ID.
    await zep.user.aadd(CreateUserRequest(user_id=user_id))

    # Add a new session in Zep for the user.
    await zep.memory.aadd_session(
        Session(
            user_id=user_id,
            session_id=session_id,
        )
    )
    # Store the system prompt at the beginning of the session.
    await zep_store_messages(
        message=system_prompt, role="system", role_type="system", session_id=session_id
    )


@cl.step(name="Conversation Sentiment", type="tool")
async def sentiment(session_id: str):
    """Analyzes the sentiment of the session's conversation."""
    classes = [
        "Positive",
        "Negative",
        "Neutral",
    ]
    sentiment = await zep.memory.aclassify_session(
        session_id,
        "Sentiment",
        classes,
        persist=True,
        instruction="Given a conversation, classify sentiment and return only the sentiment label either positive, negative or neutral.",
    )
    return sentiment


@cl.step(name="Rate Dialog Flow", type="tool")
async def interaction_classification(session_id: str):
    """Classify each session based on the conversation flow"""
    classes = ["Easy", "Fair", "Difficult"]
    classification = await zep.memory.aclassify_session(
        session_id,
        "interaction_classification",
        classes,
        persist=True,
        instruction="Given a session, on a scale of 0 to 2, with 0 being extremely easy, 1 being fair and 2 being difficult, in terms of how effortless it was for the user to book their flight.",
    )
    return classification


@cl.step(name="fact extractor", type="retrieval", language="python")
async def get_session_facts(session_id: str):
    """zep fact extractor to extract facts from the session/conversation"""
    memory = await zep.memory.aget_memory(session_id, "perpetual")
    facts = memory.facts
    summary = memory.summary
    message_history = []

    if facts:
        message_history.append(
            {
                "role_type": "system",
                "content": "Facts about this user:\n" + "\n".join(facts),
            }
        )


@cl.step(type="tool")
async def call_tool(tool_call, message_history):
    """Executes a tool call and processes its response."""
    function_name = tool_call.function.name
    arguments = ast.literal_eval(tool_call.function.arguments)

    current_step = cl.context.current_step
    current_step.name = function_name

    current_step.input = arguments
    if function_name == "flight_search":
        function_response = get_flight_results(**arguments)
    elif function_name == "book_flight":
        function_response = book_flight(**arguments)

    current_step.output = function_response
    current_step.language = "json"

    message_history.append(
        {
            "role": "function",
            "name": function_name,
            "content": function_response,
            "tool_call_id": tool_call.id,
        }
    )


@cl.step(type="llm")
async def call_gpt4(session_id):
    """Generates a response from GPT-4 based on the session's conversation history."""
    memory = await zep.message.aget_session_messages(session_id)
    memory_history = [m.to_dict() for m in memory]
    cleaned_data = [
        {
            k: v
            for k, v in item.items()
            if k not in ["created_at", "role_type", "token_count", "uuid"]
        }
        for item in memory_history
    ]

    settings = {
        "model": OPENAI_MODEL,
        "tools": fight_booking,
        "tool_choice": "auto",
    }

    cl.context.current_step.generation = cl.ChatGeneration(
        provider="openai-chat",
        messages=[
            cl.GenerationMessage(content=m["content"], role=m["role"])
            for m in cleaned_data
        ],
        settings=settings,
    )

    response = await client.chat.completions.create(messages=cleaned_data, **settings)

    message = response.choices[0].message

    for tool_call in message.tool_calls or []:
        if tool_call.type == "function":
            await call_tool(tool_call, cleaned_data)

    if message.content:
        cl.context.current_step.generation.completion = message.content
        cl.context.current_step.output = message.content

    elif message.tool_calls:
        completion = stringify_function_call(message.tool_calls[0].function)

        cl.context.current_step.generation.completion = completion
        cl.context.current_step.language = "json"
        cl.context.current_step.output = completion

    return message


async def zep_store_messages(session_id, message, role, role_type):
    """Store messages on zep memory store"""
    try:
        messages = [Message(role=role, content=message.content, role_type=role_type)]
    except Exception as e:
        messages = [Message(role=role, content=message, role_type=role_type)]
    memory = Memory(messages=messages)
    result = zep.memory.add_memory(session_id, memory)
    return result


@cl.on_message
async def run_conversation(message: cl.Message):
    """Main conversation loop that processes each message."""
    message_history = cl.user_session.get("message_history")
    session_id = cl.user_session.get("session_id")
    await zep_store_messages(
        message=message, role="user", role_type="user", session_id=session_id
    )

    cur_iter = 0

    while cur_iter < MAX_ITER:
        message = await call_gpt4(
            session_id
        )  # Logic to process GPT-4 response and tool calls within messages.
        if not message.tool_calls:
            await cl.Message(content=message.content, author="Answer").send()
            await zep_store_messages(
                message=message,
                role="assistant",
                role_type="assistant",
                session_id=session_id,
            )
            await asyncio.gather(
                interaction_classification(session_id), sentiment(session_id)
            )
            break

        cur_iter += 1
