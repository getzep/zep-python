""" Example of using the Zep Python SDK asynchronously.
This script demonstrates the following functionalities:
1. Creating a user using the ZepClient.
2. Creating a session associated with the created user.
3. Adding messages to the session.
4. Searching the session memory for a specific query.
5. Searching the session memory with MMR reranking.
6. Deleting the session memory.

Please replace the base_url and api_key with your Zep API URL and your API key respectively.

"""
import asyncio
import time
import uuid

from chat_history import history

from zep_python import (
    APIError,
    Memory,
    MemorySearchPayload,
    Message,
    NotFoundError,
    ZepClient,
)
from zep_python.memory import Session
from zep_python.user import CreateUserRequest


async def main() -> None:
    base_url = "http://localhost:8000"  # TODO: Replace with Zep API URL
    api_key = "YOUR_API_KEY"  # TODO: Replace with your API key
    async with ZepClient(base_url, api_key) as client:
        # Create a user
        user_id = uuid.uuid4().hex
        user_request = CreateUserRequest(
            user_id=user_id,
            email="user@example.com",
            first_name="John",
            last_name="Doe",
            metadata={"foo": "bar"},
        )
        try:
            user = client.user.add(user_request)
            print(f"Created user: {user.user_id}")
        except APIError as e:
            print(f"Failed to create user: {e}")

        session_id = uuid.uuid4().hex
        print(f"------Memory operations: {session_id}")

        # Create session associated with the above user
        print(f"Creating session: {session_id}")
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

        # Update session metadata
        print(f"Updating session: {session_id}")
        try:
            # The new metadata values will be merged with the existing metadata
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

        # Get session
        print(f"Getting session: {session_id}")
        try:
            session = await client.memory.aget_session(session_id)
            print(f"Session details: {session.dict()}")
        except NotFoundError:
            print("Session not found")

        # Add Memory for session
        print(f"\n2---addMemory for Session: {session_id}")
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

        # Naive wait for memory to be enriched and indexed
        time.sleep(5.0)

        # Get Memory for session
        print(f"\n3---getMemory for Session: {session_id}")
        try:
            memory = await client.memory.aget_memory(session_id)
            for message in memory.messages:
                print(f"Message: {message.to_dict()}")
        except NotFoundError:
            print(f"Memory not found for Session: {session_id}")

        # Search Memory for session
        query = "Can you name some popular destinations in Iceland?"
        search_payload = MemorySearchPayload(
            text=query,
            metadata={
                "where": {"jsonpath": '$.system.entities[*] ? (@.Label == "GPE")'}
            },
        )
        print(f"\n4---searchMemory for Query: '{query}'")
        try:
            search_results = await client.memory.asearch_memory(
                session_id, search_payload
            )
            for search_result in search_results:
                message_content = search_result.message
                print(f"Search result: {message_content}")
        except NotFoundError:
            print(f"Nothing found for Session {session_id}")

        # Search memory with MMR reranking
        search_payload = MemorySearchPayload(
            text=query,
            search_type="mmr",
            mmr_lambda=0.5,
        )
        print(f"\n4---searchMemory for MMR Query: '{query}'")
        try:
            search_results = await client.memory.asearch_memory(
                session_id, search_payload, limit=3
            )
            for search_result in search_results:
                message_content = search_result.message
                print(f"Search result: {message_content}")
        except NotFoundError:
            print(f"Nothing found for Session {session_id}")

        # Search Summary with MMR reranking
        search_payload = MemorySearchPayload(
            text=query,
            search_scope="summary",
            search_type="mmr",
            mmr_lambda=0.5,
        )
        print(f"\n4---searchMemory for MMR Query: '{query}'")
        try:
            search_results = client.memory.search_memory(
                session_id, search_payload, limit=3
            )
            for search_result in search_results:
                message_content = search_result.summary
                print(f"Search result: {message_content}")
        except NotFoundError:
            print("Nothing found for Session" + session_id)

        # Delete Memory for session
        print(f"\n5---deleteMemory for Session: {session_id}")
        try:
            result = await client.memory.adelete_memory(session_id)
            print(f"Memory deleted: {result}")
        except NotFoundError:
            print(f"Memory not found for Session {session_id}")


if __name__ == "__main__":
    asyncio.run(main())
