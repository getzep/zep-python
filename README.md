[![Tests](https://github.com/getzep/zep-python/actions/workflows/test.yml/badge.svg)](https://github.com/getzep/zep-python/actions/workflows/test.yml) [![lint](https://github.com/getzep/zep-python/actions/workflows/lint.yml/badge.svg)](https://github.com/getzep/zep-python/actions/workflows/lint.yml) [![Release to PyPI](https://github.com/getzep/zep-python/actions/workflows/release.yml/badge.svg)](https://github.com/getzep/zep-python/actions/workflows/release.yml) ![GitHub](https://img.shields.io/github/license/getzep/zep-python?color=blue)

# Zep: A long-term memory store for conversational AI applications

This is the Python client package for the Zep service. For more information about Zep, see https://github.com/getzep/zep.

### Installation

```bash
pip install zep-python
```

or

```bash
poetry add zep-python
```

## Quick Start

Ensure that you have a Zep server running. See https://github.com/getzep/zep.

```python
import asyncio

from zep_python import Memory, Message, SearchPayload, ZepClient

base_url = "http://localhost:8000"  # TODO: Replace with Zep API URL
session_id = "2a2a2a" # an identifier for your user's session.

async with ZepClient(base_url) as client:

    role = "user"
    content = "who was the first man to go to space?"
    message = Message(role=role, content=content)
    memory = Memory()
    memory.messages = [message]
    # Add a memory
    result = await client.aadd_memory(session_id, memory)

    # Long chat histories will automatically be summarized.
    # A summary and chat history are returned with a `get_memory`
    memories = await client.aget_memory(session_id)
    for memory in memories:
        for message in memory.messages:
            print(message.to_dict())

    # Search memory
    # Messages uploaded to Zep are automatically embedded and made available
    # for vector-based similarity search.
    search_payload = SearchPayload({}, "Who is Yuri Gagarin?")
    search_results = await client.asearch_memory(session_id, search_payload)
    for search_result in search_results:
        # Access the 'content' field within the 'message' object.
        message_content = search_result.message
        print(message_content)
```

## Zep Python

Zep Python has both an async and sync API. We've provided code examples for the async API, but theyre easily enough modified for sync usage.

**Class Attributes**

- `base_url` (str): The base URL of the API.
- `client` (httpx.AsyncClient): The HTTP client used for making API requests.

## Methods

- `get_memory(session_id: str, lastn: Optional[int] = None) -> List[Memory]`: Retrieve memory for the specified session.
- `add_memory(session_id: str, memory_messages: Memory) -> str`: Add memory to the specified session.
- `delete_memory(session_id: str) -> str`: Delete memory for the specified session.
- `search_memory(session_id: str, search_payload: SearchPayload, limit: Optional[int] = None) -> List[SearchResult]`: Search memory for the specified session.
- `close() -> None`: Close the HTTP client.

### Init
- `__init__(self, base_url: str) -> None` : Initialize the ZepClient with the specified base URL.

**Parameters**
- `base_url` (str): The base URL of the API.

```python
base_url = "http://localhost:8000"  # TODO: Replace with your Zep API URL
async with ZepClient(base_url) as client:
    # ...
```

---

### get_memory
- `get_memory(self, session_id: str, lastn: Optional[int] = None) -> List[Memory]`  
Retrieve memory for the specified session. This method is a synchronous wrapper for the asynchronous method `aget_memory`.

**Parameters**

- `session_id` (str): The ID of the session for which to retrieve memory.
- `lastn` (Optional[int], optional): The number of most recent memory entries to retrieve. Defaults to None (all entries).

**Returns**

- List[Memory]: A list of Memory objects representing the retrieved memory entries.

**Raises**

- `APIError`: If the API response format is unexpected.
- `NotFoundError`: If no results were found.

---

### aget_memory  
- `aget_memory(self, session_id: str, lastn: Optional[int] = None) -> List[Memory]`  
Asynchronously retrieve memory for the specified session.

**Parameters**

- `session_id` (str): The ID of the session for which to retrieve memory.
- `lastn` (Optional[int], optional): The number of most recent memory entries to retrieve. Defaults to None (all entries).

**Returns**

- `List[Memory]`: A list of Memory objects representing the retrieved memory entries.

**Raises**

- `APIError`: If the API response format is unexpected.
- `NotFoundError`: If no results were found.

```python
memories = await client.aget_memory("3a3a3a")
for memory in memories:
    for message in memory.messages:
        print(message.to_dict())
```

---

### search_memory  
- `search_memory(self, session_id: str, search_payload: SearchPayload, limit: Optional[int] = None) -> List[SearchResult]`  
Search memory for the specified session. This method is a synchronous wrapper for the asynchronous method `asearch_memory`.

**Parameters**

- `session_id` (str): The ID of the session for which memory should be searched.
- `search_payload` (SearchPayload): A SearchPayload object representing the search query.
- `limit` (Optional[int], optional): The maximum number of search results to return. Defaults to None (no limit).

**Returns**

- `List[SearchResult]`: A list of SearchResult objects representing the search results.

**Raises**

- `APIError`: If the API response format is unexpected.

---

### asearch_memory  
- `asearch_memory(self, session_id: str, search_payload: SearchPayload, limit: Optional[int] = None) -> List[SearchResult]`  

Asynchronously search memory for the specified session.

**Parameters**

- `session_id` (str): The ID of the session for which memory should be searched.
- `search_payload` (SearchPayload): A SearchPayload object representing the search query.
- `limit` (Optional[int], optional): The maximum number of search results to return. Defaults to None (no limit).

**Returns**

- `List[SearchResult]`: A list of SearchResult objects representing the search results.

**Raises**

- `APIError`: If the API response format is unexpected.

```python
search_payload = SearchPayload({}, "What food is served in Iceland?")
search_results = await client.asearch_memory(session_id, search_payload)
for search_result in search_results:
    # Access the 'content' field within the 'message' object.
    message_content = search_result.message
    print(message_content)
```

---

### add_memory  
- `add_memory(self, session_id: str, memory_messages: Memory) -> str`  

Add memory to the specified session. This method is a synchronous wrapper for the asynchronous method `aadd_memory`.

**Parameters**

- `session_id` (str): The ID of the session to which memory should be added.
- `memory_messages` (Memory): A Memory object representing the memory messages to be added.

**Returns**

- str: The response text from the API.

**Raises**

- `APIError`: If the API response format is unexpected.

---

### aadd_memory  
- `aadd_memory(self, session_id: str, memory_messages: Memory) -> str`  

Asynchronously add memory to the specified session.

**Parameters**

- `session_id` (str): The ID of the session to which memory should be added.
- `memory_messages` (Memory): A Memory object representing the memory messages to be added.

**Returns**

- str: The response text from the API.

**Raises**

- `APIError`: If the API response format is unexpected.

```python
message = Message(role="user", content="who was the first man to go to space?")

memory = Memory()
memory.messages = [message]

result = await client.aadd_memory(session_id, memory)
```

---

### delete_memory  
- `delete_memory(self, session_id: str) -> str`  

Delete memory for the specified session. This method is a synchronous wrapper for the asynchronous method `adelete_memory`.

**Parameters**

- `session_id` (str): The ID of the session for which memory should be deleted.

**Returns**

- str: The response text from the API.

**Raises**

- `APIError`: If the API response format is unexpected.

---

### adelete_memory  
- `adelete_memory(self, session_id: str) -> str`  

Asynchronously delete memory for the specified session.

**Parameters**

- `session_id` (str): The ID of the session for which memory should be deleted

```python
result = await client.adelete_memory(session_id)
```

---

### close  
- `close(self) -> None`  

Asynchronously close the HTTP client. This is Optional. 

**Note**: This method may be called when the ZepClient is no longer needed to release resources.

## Models

### Memory

Represents a memory object with messages, metadata, and other attributes.

**Attributes**:

- `messages` (Optional[List[Dict[str, Any]] | Memory]): A list of message objects, where each message contains a role and content.
- `metadata` (Optional[Dict[str, Any]]): A dictionary containing metadata associated with the memory.
- `summary` (Optional[Dict[str, Any]]): A dictionary containing a summary of the memory.
- `uuid` (Optional[str]): A unique identifier for the memory.
- `created_at` (Optional[str]): The timestamp when the memory was created.
- `token_count` (Optional[int]): The token count of the memory.

---

### Message

Represents a message in a conversation.

**Attributes**:

- `uuid` (Optional[str]): The unique identifier of the message.
- `created_at` (Optional[str]): The timestamp of when the message was created.
- `role` (str): The role of the sender of the message (e.g., "user", "assistant").
- `content` (str): The content of the message.
- `token_count` (Optional[int]): The number of tokens in the message.

**Methods**:

- `to_dict() -> Dict[str, Any]`: Returns a dictionary representation of the message.

---

### Summary

Represents a summary of a conversation.

**Attributes**:

- `uuid` (str): The unique identifier of the summary.
- `created_at` (str): The timestamp of when the summary was created.
- `content` (str): The content of the summary.
- `recent_message_uuid` (str): The unique identifier of the most recent message in the conversation.
- `token_count` (int): The number of tokens in the summary.

**Methods**:

- `to_dict() -> Dict[str, Any]`: Returns a dictionary representation of the summary.

---

### SearchPayload

Represents a search payload for querying memory.

**Attributes**:

- `meta` (Dict[str, Any]): Metadata associated with the search query.
- `text` (str): The text of the search query.

---

### SearchResult

Represents a search result from querying memory.

**Attributes**:

- `message` (Optional[Dict[str, Any]]): The message associated with the search result.
- `meta` (Optional[Dict[str, Any]]): Metadata associated with the search result.
- `score` (Optional[float]): The score of the search result.
- `summary` (Optional[str]): The summary of the search result.
- `dist` (Optional[float]): The distance metric of the search result.

---
## Exceptions

### APIError

Represents an API error.

**Attributes**:

- `code` (int): The error code associated with the API error.
- `message` (str): The error message associated with the API error.
---

### ZepClientError

Base exception class for ZepClient errors.

**Attributes**:

- `message`: str - The error message associated with the ZepClient error.
- `response_data`: Optional[dict] - The response data associated with the ZepClient error.
---

### NotFoundError

Raised when the API response contains no results.

Inherits from ZepClientError.

**Attributes**:

- `message`: str - The error message to be set for the exception.

---
