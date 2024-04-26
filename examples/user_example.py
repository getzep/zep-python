import asyncio
import os
import uuid

from dotenv import find_dotenv, load_dotenv

from zep.types import ApiError, Session
from zep.client import AsyncZep

load_dotenv(
    dotenv_path=find_dotenv()
)  # load environment variables from .env file, if present

API_KEY = os.environ.get("ZEP_API_KEY") or "YOUR_API_KEY"
API_URL = os.environ.get("ZEP_API_URL")  # only required if you're using Zep Open Source


async def main() -> None:
    client = AsyncZep(api_key=API_KEY, base_url=f"{API_URL}/api/v2")
    # Create multiple users
    for i in range(3):
        user_id = f"user{i}" + uuid.uuid4().hex
        try:
            user = await client.user.add(
                user_id=user_id,
                email=f"user{i}@example.com",
                first_name=f"John{i}",
                last_name=f"Doe{i}",
                metadata={"foo": "bar"},
            )
            print(f"Created user {i+1}: {user.user_id}")
        except ApiError as e:
            print(f"Failed to create user {i+1}: {e}")

    # Update the first user
    user_list = await client.user.list()
    user_id = user_list[0].user_id
    try:
        updated_user = await client.user.update(
            user_id=user_id,
            email="updated_user@example.com",
            first_name="UpdatedJohn",
            last_name="UpdatedDoe",
            metadata={"foo": "updated_bar"},
        )
        print(f"Updated user: {updated_user.user_id}")
    except ApiError as e:
        print(f"Failed to update user: {e}")

    # Create a Session for the first user
    session_id = uuid.uuid4().hex
    try:
        result = await client.memory.add_session(
            session_id=session_id, user_id=user_id, metadata={"session": i + 1}
        )
        print(f"Created session {i+1}: {result}")
    except ApiError as e:
        print(f"Failed to create session {i+1}: {e}")

    # Delete the second user
    user_list = await client.user.list(1, 1)
    user_id = user_list[0].user_id
    try:
        await client.user.delete(user_id=user_id)
        print(f"Deleted user: {user_id}")
    except ApiError as e:
        print(f"Failed to delete user: {e}")

    # List all users
    try:
        users_generator = client.user.list_ordered()
        print("All users:")
        async for users in users_generator:
            if users is None:
                break
            for user in users:
                print(user.user_id)
    except ApiError as e:
        print(f"Failed to list users: {e}")



if __name__ == "__main__":
    asyncio.run(main())