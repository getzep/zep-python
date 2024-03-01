from zep_python import ZepClient
import os
from dotenv import load_dotenv, find_dotenv
import uuid
from zep_python.message import Message
from zep_python.memory import Memory
import chainlit as cl
from openai import AsyncOpenAI

load_dotenv(dotenv_path=find_dotenv())

API_KEY = os.environ.get('ZEP_API_KEY')
ZEP_API_URL = os.environ.get('ZEP_API_URL')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

zep = ZepClient(api_key=API_KEY, api_url=ZEP_API_URL)

openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)


@cl.on_chat_start
async def on_chat_start():
    chat_profile = cl.user_session.get("chat_profile")
    await cl.Message(
        content=f"starting chat using the {chat_profile} chat profile"
    ).send()
    cl.user_session.set("id", uuid.uuid4())


@cl.step(name="ZepHistory", type="retrieval")
async def get_history():
    session_id = cl.user_session.get("id")
    memory = await zep.memory.aget_memory(session_id, "perpetual")
    summary = memory.summary
    message_history = []
    if summary:
        message_history.append({"role": "system", "content": summary.content})
    for message in memory.messages:
        message_history.append({
            "role": "assistant" if message.role == "ai" else "user",
            "content": message.content
        })
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


@cl.set_chat_profiles
async def chat_profile():
    return [
        cl.ChatProfile(
            name="Memory",
            markdown_description="The underlying LLM model is **GPT-3.5**.",
        ),
        cl.ChatProfile(
            name="Memory + RAG",
            markdown_description="The underlying LLM model is **GPT-4**.",
        ),
        cl.ChatProfile(
            name="Classification",
            markdown_description="The underlying LLM model is **GPT-4**.",
        ),
        cl.ChatProfile(
            name="Fact Extraction",
            markdown_description="The underlying LLM model is **GPT-4**.",
        ),
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
    await zep.memory.aadd_memory(session_id, Memory(
        messages=[
            Message(role="user", content=message.content),
        ]
    ))

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
    response_message = await call_openai(history)
    msg.content = response_message.content or ""
    await msg.update()

    memory_to_add = Memory(
        messages=[
            Message(role="assistant", content=response_message.content),
        ]
    )

    await zep.memory.aadd_memory(session_id, memory_to_add)
