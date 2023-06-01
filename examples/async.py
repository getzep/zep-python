""" Example of using the Zep Python SDK asynchronously.

    Note: Once a session is deleted, new messages cannot be added to it. The API will return
    a 400 error if you try to add messages to a deleted session.
"""
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


async def main() -> None:
    base_url = "http://localhost:8000"  # TODO: Replace with Zep API URL
    async with ZepClient(base_url) as client:
        session_id = uuid.uuid4().hex

        print(f"\n1---getMemory for Session: {session_id}")
        try:
            memory = await client.aget_memory(session_id)
            for message in memory.messages:
                print(message.to_dict())
        except NotFoundError:
            print("Memory not found")

        print(f"\n2---addMemory for Session: {session_id}")
        messages = [Message(**m) for m in history]
        memory = Memory(messages=messages)
        try:
            result = await client.aadd_memory(session_id, memory)
            print(result)
        except APIError as e:
            print(f"Unable to add memory to session {session_id}. Got error: {e}")

        # Naive wait for memory to be enriched and indexed
        time.sleep(2.0)

        print(f"\n3---getMemory for Session: {session_id}")
        try:
            memory = await client.aget_memory(session_id)
            for message in memory.messages:
                print(message.to_dict())
        except NotFoundError:
            print(f"Memory not found for Session: {session_id}")

        search_payload = MemorySearchPayload(
            text="Name some popular destinations in Iceland?",
            metadata={
                "where": {"jsonpath": '$.system.entities[*] ? (@.Label == "LOC")'}
            },
        )
        print(f"\n4---searchMemory for Query: '{search_payload}'")
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
