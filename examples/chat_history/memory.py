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
from dataclasses import Field
from typing import Optional, Dict, Any

from pydantic import BaseModel

from dotenv import find_dotenv, load_dotenv

from chat_history_shoe_purchase import history
from zep_cloud import ZepDataClass

from zep_cloud.client import AsyncZep
from zep_cloud.external_clients.memory import BaseDataExtractorModel
from zep_cloud.types import Message

load_dotenv(
    dotenv_path=find_dotenv()
)  # load environment variables from .env file, if present

API_KEY = os.environ.get("ZEP_API_KEY") or "YOUR_API_KEY"
BASE_URL = os.environ.get("ZEP_API_URL")

print(f"API_KEY:", API_KEY, BASE_URL)


async def main() -> None:
    client = AsyncZep(
        api_key=API_KEY,
    )

    # Create a user
    user_id = uuid.uuid4().hex  # unique user id. can be any alphanum string

    print(f"\n---Creating user: {user_id}")
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
        await client.memory.add(session_id=session_id, messages=[Message(**m)])

    #  Wait for the messages to be processed
    await asyncio.sleep(5)

    # Synthesize a question from most recent messages.
    # Useful for RAG apps. This is faster than using an LLM chain.
    # print("\n---Synthesize a question from most recent messages")
    # question = await client.memory.synthesize_question(session_id, last_n_messages=3)
    # print(f"Question: {question}")

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
    query = "What are Jane's favorite shoe brands?"
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

    # Extract session data from model
    print("\n---Extracting session data from model")
    extracted_data = await client.memory.extract_session_data_from_model(session_id, ShoeInfoModel(), last_n_messages=100)
    print("Extracted data: ", extracted_data.get_data())


class ShoeInfoModel(BaseDataExtractorModel):
    data: Dict[str, Any] = {}
    shoe_size: Optional[ZepDataClass] = ZepDataClass(
        type="ZepNumber", description="The user's shoe size", name="shoe_size"
    )
    shoe_budget: Optional[ZepDataClass] = ZepDataClass(
        type="ZepFloat", description="What is the purchasers budget?", name="shoe_budget"
    )


if __name__ == "__main__":
    asyncio.run(main())
