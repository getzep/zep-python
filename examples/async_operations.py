from __future__ import annotations

import asyncio

from models import Memory, Message, SearchPayload
from zep_client import ZepClient


async def main() -> None:
    base_url = "http://localhost:8000"  # TODO: Replace with Zep API URL
    async with ZepClient(base_url) as client:
        # Example usage
        session_id = "2a2a2a"

        # Get memory
        print("****** GET MEMORY ******")
        print("Getting memory for session 3a3a3a")
        memories = await client.aget_memory("3a3a3a")
        for memory in memories:
            for message in memory.messages:
                print(message.to_dict())

        # Add memory
        print("****** ADD MEMORY ******")
        print("Adding new memory for session 2a2a2a")
        role = "user"
        content = "who was the first man to go to space"
        message = Message(role=role, content=content)

        memory = Memory()
        memory.messages = [message]

        result = await client.aadd_memory(session_id, memory)
        memories = await client.aget_memory(session_id)
        for memory in memories:
            for message in memory.messages:
                print(message.to_dict())

        # Delete memory
        result = await client.adelete_memory(session_id)
        print(result)
        print("Getting memory for session 2a2a2a")
        memories = await client.aget_memory("2a2a2a")
        for memory in memories:
            for message in memory.messages:
                print(message.to_dict())

        # Search memory
        search_payload = SearchPayload({}, "Iceland")
        search_results = await client.asearch_memory(session_id, search_payload)
        for search_result in search_results:
            # Access the 'content' field within the 'message' object.
            message_content = search_result.message
            print(message_content)


if __name__ == "__main__":
    asyncio.run(main())
