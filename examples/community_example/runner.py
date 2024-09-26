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

from part1 import history as part1_history
from part2 import history as part2_history

from zep_python.client import AsyncZep
from zep_python.types import Message

load_dotenv(
    dotenv_path=find_dotenv()
)  # load environment variables from .env file, if present

API_KEY = os.environ.get("ZEP_API_KEY") or "YOUR_API_KEY"


async def seed_memory(client: AsyncZep, user_id: str) -> None:
    # Create a user

    await client.user.add(
        user_id=user_id,
        email="paul@example.com",
        first_name="Paul",
    )

    session_id = uuid.uuid4()
    # Create session associated with the above user
    print(f"\n---Creating session: {session_id}")

    await client.memory.add_session(
        session_id=session_id,
        user_id=user_id,
        metadata={"foo": "bar"},
    )

    # Get session
    print(f"\n---Getting session: {session_id}")
    session = await client.memory.get_session(session_id)
    print(f"Session details: {session}")

    # Add Memory for session
    print(f"\n---Add Memory for Session: {session_id}")
    for m in part1_history:
        print(f"{m['role']}: {m['content']}")
        await client.memory.add(session_id=session_id, messages=[Message(**m)])


async def continue_memory(client: AsyncZep, user_id: str) -> None:
    session_id = uuid.uuid4().hex  # unique session id. can be any alphanum string

    # Create session associated with the above user
    print(f"\n---Creating session: {session_id}")

    await client.memory.add_session(
        session_id=session_id,
        user_id=user_id,
        metadata={"foo": "bar"},
    )
    print(f"\n---Getting session: {session_id}")
    session = await client.memory.get_session(session_id)
    print(f"Session details: {session}")

    # Add Memory for session
    print(f"\n---Add Memory for Session: {session_id}")
    for m in part2_history:
        print(f"{m['role']}: {m['content']}")
        await client.memory.add(session_id=session_id, messages=[Message(**m)])


async def retrieve_memory(client: AsyncZep, session_id: str) -> None:
    memory = await client.memory.get(session_id)
    for f in memory.relevant_facts:
        print(f"Fact: {f.fact}")
    print("\n---End of Memory")


async def search_user_memory(client: AsyncZep, user_id: str, query: str) -> None:
    facts_result = await client.memory.search_sessions(
        user_id=user_id, text=query, search_scope="facts"
    )

    for f in facts_result.results:
        print(f"Fact: {f.fact.fact}")


async def main() -> None:
    client = AsyncZep(
        api_key=API_KEY,
    )
    user_id = str(uuid.uuid4())
    await seed_memory(client, user_id)
    await continue_memory(client, user_id)

    # print("\n---Retrieving Session Memory\n")
    # await retrieve_memory(client, "")
    # print("\n---Searching User Memory\n")
    # await search_user_memory(
    #     client,
    #     "",
    #     "Where does he primarily run?"
    # )
    # await client.memory.delete("")
    # await client.user.delete("")


if __name__ == "__main__":
    asyncio.run(main())
