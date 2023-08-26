""" Example of using the Zep Python SDK asynchronously.

    Note: Once a session is deleted, new messages cannot be added to it.
    The API will return a 400 error if you try to add messages to a deleted session.
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
            print(result)
        except NotFoundError as e:
            print(f"Unable to create session {session_id} got error: {e}")
        except APIError as e:
            print(f"Unable to create session {session_id} got error: {e}")

        # Update session metadata
        print(f"Updating session: {session_id}")
        try:
            # The new metadata values will be merged with the existing metadata
            session = Session(session_id=session_id, metadata={"bar": "foo"})
            result = await client.memory.aupdate_session(session)
            print(result)
        except NotFoundError as e:
            print(f"Unable to update session {session_id} got error: {e}")
        except APIError as e:
            print(f"Unable to update session {session_id} got error: {e}")

        # Get session
        print(f"Getting session: {session_id}")
        try:
            _ = await client.memory.aget_session(session_id)
        except NotFoundError:
            print("Session not found")

        # Get Memory for session
        print(f"\n1---getMemory for Session: {session_id}")
        try:
            memory = await client.memory.aget_memory(session_id)
            for message in memory.messages:
                print(message.to_dict())
        except NotFoundError:
            print("Memory not found")

        # Add Memory for session
        print(f"\n2---addMemory for Session: {session_id}")
        messages = [Message(**m) for m in history]
        memory = Memory(messages=messages)
        try:
            result = await client.memory.aadd_memory(session_id, memory)
            print(result)
        except NotFoundError as e:
            print(f"Unable to add memory to session {session_id}. Got error: {e}")
        except APIError as e:
            print(f"Unable to add memory to session {session_id}. Got error: {e}")

        # Naive wait for memory to be enriched and indexed
        time.sleep(2.0)

        # Get Memory for session
        print(f"\n3---getMemory for Session: {session_id}")
        try:
            memory = await client.memory.aget_memory(session_id)
            for message in memory.messages:
                print(message.to_dict())
        except NotFoundError:
            print(f"Memory not found for Session: {session_id}")

        # Search Memory for session
        search_payload = MemorySearchPayload(
            text="Name some popular destinations in Iceland?",
            metadata={
                "where": {"jsonpath": '$.system.entities[*] ? (@.Label == "LOC")'}
            },
        )
        print(f"\n4---searchMemory for Query: '{search_payload}'")
        try:
            search_results = await client.memory.asearch_memory(
                session_id, search_payload
            )
            for search_result in search_results:
                message_content = search_result.message
                print(message_content)
        except NotFoundError:
            print(f"Nothing found for Session {session_id}")

        # Delete Memory for session
        print(f"\n5---deleteMemory for Session {session_id}")
        try:
            result = await client.memory.adelete_memory(session_id)
            print(result)
        except NotFoundError:
            print(f"Memory not found for Session {session_id}")


if __name__ == "__main__":
    asyncio.run(main())
