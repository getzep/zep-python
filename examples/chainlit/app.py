import os
import uuid

import chainlit as cl
from chainlit.input_widget import Select
from dotenv import find_dotenv, load_dotenv
from openai import AsyncOpenAI

from zep_python import ZepClient
from zep_python.memory import Memory
from zep_python.message import Message
from examples.chat_history.chat_history_travel import history as travel_history
from examples.chat_history.chat_history_shoe_purchase import history as sales_history

load_dotenv(dotenv_path=find_dotenv())

API_KEY = os.environ.get("ZEP_API_KEY")
ZEP_API_URL = os.environ.get("ZEP_API_URL")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

zep = ZepClient(api_key=API_KEY, api_url=ZEP_API_URL)

openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)


@cl.on_chat_start
async def on_chat_start():
    chat_profile = cl.user_session.get("chat_profile")
    await cl.Message(
        content=f"starting chat using the {chat_profile} chat profile"
    ).send()
    settings = await cl.ChatSettings(
        [
            Select(
                id="memory_type",
                label="Memory Type",
                values=["perpetual", "message_window", "summary_retriever"],
                initial_index=0,
            ),
        ]
    ).send()

    cl.user_session.set("memory_type", settings["memory_type"])

    cl.user_session.set("id", uuid.uuid4())
    if chat_profile == "Memory + RAG":
        collection_name = os.environ.get("ZEP_COLLECTION")
        if not collection_name:
            raise ValueError("ZEP_COLLECTION environment variable is not set")
        try:
            await zep.document.aget_collection(collection_name)
        except Exception as e:
            raise ValueError(f"Error accessing collection {collection_name}: {e}")

    if chat_profile != "Memory + RAG":
        await cl.Message(
            content="You can optionally populate session with some relevant messages",
            actions=[
                cl.Action(name="Populate Messages", value="populate_messages", description="Will populate session with relevant messages")
            ]
        ).send()



@cl.action_callback("Populate Messages")
async def on_action():
    example_history = travel_history if cl.user_session.get("chat_profile") == "Memory" else sales_history
    session_id = cl.user_session.get("id")
    try:
        for m in example_history:
            message = Message(**m)
            memory = Memory(messages=[message])
            await zep.memory.aadd_memory(session_id, memory)
        memory = await zep.memory.aget_memory(session_id, cl.user_session.get("memory_type"))
        for m in memory.messages:
            await cl.Message(author="Assistant" if m.role == "assistant" else "You", content=m.content).send()
    except Exception as e:
        raise ValueError(f"Error adding memory to session {session_id}: {e}")


@cl.on_settings_update
async def update_settings(settings):
    cl.user_session.set("memory_type", settings["memory_type"])


@cl.step(name="ZepHistory", type="retrieval")
async def get_history():
    session_id = cl.user_session.get("id")
    memory = await zep.memory.aget_memory(
        session_id, cl.user_session.get("memory_type")
    )
    summary = memory.summary
    message_history = []
    if summary:
        message_history.append({"role": "system", "content": summary.content})
    for message in memory.messages:
        message_history.append(
            {
                "role": "assistant" if message.role == "ai" else "user",
                "content": message.content,
            }
        )
    return message_history


@cl.step(name="ZepVectorStore", type="retrieval")
async def get_context(question: str):
    collection_name = "leobernstein"
    collection = await zep.document.aget_collection(collection_name)
    result = await collection.asearch(text=question, limit=1, search_type="mmr")
    return result[0].content


@cl.step(name="Synthesize Question", type="retrieval")
async def synthesize_question(session_id: str):
    question = await zep.memory.asynthesize_question(session_id, last_n=3)
    return question

@cl.step(name="Classify Conversation", type="tool")
async def classify_conversation(session_id: str):
    classes = [
        "low spender <$50",
        "medium spender >=$50, <$100",
        "high spender >=$100",
        "unknown",
    ]
    classification = await zep.memory.aclassify_session(
        session_id, "spender_category", classes
    )
    return classification


@cl.set_chat_profiles
async def chat_profile():
    return [
        cl.ChatProfile(
            name="Memory",
            markdown_description="Basic LLM app with persistent memory.",
        ),
        cl.ChatProfile(
            name="Memory + RAG",
            markdown_description="LLM app with persistent memory and RAG context retrieval.",
        ),
        cl.ChatProfile(
            name="Classification",
            markdown_description="Dialog Classification Example",
        )
    ]


@cl.step(name="OpenAI", type="llm")
async def call_openai(messages):
    response = await openai_client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
    )
    return response.choices[0].message


@cl.on_message
async def on_message(message: cl.Message):
    session_id = cl.user_session.get("id")
    await zep.memory.aadd_memory(
        session_id,
        Memory(
            messages=[
                Message(role="user", content=message.content),
            ]
        ),
    )

    msg = cl.Message(author="Assistant", content="")
    await msg.send()
    history = await get_history()
    if cl.user_session.get("chat_profile") == "Memory + RAG":
        search_query = await synthesize_question(session_id)
        context = await get_context(search_query)
        system_prompt = f"""Answer the question based only on the following context:
        <context>
        {context}
        </context>"""
        history.append({"role": "system", "content": system_prompt})
    if cl.user_session.get("chat_profile") == "Classification":
        classification = await classify_conversation(session_id)
    response_message = await call_openai(history)
    msg.content = response_message.content or ""
    await msg.update()

    memory_to_add = Memory(
        messages=[
            Message(role="assistant", content=response_message.content),
        ]
    )

    await zep.memory.aadd_memory(session_id, memory_to_add)
