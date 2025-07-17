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
from zep_cloud.types import Message

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

    # await asyncio.sleep(1)
    print(f"User added: {user_id}")
    thread_id = uuid.uuid4().hex  # unique session id. can be any alphanum string

    # Create session associated with the above user
    print(f"\n---Creating thread: {thread_id}")

    await client.thread.create(
        thread_id=thread_id,
        user_id=user_id,
    )

    # Get session
    print(f"\n---Getting thread: {thread_id}")
    session = await client.thread.get(thread_id)
    print(f"Thread details: {session}")

    # Add messages to the thread
    print(f"\n---Add messages to the thread: {thread_id}")
    for m in history:
        print(f"{m['role']}: {m['content']}")
        await client.thread.add_messages(thread_id=thread_id, messages=[Message(**m)])
        # await asyncio.sleep(0.5)

    #  Wait for the messages to be processed
    await asyncio.sleep(50)

    # Get user context for thread
    print(f"\n---Get user context for thread: {thread_id}")
    user_context = await client.thread.get_user_context(thread_id)

    print(f"User context: {user_context.context}")

    # Delete thread and clear context
    # Uncomment to run
    # print(f"\n6---delete thread memory : {thread_id}")
    # await client.thread.delete(thread_id)


if __name__ == "__main__":
    asyncio.run(main())