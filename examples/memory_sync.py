""" This is an example of how to use the Zep Python SDK to interact with the Zep API.

The script demonstrates the following functionalities:
1. Creating a user using the ZepClient.
2. Creating a session associated with the created user.
3. Adding messages to the session.
4. Searching the session memory for a specific query.
5. Searching the session memory with MMR reranking.
6. Deleting the session memory.

Please replace the base_url and api_key with your Zep API URL and your API key respectively.
"""
import os
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


def main() -> None:
    project_api_key = os.environ.get("PROJECT_API_KEY")
    if project_api_key is None:
        raise ValueError("PROJECT_API_KEY environment variable must be set")

    with ZepClient(
        project_api_key=project_api_key, base_url=None, api_key=None
    ) as client:
        # Example usage

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

        # Create session associated with the above user
        session_id = uuid.uuid4().hex
        print(f"Creating session: {session_id}")
        try:
            session = Session(
                session_id=session_id, user_id=user_id, metadata={"foo": "bar"}
            )
            result = client.memory.add_session(session)
            print(f"Session created: {result}")
        except APIError as e:
            print(f"Unable to create session {session_id}. Error: {e}")

        # Update session metadata
        print(f"Updating session: {session_id}")
        try:
            # The new metadata values will be merged with the existing metadata
            session = Session(session_id=session_id, metadata={"bar": "foo"})
            result = client.memory.update_session(session)
            print(f"Session updated: {result}")
        except APIError as e:
            print(f"Unable to update session {session_id}. Error: {e}")

        # Get session
        print(f"Getting session: {session_id}")
        try:
            session = client.memory.get_session(session_id)
            print(f"Session details: {session.dict()}")
        except NotFoundError:
            print("Session not found")

        # Add memory
        print("\n2---addMemory for Session: " + session_id)
        try:
            for m in history:
                message = Message(**m)
                memory = Memory(messages=[message])
                client.memory.add_memory(session_id, memory)
            print(f"Added {len(history)} messages to memory for session {session_id}")
        except APIError as e:
            print(f"Unable to add memory to session {session_id}. Error: {e}")

        # Naive wait for memory to be enriched and indexed
        time.sleep(5.0)

        # Get memory we just added
        print(f"\n3---getMemory for Session: {session_id}")
        try:
            memory = client.memory.get_memory(session_id)
            for message in memory.messages:
                print(f"Message: {message.dict()}")
        except NotFoundError:
            print("Memory not found for Session: " + session_id)

        # Search memory
        query = "Can you name some popular destinations in Iceland?"
        search_payload = MemorySearchPayload(
            text=query,
            metadata={
                "where": {"jsonpath": '$.system.entities[*] ? (@.Label == "LOC")'}
            },
        )
        print(f"\n4---searchMemory for Query: '{query}'")
        try:
            search_results = client.memory.search_memory(session_id, search_payload)
            for search_result in search_results:
                message_content = search_result.message
                print(f"Search result: {message_content}")
        except NotFoundError:
            print("Nothing found for Session" + session_id)

        # Search memory with MMR reranking
        search_payload = MemorySearchPayload(
            text=query,
            search_type="mmr",
            mmr_lambda=0.5,
        )
        print(f"\n4---searchMemory for MMR Query: '{query}'")
        try:
            search_results = client.memory.search_memory(
                session_id, search_payload, limit=3
            )
            for search_result in search_results:
                message_content = search_result.message
                print(f"Search result: {message_content}")
        except NotFoundError:
            print("Nothing found for Session" + session_id)

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

        # Delete memory
        print(f"Deleting memory for Session: {session_id}")
        try:
            result = client.memory.delete_memory(session_id)
            print(f"Memory deleted: {result}")
        except NotFoundError:
            print("Memory not found for Session" + session_id)


if __name__ == "__main__":
    main()
