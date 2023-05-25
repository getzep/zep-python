import asyncio

from zep_python import (
    APIError,
    Memory,
    Message,
    NotFoundError,
    SearchPayload,
    ZepClient,
)


async def main() -> None:
    base_url = "http://localhost:8000"  # TODO: Replace with Zep API URL
    async with ZepClient(base_url) as client:
        session_id = "1234567890"

        print(f"\n1---getMemory for Session: {session_id}")
        try:
            memory = await client.aget_memory(session_id)
            for message in memory.messages:
                print(message.to_dict())
        except NotFoundError:
            print("Memory not found")

        print(f"\n2---addMemory for Session: {session_id}")
        history = [
            {
                "role": "user",
                "content": "I'm looking to plan a trip to Iceland. Can you help me?",
            },
            {
                "role": "assistant",
                "content": "Of course! I'd be happy to help you plan your trip.",
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
        messages = [Message(**m) for m in history]
        memory = Memory(messages=messages)
        try:
            result = await client.aadd_memory(session_id, memory)
            print(result)
        except APIError as e:
            print(f"Unable to add memory to session {session_id}. Got error: {e}")

        print(f"\n3---getMemory for Session: {session_id}")
        try:
            memory = await client.aget_memory(session_id)
            for message in memory.messages:
                print(message.to_dict())
        except NotFoundError:
            print(f"Memory not found for Session: {session_id}")

        search_payload = SearchPayload(text="Iceland")
        print(f"\n4---searchMemory for Query: '{search_payload.text}'")
        try:
            search_results = await client.asearch_memory(session_id, search_payload)
            for search_result in search_results:
                message_content = search_result.message
                print(message_content)
        except NotFoundError:
            print(f"Nothing found for Session {session_id}")

        print(f"\n5---deleteMemory for Session {session_id}")
        try:
            result = await client.adelete_memory(session_id)
            print(result)
        except NotFoundError:
            print(f"Memory not found for Session {session_id}")


if __name__ == "__main__":
    asyncio.run(main())
