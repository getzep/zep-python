"""
Example of using the Zep Python SDK asynchronously.

This script demonstrates the following functionality:
- Creating a user.
- Creating a session associated with the created user.
- Adding messages to the session.
- Searching the session memory for a specific query.
- Searching the session memory with MMR reranking.
- Searching the session memory with a metadata filter.
- optionally deleting the session.
"""

import asyncio
import os
import uuid

from dotenv import find_dotenv, load_dotenv

from examples.chat_history.chat_history_shoe_purchase import history

from zep.client import AsyncZep
from zep.types import Memory, Message

load_dotenv(
    dotenv_path=find_dotenv()
)  # load environment variables from .env file, if present

API_KEY = os.environ.get("ZEP_API_KEY") or "YOUR_API_KEY"
API_URL = os.environ.get("ZEP_API_URL")  # only required if you're using Zep Open Source


async def main() -> None:
    client = AsyncZep(
        api_key=API_KEY,
    )

    # Create a user
    user_id = uuid.uuid4().hex  # unique user id. can be any alphanum string

    await client.user.add(
        user_id=user_id,
        email="user@example.com",
        first_name="Jane",
        last_name="Smith",
        metadata={"vip": "true"},
    )

    session_id = uuid.uuid4().hex  # unique session id. can be any alphanum string

    # Create session associated with the above user
    print(f"\n---Creating session: {session_id}")

    await client.memory.add_session(session_id=session_id, user_id=user_id, metadata={"foo": "bar"})

    # Update session metadata
    print(f"\n---Updating session: {session_id}")
    await client.memory.update_session(session_id=session_id, metadata={"bar": "foo"})

    # Get session
    print(f"\n---Getting session: {session_id}")
    session = await client.memory.get_session(session_id)
    print(f"Session details: {session}")

    # Add Memory for session
    print(f"\n---Add Memory for Session: {session_id}")
    for m in history:
        print(f"{m['role']}: {m['content']}")
        message = Message(**m)
        memory = Memory(messages=[message])
        await client.memory.create(session_id=session_id, request=memory)

    # Synthesize a question from most recent messages.
    # Useful for RAG apps. This is faster than using an LLM chain.
    print("\n---Synthesize a question from most recent messages")
    question = await client.memory.synthesize_question(session_id, last_n_messages=3)
    print(f"Question: {question}")

    # Classify the session.
    # Useful for semantic routing, filtering, and many other use cases.
    print("\n---Classify the session")
    classes = [
        "low spender <$50",
        "medium spender >=$50, <$100",
        "high spender >=$100",
        "unknown",
    ]
    classification = await client.memory.classify_session(
        session_id, name="spender_category", classes=classes, persist=True
    )
    print(f"Classification: {classification}")

    # Get Memory for session
    print(f"\n---Get Perpetual Memory for Session: {session_id}")
    memory = await client.memory.get(session_id, memory_type="perpetual")
    print(f"Memory: {memory}")
    print("\n---End of Memory")

    # Search Memory for session
    query = "What are Jane's favorite show brands?"
    print(f"\n---Searching over summaries for: '{query}'")
    summary_result = await client.memory.search(session_id, text=query, search_scope="summary")
    print("summaryResult: ", summary_result)

    print("\n---Searching over summaries with MMR Reranking")
    summary_mmr_result = await client.memory.search(session_id, text=query, search_scope="summary", search_type="mmr")
    print("summary_mmr_result: ", summary_mmr_result)

    print("\n---Searching over messages using a metadata filter")

    messages_result = await client.memory.search(
        session_id,
        text=query,
        search_scope="messages",
        metadata={"where": {"jsonpath": '$[*] ? (@.bar == "foo")'}}
    )
    print("messages_result: ", messages_result)

    # Delete Memory for session
    # Uncomment to run
    print(f"\n5---deleteMemory for Session: {session_id}")
    await client.memory.delete(session_id)


if __name__ == "__main__":
    asyncio.run(main())
