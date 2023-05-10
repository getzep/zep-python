import asyncio

from zep import Memory, Message, NotFoundError, SearchPayload, ZepClient


async def main() -> None:
    base_url = "http://localhost:8000"  # TODO: Replace with Zep API URL
    async with ZepClient(base_url) as client:
        # Example usage
        session_id = "2a2a2a"

        # Get memory
        print("****** GET MEMORY ******")
        print("Getting memory for session 3a3a3a")
        try:
            memories = await client.aget_memory("3a3a3a")
            for memory in memories:
                for message in memory.messages:
                    print(message.to_dict())
        except NotFoundError:
            print("Memory not found")

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
        try:
            memories = await client.aget_memory(session_id)
            for memory in memories:
                for message in memory.messages:
                    print(message.to_dict())
        except NotFoundError:
            print("Memory not found")

        # Add memory for a different session
        session_id = "5a5a5a"

        history = [
            {
                "role": "user",
                "content": ("I'm looking to plan a trip to Iceland. Can you help me?"),
            },
            {
                "role": "assistant",
                "content": ("Of course! I'd be happy to help you plan your trip."),
            },
            {
                "role": "user",
                "content": "What's the best time of year to go?",
            },
            {
                "role": "assistant",
                "content": (
                    "The best time to visit Iceland is from June to August. The"
                    " weather is milder, and you'll have more daylight for"
                    " sightseeing."
                ),
            },
            {
                "role": "user",
                "content": "Do I need a visa?",
            },
            {
                "role": "assistant",
                "content": (
                    "Visa requirements depend on your nationality. Citizens of"
                    " the Schengen Area, the US, Canada, and several other"
                    " countries can visit Iceland for up to 90 days without a"
                    " visa."
                ),
            },
        ]
        memories = [Message(**m) for m in history]
        memory = Memory(messages=memories)
        result = await client.aadd_memory(session_id, memory)
        print(result)
        # Search memory
        search_payload = SearchPayload({}, "Iceland")
        search_results = await client.asearch_memory(session_id, search_payload)
        for search_result in search_results:
            # Access the 'content' field within the 'message' object.
            message_content = search_result.message
            print(message_content)


if __name__ == "__main__":
    asyncio.run(main())
