[![Tests](https://github.com/getzep/zep-python/actions/workflows/test.yml/badge.svg)](https://github.com/getzep/zep-python/actions/workflows/test.yml) [![lint](https://github.com/getzep/zep-python/actions/workflows/lint.yml/badge.svg)](https://github.com/getzep/zep-python/actions/workflows/lint.yml) [![Release to PyPI](https://github.com/getzep/zep-python/actions/workflows/release.yml/badge.svg)](https://github.com/getzep/zep-python/actions/workflows/release.yml) ![GitHub](https://img.shields.io/github/license/getzep/zep-python?color=blue)

# Zep: A long-term memory store for conversational AI applications

This is the Python client package for the Zep service. For more information about Zep, see https://github.com/getzep/zep.

Zep documentation: [https://docs.getzep.com](https://docs.getzep.com/)

## Installation

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

from zep_python import Memory, Message, MemorySearchPayload, ZepClient

base_url = "http://localhost:8000"  # TODO: Replace with Zep API URL
session_id = "2a2a2a"  # an identifier for your user's session.

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
    memory = await client.aget_memory(session_id)
    for message in memory.messages:
        print(message.to_dict())

    # Search memory
    # Messages uploaded to Zep are automatically embedded and made available
    # for vector-based similarity search.
    search_payload = MemorySearchPayload("Who is Yuri Gagarin?")
    search_results = await client.asearch_memory(session_id, search_payload)
    for search_result in search_results:
        # Access the 'content' field within the 'message' object.
        message_content = search_result.message
        print(message_content)
```

## Server Installation and SDK Documentation

Server installation documentation and more available here: [https://getzep.github.io](https://getzep.github.io/)
