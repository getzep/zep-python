import uuid

from zep_python import APIError, ZepClient
from zep_python.user import CreateUserRequest, UpdateUserRequest


def main() -> None:
    base_url = "http://localhost:8000"  # TODO: Replace with Zep API URL
    api_key = "YOUR_API_KEY"  # TODO: Replace with your API key

    with ZepClient(base_url, api_key) as client:
        # Create multiple users
        for i in range(3):
            user_id = uuid.uuid4().hex
            user_request = CreateUserRequest(
                user_id=user_id,
                email=f"user{i}@example.com",
                first_name=f"John{i}",
                last_name=f"Doe{i}",
                metadata={"foo": "bar"},
            )
            try:
                user = client.user.add(user_request)
                print(f"Created user {i+1}: {user.user_id}")
            except APIError as e:
                print(f"Failed to create user {i+1}: {e}")

        # Update the first user
        user_id = client.user.list()[0].user_id
        user_request = UpdateUserRequest(
            user_id=user_id,
            email="updated_user@example.com",
            first_name="UpdatedJohn",
            last_name="UpdatedDoe",
            metadata={"foo": "updated_bar"},
        )
        try:
            updated_user = client.user.update(user_request)
            print(f"Updated user: {updated_user.user_id}")
        except APIError as e:
            print(f"Failed to update user: {e}")

        # Delete the second user
        user_id = client.user.list()[1].user_id
        try:
            client.user.delete(user_id)
            print(f"Deleted user: {user_id}")
        except APIError as e:
            print(f"Failed to delete user: {e}")

        # List all users
        try:
            users_generator = client.user.list_chunked()
            print("All users:")
            while True:
                users = next(users_generator, None)
                if users is None:
                    break
                for user in users:
                    print(user.user_id)
        except APIError as e:
            print(f"Failed to list users: {e}")


if __name__ == "__main__":
    main()
