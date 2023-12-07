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
from zep_python.message import Message
from zep_python.user import CreateUserRequest

def main() -> None:
    base_url = "http://localhost:8000"  # TODO: Replace with Zep API URL
    api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.e30.nEJCptN3CRfD_SQ4om4Oa2yh-ARPI41qkjj0La0Hw54"  # TODO: Replace with your API key
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

        print(f"\n2---addMemory for Session: {session_id}")
        try:
            for m in history:
                message = Message(**m)
                memory = Memory(messages=[message])
                client.memory.add_memory(session_id, memory)
            print(f"Added {len(history)} messages to memory for session {session_id}")
        except NotFoundError as e:
            print(f"Memory not found for session {session_id}. Got error: {e}")
        except APIError as e:
            print(
                f"API error occurred while adding memory to session {session_id}. Got"
                f" error: {e}"
            )

        # Get session messages
        session_messages = client.message.get_session_messages(session_id)
        print(f"Get Session Messages: {session_messages}")

        # Get Session Message
        
        # get first session message
        first_session_message_id = session_messages[0].uuid
        print(f"Get Session Message: {first_session_message_id}")

        session_message = client.message.get_session_message(session_id, first_session_message_id)
        print(f"Get Session Message: {session_message}")

        updated_session_message_metadata = {"metadata": {"foo": "bar"}}
        updated_session_message = client.message.update_message_metadata(
            session_id, first_session_message_id, updated_session_message_metadata
        )
        print(f"Updated Session Message Metadata: {updated_session_message}")

        # Delete memory
        print(f"Deleting memory for Session: {session_id}")
        try:
            result = client.memory.delete_memory(session_id)
            print(f"Memory deleted: {result}")
        except NotFoundError:
            print("Memory not found for Session" + session_id)






if __name__ == "__main__":
    main()