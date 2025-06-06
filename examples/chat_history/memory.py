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

from chat_history_shoe_purchase import history

from zep_cloud.client import AsyncZep
from zep_cloud.types import Message, FactRatingInstruction, FactRatingExamples

load_dotenv(
    dotenv_path=find_dotenv()
)  # load environment variables from .env file, if present

API_KEY = os.environ.get("ZEP_API_KEY") or "YOUR_API_KEY"


async def main() -> None:
    client = AsyncZep(
        api_key=API_KEY,
    )

    # Create a user
    user_id = uuid.uuid4().hex  # unique user id. can be any alphanum string
    fact_rating_instruction = """Rate the facts by poignancy. Highly poignant 
    facts have a significant emotional impact or relevance to the user. 
    Facts with low poignancy are minimally relevant or of little emotional
    significance."""
    fact_rating_examples = FactRatingExamples(
        high="The user received news of a family member's serious illness.",
        medium="The user completed a challenging marathon.",
        low="The user bought a new brand of toothpaste.",
    )
    await client.user.add(
        user_id=user_id,
        email="user@example.com",
        first_name="Jane",
        last_name="Smith",
        metadata={"vip": "true"},
    )

    # await asyncio.sleep(1)
    print(f"User added: {user_id}")
    session_id = uuid.uuid4().hex  # unique session id. can be any alphanum string

    # Create session associated with the above user
    print(f"\n---Creating session: {session_id}")

    await client.memory.add_session(
        session_id=session_id,
        user_id=user_id,
        metadata={"foo": "bar"},
    )
    # await asyncio.sleep(1)
    # Update session metadata
    print(f"\n---Updating session: {session_id}")
    await client.memory.update_session(session_id=session_id, metadata={"bar": "foo"})
    # await asyncio.sleep(3)
    # Get session
    print(f"\n---Getting session: {session_id}")
    session = await client.memory.get_session(session_id)
    print(f"Session details: {session}")
    # await asyncio.sleep(3)

    # Add Memory for session
    print(f"\n---Add Memory for Session: {session_id}")
    for m in history:
        print(f"{m['role']}: {m['content']}")
        await client.memory.add(session_id=session_id, messages=[Message(**m)])
        # await asyncio.sleep(0.5)

    #  Wait for the messages to be processed
    await asyncio.sleep(50)

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
    memory = await client.memory.get(session_id)
    print(f"Memory: {memory}")
    print("\n---End of Memory")

    print(f"Memory context: {memory.context}")

    # Delete Memory for session
    # Uncomment to run
    # print(f"\n6---deleteMemory for Session: {session_id}")
    # await client.memory.delete(session_id)


if __name__ == "__main__":
    asyncio.run(main())