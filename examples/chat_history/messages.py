import os
import uuid

from dotenv import find_dotenv, load_dotenv

from examples.chat_history.chat_history_shoe_purchase import history
from zep_python import (
    APIError,
    NotFoundError,
    ZepClient,
)
from zep_python.memory import Memory, Session
from zep_python.message import Message
from zep_python.user import CreateUserRequest

load_dotenv(
    dotenv_path=find_dotenv()
)  # load environment variables from .env file, if present

API_KEY = os.environ.get("ZEP_API_KEY") or "YOUR_API_KEY"
API_URL = os.environ.get("ZEP_API_URL")  # only required if you're using Zep Open Source


def create_user(client):
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
        return user
    except APIError as e:
        print(f"Failed to create user: {e}")


def create_session(client, user_id):
    session_id = uuid.uuid4().hex
    print(f"Creating session: {session_id}")
    try:
        session = Session(
            session_id=session_id, user_id=user_id, metadata={"foo": "bar"}
        )
        result = client.memory.add_session(session)
        print(f"Session created: {result}")
        return session_id
    except APIError as e:
        print(f"Unable to create session {session_id}. Error: {e}")


def add_memory_to_session(client, session_id, history):
    print(f"addMemory for Session: {session_id}")
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
            f"API error occurred while adding memory to session {session_id}."
            f" Got error: {e}"
        )


def get_and_print_session_messages(client, session_id):
    try:
        session_messages = client.message.get_session_messages(session_id)
        print(f"Get Session Messages: {session_messages}")
        return session_messages
    except NotFoundError as e:
        print(f"Session not found for Session {session_id}. Got error: {e}")
    except APIError as e:
        print(
            "API error occurred while getting messages for Session"
            f" {session_id}. Got error: {e}"
        )


def get_and_print_first_session_message(client, session_id, message_id):
    try:
        session_message = client.message.get_session_message(session_id, message_id)
        print(f"Get Session Message: {session_message}")
    except NotFoundError as e:
        print(
            f"Session Message not found for Session {session_id} and Message "
            f"{message_id}. Got error: {e}"
        )
    except APIError as e:
        print(
            "API error occurred while getting message for Session"
            f" {session_id} and Message {message_id}. Got error: {e}"
        )


def update_and_print_session_message_metadata(client, session_id, message_id):
    updated_session_message_metadata = {"metadata": {"foo": "bar"}}
    try:
        updated_session_message = client.message.update_message_metadata(
            session_id, message_id, updated_session_message_metadata
        )
        print(f"Updated Session Message Metadata: {updated_session_message}")
    except NotFoundError as e:
        print(
            f"Session Message not found for Session {session_id} and "
            f"Message {message_id}. Got error: {e}"
        )
    except APIError as e:
        print(
            "API error occurred while updating message metadata for Session"
            f" {session_id} and Message {message_id}. Got error: {e}"
        )


def delete_and_print_memory_for_session(client, session_id):
    print(f"Deleting memory for Session: {session_id}")
    try:
        result = client.memory.delete_memory(session_id)
        print(f"Memory deleted: {result}")
    except NotFoundError:
        print("Memory not found for Session" + session_id)


def main():
    with ZepClient(api_key=API_KEY, api_url=API_URL) as client:
        user = create_user(client)
        session_id = create_session(client, user.user_id)
        add_memory_to_session(client, session_id, history)
        session_messages = get_and_print_session_messages(client, session_id)
        first_session_message_id = session_messages[0].uuid
        get_and_print_first_session_message(
            client, session_id, first_session_message_id
        )
        update_and_print_session_message_metadata(
            client, session_id, first_session_message_id
        )
        # Uncomment the following line to delete the memory for the session
        # delete_and_print_memory_for_session(client, session_id)


if __name__ == "__main__":
    main()
