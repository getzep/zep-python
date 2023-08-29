import uuid

from zep_python import APIError, ZepClient
from zep_python.memory.models import Session
from zep_python.user import CreateUserRequest


def main() -> None:
    base_url = "http://localhost:8000"  # TODO: Replace with Zep API URL
    api_key = "YOUR_API_KEY"  # TODO: Replace with your API key

    with ZepClient(base_url, api_key) as client:
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

        # Create multiple sessions associated with the user
        for i in range(3):
            session_id = uuid.uuid4().hex
            session = Session(
                session_id=session_id, user_id=user_id, metadata={"session": i + 1}
            )
            try:
                result = client.memory.add_session(session)
                print(f"Created session {i+1}: {result}")
            except APIError as e:
                print(f"Failed to create session {i+1}: {e}")

        # List all sessions associated with the user
        try:
            sessions = client.user.get_sessions(user_id)
            print(f"Sessions for user {user_id}:")
            for session in sessions:
                print(session.dict(exclude_unset=True), "\n")
        except APIError as e:
            print(f"Failed to list sessions for user {user_id}: {e}")


if __name__ == "__main__":
    main()
