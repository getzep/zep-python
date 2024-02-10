import asyncio
import os
import uuid

from dotenv import find_dotenv, load_dotenv

from zep_python import APIError, ZepClient
from zep_python.memory import Session
from zep_python.user import CreateUserRequest, UpdateUserRequest

load_dotenv(
    dotenv_path=find_dotenv()
)  # load environment variables from .env file, if present

API_KEY = os.environ.get("ZEP_API_KEY") or "YOUR_API_KEY"
API_URL = os.environ.get("ZEP_API_URL")  # only required if you're using Zep Open Source


async def main() -> None:
    with ZepClient(api_key=API_KEY, api_url=API_URL) as client:
        # Create multiple users
        for i in range(3):
            user_id = f"user{i}" + uuid.uuid4().hex
            user_request = CreateUserRequest(
                user_id=user_id,
                email=f"user{i}@example.com",
                first_name=f"John{i}",
                last_name=f"Doe{i}",
                metadata={"foo": "bar"},
            )
            try:
                user = await client.user.aadd(user_request)
                print(f"Created user {i+1}: {user.user_id}")
            except APIError as e:
                print(f"Failed to create user {i+1}: {e}")

        # Update the first user
        user_list = await client.user.alist(1)
        user_id = user_list[0].user_id
        user_request = UpdateUserRequest(
            user_id=user_id,
            email="updated_user@example.com",
            first_name="UpdatedJohn",
            last_name="UpdatedDoe",
            metadata={"foo": "updated_bar"},
        )
        try:
            updated_user = await client.user.aupdate(user_request)
            print(f"Updated user: {updated_user.user_id}")
        except APIError as e:
            print(f"Failed to update user: {e}")

        # Create a Session for the first user
        session_id = uuid.uuid4().hex
        session = Session(
            session_id=session_id, user_id=user_id, metadata={"session": i + 1}
        )
        try:
            result = await client.memory.aadd_session(session)
            print(f"Created session {i+1}: {result}")
        except APIError as e:
            print(f"Failed to create session {i+1}: {e}")

        # Delete the second user
        user_list = await client.user.alist(1, 1)
        user_id = user_list[0].user_id
        try:
            await client.user.adelete(user_id)
            print(f"Deleted user: {user_id}")
        except APIError as e:
            print(f"Failed to delete user: {e}")

        # List all users
        try:
            users_generator = client.user.alist_chunked()
            print("All users:")
            async for users in users_generator:
                if users is None:
                    break
                for user in users:
                    print(user.user_id)
        except APIError as e:
            print(f"Failed to list users: {e}")


if __name__ == "__main__":
    asyncio.run(main())
