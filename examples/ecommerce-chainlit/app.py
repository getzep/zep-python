import asyncio
import os
import uuid

import chainlit as cl
from chat_history_shoe_purchase import history as previous_chat_history
from dotenv import find_dotenv, load_dotenv
from openai import AsyncOpenAI

from zep_cloud.client import AsyncZep
from zep_cloud.types import Message

load_dotenv(dotenv_path=find_dotenv())

API_KEY = os.environ.get("ZEP_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

OPENAI_MODEL = "gpt-4-0125-preview"

ASSISTANT_ROLE = "assistant"
USER_ROLE = "user"
BOT_NAME = "Amazing Shoe Salesbot"

zep = AsyncZep(api_key=API_KEY)

openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)

welcome_message = """Welcome to the shoe store! I'm here to help you find the perfect pair of shoes."""

base_system_prompt = """You are a friendly shoe sales assistant. You are responsible for both selling shoes and managing customer
orders, returns, and exchanges."""

sales_instructions = """You job is to be sell shoes to users. Be helpful and ensure that the
conversation is always moving towards closing a sale. You can ask questions to understand the user's needs and
provide recommendations based on the user's responses. Keep your responses short and Always Be Closing!

Important: To move a customer towards an order, you must:
- ask how the shoes will be used (e.g. for running, walking, hiking or streetwear)
- ask the user for their shoe size and foot width. Also, for running shoes, do they have a pronation or supination?
- do they have a color preference?
- lastly, you can't move forward without asking for their budget 

You are authorized to offer only a 10% discount on the final price.

Do not ask for all of the above at once. Ask for these as you progress the conversation. 
You must recommend a shoe that meets the above criteria.
"""

return_instructions = """Review the user's purchase history. What shoe did they previously purchase? ALWAYS ask the user if this
is the item they want to return.  

Ask for the reason for the return and offer a solution: either money back or an exchange.

You must be helpful and ensure that the conversation is always moving towards a resolution. 

You may not offer discounts towards a return or exchange.
"""

order_instructions = """To complete an order, you must get the user's full name, email address, and shipping address. 
You must also ask the user to add their credit card information in our secure payment form. This will allow us to process the order and ensure a smooth transaction."""


async def load_previous_chat_history(session_id: str):
    await zep.memory.add(
        session_id=session_id,
        messages=[
            Message(role_type=msg["role_type"], content=msg["content"])
            for msg in previous_chat_history
        ],
    )


@cl.step(name="Zep Chat History Retrieval", type="retrieval", language="python")
async def get_history(session_id: str):
    memory = await zep.memory.get(session_id=session_id, memory_type="perpetual")
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
    if summary:
        message_history.append(
            {"role_type": "system", "content": "Chat History:\n" + summary.content}
        )

    for message in memory.messages:
        message_history.append(
            {
                "role_type": message.role_type,
                "content": message.content,
            }
        )
    return message_history


async def display_actions():
    await cl.Message(
        content="Select an action",
        actions=[
            cl.Action(
                name="Print Facts",
                value="print_facts",
            )
        ],
    ).send()


@cl.action_callback("Print Facts")
async def print_facts():
    session_id = cl.user_session.get("session_id")
    memory = await zep.memory.get(session_id=session_id, memory_type="perpetual")
    facts = memory.facts

    if facts:
        msg = cl.Message(author="System", content="\n".join(facts))
        await msg.send()


@cl.step(name="Zep Collection Retrieval", type="retrieval", language="python")
async def get_shoe_data(question: str):
    collection_name = "shoe_data"
    result = await zep.document.search(collection_name=collection_name, text=question, limit=3, search_type="mmr")
    return "\n".join([r.content for r in result.results])


@cl.step(name="Synthesize Retrieval Question", type="retrieval")
async def synthesize_question(session_id: str):
    sq_result = await zep.memory.synthesize_question(session_id=session_id, last_n_messages=4)
    return sq_result.question


@cl.step(name="Classify Intent", type="tool")
async def classify_intent(session_id: str) -> str:
    classes = [
        "the user wants to buy shoes (buy_shoes)",
        "the user wants to return shoes (return_shoes)",
        "the user intent is unknown (unknown)",
    ]
    classification = await zep.memory.classify_session(
        session_id=session_id, name="intent", classes=classes, last_n=2, persist=False
    )
    if "buy_shoes" in classification.class_:
        return "buy_shoes"
    if "return_shoes" in classification.class_:
        return "return_shoes"
    if "order_query" in classification.class_:
        return "order_query"
    return "unknown"


@cl.step(name="Classify Budget", type="tool")
async def classify_budget(session_id: str):
    classes = [
        "the user's budget is less than $100",
        "the user's budget is greater than $100 but less than $200",
        "the user's budget is greater than $200",
        "the user has not mentioned their budget for shoes (unknown)",
    ]
    classification = await zep.memory.classify_session(
        session_id=session_id, name="spender_category", classes=classes, persist=False
    )
    return classification


@cl.step(name="Classify User Agreed on Purchase", type="tool")
async def classify_ready_for_purchase(session_id: str):
    classes = [
        "the user has agreed to buy a specific shoe (ready_for_purchase)",
        "the user has not yet agreed to buy a specific shoe (not_ready)",
    ]
    classification = await zep.memory.classify_session(
        session_id=session_id, name="ready_for_purchase", classes=classes, persist=False
    )
    return classification


@cl.step(name="OpenAI", type="llm")
async def call_openai(messages):
    response = await openai_client.chat.completions.create(
        model=OPENAI_MODEL,
        temperature=0.1,
        messages=messages,
    )
    return response.choices[0].message


@cl.on_message
async def on_message(message: cl.Message):
    session_id = cl.user_session.get("session_id")
    # Add the user's message to Zep's memory
    await zep.memory.add(
        session_id=session_id,
        messages=[
            Message(
                role_type=USER_ROLE,
                content=message.content,
                role=cl.user_session.get("user_name"),
            ),
        ],
        summary_instruction="Do not include shoe sizes.",
    )

    (
        search_query,
        chat_history,
        budget_class,
        ready_to_purchase,
        intent,
    ) = await asyncio.gather(
        synthesize_question(session_id),
        get_history(session_id),
        classify_budget(session_id),
        classify_ready_for_purchase(session_id),
        classify_intent(session_id),
    )

    print(intent)

    # Load the base prompt into
    prompt = [{"role": "system", "content": base_system_prompt}]

    match intent:
        case "buy_shoes" | "unknown":
            if "ready_for_purchase" in ready_to_purchase.class_:
                prompt.append({"role": "system", "content": order_instructions})
                msg = cl.Message(
                    author="System",
                    content=ready_to_purchase,
                    actions=[
                        cl.Action(name="Complete Purchase", value="complete_purchase")
                    ],
                )
                await msg.send()
                await zep.memory.update_session(
                    session_id=session_id,
                    metadata={"purchase_state": "ready_for_purchase"},
                )

                if "unknown" not in budget_class.class_:
                    msg = cl.Message(
                        author="System",
                        content=f"{budget_class.name}: {budget_class.class_}",
                    )
                    await msg.send()
            else:
                shoe_data = await get_shoe_data(search_query)
                prompt.append({"role": "system", "content": sales_instructions})
                prompt.append(
                    {
                        "role": "system",
                        "content": f"""Use the context below to answer the question:
                                    <context>
                                    {shoe_data}
                                    </context>""",
                    }
                )
        case "return_shoes":
            prompt.append({"role": "system", "content": return_instructions})
            msg = cl.Message(author="System", content="Identified Return Intent")
            await msg.send()
        case _:
            print("Unknown intent")
            return

    prompt = prompt + [
        {"role": message["role_type"], "content": message["content"]}
        for message in chat_history
    ]

    response_message = await call_openai(prompt)
    msg = cl.Message(author=BOT_NAME, content=(response_message.content))
    await msg.send()

    await zep.memory.add(
        session_id=session_id,
        messages=[
            Message(
                role_type=ASSISTANT_ROLE,
                content=response_message.content,
                role=BOT_NAME,
            ),
        ]
    )

    await display_actions()


@cl.on_chat_start
async def main():
    user_id = str(uuid.uuid4())
    session_id = str(uuid.uuid4())
    cl.user_session.set("user_id", user_id)
    cl.user_session.set("session_id", session_id)

    msg = cl.Message(author=BOT_NAME, content=welcome_message)
    await msg.send()

    name_prompt = "What is your name?"
    user_name = ""
    name_response = ""
    res = await cl.AskUserMessage(content=name_prompt).send()
    if res:
        user_name = res["output"]
        cl.user_session.set("user_name", user_name)
        name_response = f"Hi {user_name}! How can I assist you today?"
        await cl.Message(
            content=name_response,
        ).send()

    if not user_name:
        return

    await zep.user.add(
        user_id=user_id,
        first_name=user_name,
        last_name="Chalef",
        email="daniel.chalef@getzep.com",
    )

    await zep.memory.add_session(
        user_id=user_id,
        session_id=session_id,
    )

    await load_previous_chat_history(session_id)

    await zep.memory.add(
        session_id=session_id,
        messages=[
            Message(
                role_type=ASSISTANT_ROLE,
                content=welcome_message + " " + name_prompt,
                role=BOT_NAME,
            ),
            Message(role_type=USER_ROLE, content=user_name, role=user_name),
            Message(role_type=ASSISTANT_ROLE, content=name_response, role=BOT_NAME),
        ]
    )