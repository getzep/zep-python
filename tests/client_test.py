# mypy: ignore-errors
from typing import Dict
from uuid import uuid4

import pytest
from pytest_httpx import HTTPXMock

from zep_python import NotFoundError
from zep_python.models import Memory, Message, SearchPayload
from zep_python.zep_client import ZepClient

api_base_url = "http://localhost/api/v1"


@pytest.fixture
def assert_all_responses_were_requested() -> bool:
    return False


def filter_unset_fields(d: Dict) -> Dict:
    filtered = {}
    for key, value in d.items():
        if value is not None:
            if isinstance(value, dict):
                nested = filter_unset_fields(value)
                if nested:  # Only add non-empty dictionaries
                    filtered[key] = nested
            elif isinstance(value, list):
                filtered[key] = [
                    filter_unset_fields(item) if isinstance(item, dict) else item
                    for item in value
                ]
            else:
                filtered[key] = value
    return filtered


@pytest.mark.asyncio
async def test_aget_memory(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    mock_response = {
        "messages": [
            {"uuid": "msg-uuid", "role": "user", "content": "Test message"},
            {"uuid": "msg-uuid2", "role": "ai", "content": "Test message2"},
        ],
    }

    httpx_mock.add_response(status_code=200, json=mock_response)

    async with ZepClient(base_url=api_base_url) as client:
        memory = await client.aget_memory(session_id)

        assert len(memory.messages) == 2
        assert memory.messages[0].uuid == "msg-uuid"
        assert memory.messages[0].role == "user"
        assert memory.messages[0].content == "Test message"
        assert filter_unset_fields(memory.dict()) == mock_response


@pytest.mark.asyncio
async def test_aget_memory_missing_session(httpx_mock: HTTPXMock):
    async with ZepClient(base_url=api_base_url) as client:
        with pytest.raises(ValueError):
            _ = await client.aget_memory(session_id=None)  # type: ignore


@pytest.mark.asyncio
async def test_aget_memory_missing_values(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    mock_response = {
        "messages": [
            {"role": "user", "content": "Test message"},
            {
                "uuid": "msg-uuid2",
                "role": "ai",
            },
        ],
    }

    httpx_mock.add_response(
        status_code=200,
        json=mock_response,
    )

    # Fields are optional and so this should still parse
    async with ZepClient(base_url=api_base_url) as client:
        memory = await client.aget_memory(session_id)

    # there should be two messages
    assert len(memory.messages) == 2


def test_get_memory(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    mock_response = {
        "messages": [
            {"uuid": "msg-uuid", "role": "user", "content": "Test message"},
            {"uuid": "msg-uuid2", "role": "ai", "content": "Test message2"},
        ],
    }

    httpx_mock.add_response(status_code=200, json=mock_response)

    with ZepClient(base_url=api_base_url) as client:
        memory = client.get_memory(session_id)

        assert len(memory.messages) == 2
        assert memory.messages[0].uuid == "msg-uuid"
        assert memory.messages[0].role == "user"
        assert memory.messages[0].content == "Test message"


@pytest.mark.asyncio
async def test_aget_memory_not_found(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    mock_response = {}

    httpx_mock.add_response(status_code=404, json=mock_response)

    async with ZepClient(base_url=api_base_url) as client:
        with pytest.raises(NotFoundError):
            _ = await client.aget_memory(session_id)


@pytest.mark.asyncio
async def test_aadd_memory(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    memory_messages = Memory(
        messages=[
            Message(role="user", content="Test message"),
            Message(role="ai", content="Test message2"),
        ]
    )

    httpx_mock.add_response(status_code=200, text="OK")

    async with ZepClient(base_url=api_base_url) as client:
        response = await client.aadd_memory(session_id, memory_messages)
        assert response == "OK"


def test_add_memory(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    memory_messages = Memory(
        messages=[
            Message(role="user", content="Test message"),
            Message(role="ai", content="Test message2"),
        ]
    )

    httpx_mock.add_response(status_code=200, text="OK")

    with ZepClient(base_url=api_base_url) as client:
        response = client.add_memory(session_id, memory_messages)
        assert response == "OK"


@pytest.mark.asyncio
async def test_adelete_memory(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    httpx_mock.add_response(status_code=200, text="Memory deleted")

    async with ZepClient(base_url=api_base_url) as client:
        response = await client.adelete_memory(session_id)

        assert response == "Memory deleted"


@pytest.mark.asyncio
async def test_adelete_memory_session_unknown(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    httpx_mock.add_response(status_code=404)

    async with ZepClient(base_url=api_base_url) as client:
        with pytest.raises(NotFoundError):
            _ = await client.adelete_memory(session_id)


@pytest.mark.asyncio
async def test_asearch_memory(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    search_payload = SearchPayload(meta={}, text="Test query")
    mock_response = [
        {
            "message": {
                "uuid": "msg-uuid",
                "role": "user",
                "content": "Test message",
            },
            "score": 0.9,
        }
    ]

    httpx_mock.add_response(status_code=200, json=mock_response)

    async with ZepClient(base_url=api_base_url) as client:
        search_results = await client.asearch_memory(session_id, search_payload)

        assert len(search_results) == 1
        assert search_results[0].message["uuid"] == "msg-uuid"
        assert search_results[0].message["role"] == "user"
        assert search_results[0].message["content"] == "Test message"
        assert search_results[0].score == 0.9


@pytest.mark.asyncio
async def test_asearch_memory_no_payload(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    async with ZepClient(base_url=api_base_url) as client:
        with pytest.raises(ValueError):
            _ = await client.asearch_memory(session_id, None)  # type: ignore


def test_search_memory(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    search_payload = SearchPayload(meta={}, text="Test query")
    mock_response = [
        {
            "message": {
                "uuid": "msg-uuid",
                "role": "user",
                "content": "Test message",
            },
            "score": 0.9,
        }
    ]

    httpx_mock.add_response(status_code=200, json=mock_response)

    with ZepClient(base_url=api_base_url) as client:
        search_results = client.search_memory(session_id, search_payload)

        assert len(search_results) == 1
        assert search_results[0].message["uuid"] == "msg-uuid"
        assert search_results[0].message["role"] == "user"
        assert search_results[0].message["content"] == "Test message"
        assert search_results[0].score == 0.9
