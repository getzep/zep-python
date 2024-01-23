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
import time
import uuid

from chat_history import history
from dotenv import load_dotenv

from zep_python import (
    APIError,
    NotFoundError,
    ZepClient,
)
from zep_python.memory import Memory, MemorySearchPayload, Session
from zep_python.message import Message
from zep_python.user import CreateUserRequest

load_dotenv()  # load environment variables from .env file, if present

API_KEY = os.environ.get("ZEP_API_KEY") or "YOUR_API_KEY"
API_URL = os.environ.get("ZEP_API_URL")  # only required if you're using Zep Open Source


async def create_user(client, user_id):
    user_request = CreateUserRequest(
        user_id=user_id,
        email="user@example.com",
        first_name="John",
        last_name="Doe",
        metadata={"foo": "bar"},
    )
    try:
        user = await client.user.aadd(user_request)
        print(f"Created user: {user.user_id}")
    except APIError as e:
        print(f"Failed to create user: {e}")


async def create_session(client, user_id, session_id):
    try:
        session = Session(
            session_id=session_id, user_id=user_id, metadata={"foo": "bar"}
        )
        result = await client.memory.aadd_session(session)
        print(f"Session created: {result}")
    except APIError as e:
        print(
            f"API error occurred while adding memory to session {session_id}. Got"
            f" error: {e}"
        )


async def update_session(client, session_id):
    try:
        session = Session(session_id=session_id, metadata={"bar": "foo"})
        result = await client.memory.aupdate_session(session)
        print(f"Session updated: {result}")
    except NotFoundError as e:
        print(f"Memory not found for session {session_id}. Got error: {e}")
    except APIError as e:
        print(
            f"API error occurred while adding memory to session {session_id}. Got"
            f" error: {e}"
        )


async def get_session(client, session_id):
    try:
        session = await client.memory.aget_session(session_id)
        print(f"Session details: {session}")
    except NotFoundError:
        print("Session not found")


async def add_memory_to_session(client, session_id):
    try:
        for m in history:
            message = Message(**m)
            memory = Memory(messages=[message])
            await client.memory.aadd_memory(session_id, memory)
        print(f"Added {len(history)} messages to memory for session {session_id}")
    except NotFoundError as e:
        print(f"Memory not found for session {session_id}. Got error: {e}")
    except APIError as e:
        print(
            f"API error occurred while adding memory to session {session_id}. Got"
            f" error: {e}"
        )


async def get_memory_from_session(client, session_id):
    print(
        f"\nGetting most recent memory. We're pausing until all {len(history)} messages are embedded and summarized.\n"
    )
    memory = Memory()
    try:
        while memory.summary is None:
            memory = await client.memory.aget_memory(
                session_id, memory_type="perpetual"
            )
            time.sleep(0.5)

        print(f"Summary: {memory.summary.content}")
        for message in memory.messages:
            print(f"Message: {message.to_dict()}")
    except NotFoundError:
        print(f"Memory not found for Session: {session_id}")


async def search_memory(client, session_id, search_payload: MemorySearchPayload):
    try:
        search_results = await client.memory.asearch_memory(
            session_id, search_payload, limit=3
        )
        for search_result in search_results:
            if search_payload.search_scope == "messages":
                print(f"Result: {search_result.message.content}")
            else:
                print(f"Result: {search_result.summary.content}")
            print(f"Score: {search_result.dist}")
    except NotFoundError:
        print(f"Nothing found for Session {session_id}")


async def delete_session(client, session_id):
    try:
        result = await client.memory.adelete_memory(session_id)
        print(f"Memory deleted: {result}")
    except NotFoundError:
        print(f"Memory not found for Session {session_id}")


async def main() -> None:
    client = ZepClient(api_key=API_KEY, api_url=API_URL)

    # Create a user
    user_id = uuid.uuid4().hex  # unique user id. can be any alphanum string
    await create_user(client, user_id)

    session_id = uuid.uuid4().hex  # unique session id. can be any alphanum string

    # Create session associated with the above user
    print(f"\n---Creating session: {session_id}")
    await create_session(client, user_id, session_id)

    # Update session metadata
    print(f"\n---Updating session: {session_id}")
    await update_session(client, session_id)

    # Get session
    print(f"\n---Getting session: {session_id}")
    await get_session(client, session_id)

    # Add Memory for session
    print(f"\n---Add Memory for Session: {session_id}")
    await add_memory_to_session(client, session_id)

    # Get Memory for session
    print(f"\n---Get Memory for Session: {session_id}")
    await get_memory_from_session(client, session_id)

    # Search Memory for session
    query = "What type of food can you eat in Iceland?"
    print(f"\n---Searching over summaries for: '{query}'")
    search_payload = MemorySearchPayload(
        text=query,
        search_scope="summary",
    )
    await search_memory(client, session_id, search_payload)

    print("\n---Searching over summaries with MMR Reranking")
    search_payload = MemorySearchPayload(
        text=query,
        search_scope="summary",
        search_type="mmr",
    )
    await search_memory(client, session_id, search_payload)

    print("\n---Searching over messages using a metadata filter")
    search_payload = MemorySearchPayload(
        text=query,
        search_scope="messages",
        metadata={"where": {"jsonpath": '$[*] ? (@.bar == "foo")'}},
    )
    await search_memory(client, session_id, search_payload)

    # Delete Memory for session
    # Uncomment to run
    # print(f"\n5---deleteMemory for Session: {session_id}")
    # await delete_memory_from_session(client, session_id)


if __name__ == "__main__":
    asyncio.run(main())
