""" Example of using the Zep Python SDK.

    Note: Once a session is deleted, new messages cannot be added to it.
    The API will return a 400 error if you try to add messages to a deleted session.
"""
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
    base_url = "http://localhost:8000"  # TODO: Replace with Zep API URL
    api_key = "YOUR_API_KEY"  # TODO: Replace with your API key
    with ZepClient(base_url, api_key) as client:
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

        #
        # Create session associated with the above user
        #
        session_id = uuid.uuid4().hex
        print(f"Creating session: {session_id}")
        try:
            session = Session(
                session_id=session_id, user_id=user_id, metadata={"foo": "bar"}
            )
            result = client.memory.add_session(session)
            print(result)
        except APIError as e:
            print(f"Unable to create session {session_id} got error: {e}")

        #
        # Update session metadata
        #
        print(f"Updating session: {session_id}")
        try:
            # The new metadata values will be merged with the existing metadata
            session = Session(session_id=session_id, metadata={"bar": "foo"})
            result = client.memory.update_session(session)
            print(result)
        except APIError as e:
            print(f"Unable to update session {session_id} got error: {e}")

        #
        # Get session
        #
        print(f"Getting session: {session_id}")
        try:
            session = client.memory.get_session(session_id)
            print(session.dict())
        except NotFoundError:
            print("Session not found")

        #
        # Get memory
        #
        print(f"\n1---getMemory for Session: {session_id}")
        try:
            memory = client.memory.get_memory(session_id)
            for message in memory.messages:
                print(message.to_dict())
        except NotFoundError:
            print("Memory not found")

        #
        # Add memory
        #
        print("\n2---addMemory for Session: " + session_id)
        messages = [Message(**m) for m in history]  # type: ignore
        memory = Memory(messages=messages)
        try:
            result = client.memory.add_memory(session_id, memory)
            print(result)
        except APIError as e:
            print(f"Unable to add memory to session {session_id} got error: {e}")

        # Naive wait for memory to be enriched and indexed
        time.sleep(2.0)

        #
        # Get memory we just added
        #
        print(f"\n3---getMemory for Session: {session_id}")
        try:
            memory = client.memory.get_memory(session_id)
            for message in memory.messages:
                print(message.to_dict())
        except NotFoundError:
            print("Memory not found for Session: " + session_id)

        #
        # Search memory
        #
        search_payload = MemorySearchPayload(
            text="Name some popular destinations in Iceland?",
            metadata={
                "where": {"jsonpath": '$.system.entities[*] ? (@.Label == "LOC")'}
            },
        )
        print(f"\n4---searchMemory for Query: '{search_payload}'")
        # Search memory
        try:
            search_results = client.memory.search_memory(session_id, search_payload)
            for search_result in search_results:
                # Access the 'content' field within the 'message' object.
                message_content = search_result.message
                print(message_content)
        except NotFoundError:
            print("Nothing found for Session" + session_id)

        #
        # Delete memory
        #
        print(f"Deleting memory for Session: {session_id}")
        try:
            result = client.memory.delete_memory(session_id)
            print(result)
        except NotFoundError:
            print("Memory not found for Session" + session_id)


if __name__ == "__main__":
    main()
