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

from zep_python.client import AsyncZep
from zep_python.types import Message

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

    await client.memory.add_session(
        session_id=session_id,
        user_id=user_id,
        metadata={"foo": "bar"},
    )

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

    # Get Memory for session
    print(f"\n---Get Perpetual Memory for Session: {session_id}")
    memory = await client.memory.get(session_id, memory_type="perpetual")
    print(f"Memory: {memory}")
    print("\n---End of Memory")

    query = "What are Jane's favorite shoe brands?"
    print(f"\n---Searching over user facts for: '{query}'")
    facts_result = await client.memory.search_sessions(
        user_id=user_id, text=query, search_scope="facts"
    )
    print("facts_result: ", facts_result)

    # Delete Memory for session
    # Uncomment to run
    # print(f"\n6---deleteMemory for Session: {session_id}")
    # await client.memory.delete(session_id)


if __name__ == "__main__":
    asyncio.run(main())
