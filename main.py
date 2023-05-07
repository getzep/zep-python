import asyncio
import httpx
from typing import List, Optional, Any, Dict

class Memory:
    def __init__(self, messages: List['Message'], metadata: Dict[str, Any], summary: 'Summary'):
        self.messages = messages
        self.metadata = metadata
        self.summary = summary

class Message:
    def __init__(self, content: str, created_at: str, metadata: Dict[str, Any], role: str, token_count: int, uuid: str):
        self.content = content
        self.created_at = created_at
        self.metadata = metadata
        self.role = role
        self.token_count = token_count
        self.uuid = uuid

class SearchPayload:
    def __init__(self, meta: Dict[str, Any], text: str):
        self.meta = meta
        self.text = text

class SearchResult:
    def __init__(self, dist: float, message: Message, meta: Dict[str, Any], summary: 'Summary'):
        self.dist = dist
        self.message = message
        self.meta = meta
        self.summary = summary

class Summary:
    def __init__(self, content: str, created_at: str, metadata: Dict[str, Any], recent_message_uuid: str, token_count: int, uuid: str):
        self.content = content
        self.created_at = created_at
        self.metadata = metadata
        self.recent_message_uuid = recent_message_uuid
        self.token_count = token_count
        self.uuid = uuid

class APIError:
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

class ZepClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient()

    @_sync
    async def get_memory(self, session_id: str, lastn: Optional[int] = None) -> List[Memory]:
        return await self.aget_memory(session_id, lastn)

    async def aget_memory(self, session_id: str, lastn: Optional[int] = None) -> List[Memory]:
        params = {'lastn': lastn} if lastn is not None else {}
        response = await self.client.get(f'{self.base_url}/api/v1/sessions/{session_id}/memory', params=params)
        response.raise_for_status()
        return [Memory(**memory) for memory in response.json()]

    @_sync
    async def add_memory(self, session_id: str, memory_messages: Memory) -> str:
        return await self.aadd_memory(session_id, memory_messages)

    async def aadd_memory(self, session_id: str, memory_messages: Memory) -> str:
        response = await self.client.post(f'{self.base_url}/api/v1/sessions/{session_id}/memory', json=memory_messages.__dict__)
        response.raise_for_status()
        return response.text

    @_sync
    async def delete_memory(self, session_id: str) -> str:
        return await self.adelete_memory(session_id)

    async def adelete_memory(self, session_id: str) -> str:
        response = await self.client.delete(f'{self.base_url}/api/v1/sessions/{session_id}/memory')
        response.raise_for_status()
        return response.text

    @_sync
    async def search_memory(self, session_id: str, search_payload: SearchPayload, limit: Optional[int] = None) -> List[SearchResult]:
        return await self.asearch_memory(session_id, search_payload, limit)

    async def asearch_memory(self, session_id: str, search_payload: SearchPayload, limit: Optional[int] = None) -> List[SearchResult]:
        params = {'limit': limit} if limit is not None else {}
        response = await self.client.post(f'{self.base_url}/api/v1/sessions/{session_id}/search', json=search_payload.__dict__, params=params)
        response.raise_for_status()
        return [SearchResult(**search_result) for search_result in response.json()]

    async def close(self):
        await self.client.aclose()

async def main():
    base_url = "http://example.com/api/v1"
    client = ZepLTMClient(base_url)

    # Example usage
    session_id = "your_session_id"

    # Get memory
    memories = await client.aget_memory(session_id)
    for memory in memories:
        print(memory.messages)

    # Add memory
    messages = [Message("Sample message", "2023-05-07T10:00:00", {}, "user", 3, "12345678-1234-1234-1234-1234567890ab")]
    metadata = {}
    summary = Summary("Sample summary", "2023-05-07T10:00:00", {}, "12345678-1234-1234-1234-1234567890ab", 3, "12345678-1234-1234-1234-1234567890cd")
    memory = Memory(messages, metadata, summary)

    result = await client.aadd_memory(session_id, memory)
    print(result)

    # Delete memory
    result = await client.adelete_memory(session_id)
    print(result)

    # Search memory
    search_payload = SearchPayload({}, "search query")
    search_results = await client.asearch_memory(session_id, search_payload)
    for search_result in search_results:
        print(search_result.message.content)

    await client.close()

if __name__ == "__main__":
    asyncio.run(main())
