""" Example of using the Zep Python SDK.

    Note: Once a session is deleted, new messages cannot be added to it. The API will return
    a 400 error if you try to add messages to a deleted session.
"""
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


def main() -> None:
    base_url = "http://localhost:8000"  # TODO: Replace with Zep API URL
    with ZepClient(base_url) as client:
        # Example usage
        session_id = uuid.uuid4().hex

        #
        # Get memory
        #
        print(f"\n1---getMemory for Session: {session_id}")
        try:
            memory = client.get_memory(session_id)
            for message in memory.messages:
                print(message.to_dict())
        except NotFoundError:
            print("Memory not found")

        #
        # Add memory
        #
        print("\n2---addMemory for Session: " + session_id)
        messages = [Message(**m) for m in history]  # type: ignore
        memory = Memory(messages=messages)
        try:
            result = client.add_memory(session_id, memory)
            print(result)
        except APIError as e:
            print(f"Unable to add memory to session {session_id} got error: {e}")

        # Naive wait for memory to be enriched and indexed
        time.sleep(2.0)

        #
        # Get memory we just added
        #
        print(f"\n3---getMemory for Session: {session_id}")
        try:
            memory = client.get_memory(session_id)
            for message in memory.messages:
                print(message.to_dict())
        except NotFoundError:
            print("Memory not found for Session: " + session_id)

        #
        # Search memory
        #
        search_payload = MemorySearchPayload(
            text="Name some popular destinations in Iceland?",
            metadata={
                "where": {"jsonpath": '$.system.entities[*] ? (@.Label == "LOC")'}
            },
        )
        print(f"\n4---searchMemory for Query: '{search_payload}'")
        # Search memory
        try:
            search_results = client.search_memory(session_id, search_payload)
            for search_result in search_results:
                # Access the 'content' field within the 'message' object.
                message_content = search_result.message
                print(message_content)
        except NotFoundError:
            print("Nothing found for Session" + session_id)

        #
        # Delete memory
        #
        print(f"Deleting memory for Session: {session_id}")
        try:
            result = client.delete_memory(session_id)
            print(result)
        except NotFoundError:
            print("Memory not found for Session" + session_id)


if __name__ == "__main__":
    main()
