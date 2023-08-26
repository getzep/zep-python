# mypy: ignore-errors
from typing import Dict, List
from uuid import uuid4

import pytest
from pytest_httpx import HTTPXMock

from tests.conftest import API_BASE_URL, mock_healthcheck, undo_mock_healthcheck
from zep_python import NotFoundError
from zep_python.memory.models import (
    Memory,
    MemorySearchPayload,
    Message,
    Session,
)
from zep_python.zep_client import ZepClient

_ = mock_healthcheck, undo_mock_healthcheck

mock_messages = {
    "messages": [
        {
            "uuid": "msg-uuid",
            "role": "user",
            "content": "Test message",
            "metadata": {"key": "value"},
        },
        {
            "uuid": "msg-uuid2",
            "role": "ai",
            "content": "Test message2",
            "metadata": {"key2": "value2"},
        },
    ],
}

mock_memory = Memory(
    messages=[
        Message(role="user", content="Test message", metadata={"key": "value"}),
        Message(role="ai", content="Test message2"),
    ]
)


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


def validate_memory(memory: Memory):
    assert len(memory.messages) == len(mock_messages["messages"])

    for i in range(len(memory.messages)):
        assert memory.messages[i].uuid == mock_messages["messages"][i]["uuid"]
        assert memory.messages[i].role == mock_messages["messages"][i]["role"]
        assert memory.messages[i].content == mock_messages["messages"][i]["content"]
        assert memory.messages[i].metadata == mock_messages["messages"][i]["metadata"]

    assert filter_unset_fields(memory.dict()) == mock_messages


@pytest.mark.asyncio
async def test_aget_memory(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    async with ZepClient(base_url=API_BASE_URL) as client:
        httpx_mock.add_response(status_code=200, json=mock_messages)
        memory = await client.memory.aget_memory(session_id)

        validate_memory(memory)


@pytest.mark.asyncio
async def test_aget_memory_missing_session(httpx_mock: HTTPXMock):
    async with ZepClient(base_url=API_BASE_URL) as client:
        with pytest.raises(ValueError):
            _ = await client.memory.aget_memory(session_id=None)  # type: ignore


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
    async with ZepClient(base_url=API_BASE_URL) as client:
        memory = await client.memory.aget_memory(session_id)

    # there should be two messages
    assert len(memory.messages) == 2


def test_get_memory(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    httpx_mock.add_response(status_code=200, json=mock_messages)

    with ZepClient(base_url=API_BASE_URL) as client:
        memory = client.memory.get_memory(session_id)

        validate_memory(memory)


@pytest.mark.asyncio
async def test_aget_memory_not_found(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    empty_mock_response = {}

    httpx_mock.add_response(status_code=404, json=empty_mock_response)

    async with ZepClient(base_url=API_BASE_URL) as client:
        with pytest.raises(NotFoundError):
            _ = await client.memory.aget_memory(session_id)


@pytest.mark.asyncio
async def test_aadd_memory(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    httpx_mock.add_response(status_code=200, text="OK")

    async with ZepClient(base_url=API_BASE_URL) as client:
        response = await client.memory.aadd_memory(session_id, mock_memory)
        assert response == "OK"


def test_add_memory(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    httpx_mock.add_response(status_code=200, text="OK")

    with ZepClient(base_url=API_BASE_URL) as client:
        response = client.memory.add_memory(session_id, mock_memory)
        assert response == "OK"


@pytest.mark.asyncio
async def test_adelete_memory(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    httpx_mock.add_response(status_code=200, text="Memory deleted")

    async with ZepClient(base_url=API_BASE_URL) as client:
        response = await client.memory.adelete_memory(session_id)

        assert response == "Memory deleted"


@pytest.mark.asyncio
async def test_adelete_memory_session_unknown(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    httpx_mock.add_response(status_code=404)

    async with ZepClient(base_url=API_BASE_URL) as client:
        with pytest.raises(NotFoundError):
            _ = await client.memory.adelete_memory(session_id)


@pytest.mark.asyncio
async def test_asearch_memory(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    search_payload = MemorySearchPayload(
        meta={},
        text="Test query",
        metadata={"where": {"jsonpath": '$.system.entities[*] ? (@.Label == "DATE")'}},
    )
    mock_response = [
        {
            "message": {
                "uuid": "msg-uuid",
                "role": "user",
                "content": "Test message",
            },
            "dist": 0.9,
        }
    ]

    httpx_mock.add_response(status_code=200, json=mock_response)

    async with ZepClient(base_url=API_BASE_URL) as client:
        search_results = await client.memory.asearch_memory(session_id, search_payload)

        assert len(search_results) == 1
        assert search_results[0].message["uuid"] == "msg-uuid"
        assert search_results[0].message["role"] == "user"
        assert search_results[0].message["content"] == "Test message"
        assert search_results[0].dist == 0.9


@pytest.mark.asyncio
async def test_asearch_memory_no_payload(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    async with ZepClient(base_url=API_BASE_URL) as client:
        with pytest.raises(ValueError):
            _ = await client.memory.asearch_memory(session_id, None)  # type: ignore


def test_search_memory(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    search_payload = MemorySearchPayload(
        meta={},
        text="Test query",
        metadata={"where": {"jsonpath": '$.system.entities[*] ? (@.Label == "DATE")'}},
    )
    mock_response = [
        {
            "message": {
                "uuid": "msg-uuid",
                "role": "user",
                "content": "Test message",
            },
            "dist": 0.9,
        }
    ]

    httpx_mock.add_response(status_code=200, json=mock_response)

    with ZepClient(base_url=API_BASE_URL) as client:
        search_results = client.memory.search_memory(session_id, search_payload)

        assert len(search_results) == 1
        assert search_results[0].message["uuid"] == "msg-uuid"
        assert search_results[0].message["role"] == "user"
        assert search_results[0].message["content"] == "Test message"
        assert search_results[0].dist == 0.9


# Predefined session response
mock_session = {
    "uuid": str(uuid4()),
    "id": 1,
    "created_at": "2020-12-31T23:59:59",
    "updated_at": "2021-01-01T00:00:00",
    "deleted_at": None,
    "session_id": "abc123",
    "metadata": {},
    "user_id": "user123",
}


def validate_session(session):
    # Validate the session object here
    assert Session.parse_obj(mock_session) == session


@pytest.mark.asyncio
async def test_get_session(httpx_mock: HTTPXMock):
    session_id = "abc123"

    httpx_mock.add_response(status_code=200, json=mock_session)

    client = ZepClient(base_url=API_BASE_URL)
    session = client.memory.get_session(session_id)

    validate_session(session)


def test_get_session_missing_id():
    client = ZepClient(base_url=API_BASE_URL)

    with pytest.raises(ValueError):
        client.memory.get_session(session_id=None)  # type: ignore


@pytest.mark.asyncio
async def test_aget_session(httpx_mock: HTTPXMock):
    session_id = "abc123"

    httpx_mock.add_response(status_code=200, json=mock_session)

    async with ZepClient(base_url=API_BASE_URL) as client:
        session = await client.memory.aget_session(session_id)

        validate_session(session)


@pytest.mark.asyncio
async def test_aget_session_missing_id(httpx_mock: HTTPXMock):
    async with ZepClient(base_url=API_BASE_URL) as client:
        with pytest.raises(ValueError):
            _ = await client.memory.aget_session(session_id=None)  # type: ignore


def test_add_session(httpx_mock: HTTPXMock):
    session = Session(**mock_session)

    httpx_mock.add_response(status_code=200, json=mock_session)

    client = ZepClient(base_url=API_BASE_URL)
    result = client.memory.add_session(session)

    assert result == session


def test_add_session_missing_session():
    client = ZepClient(base_url=API_BASE_URL)

    with pytest.raises(ValueError):
        client.memory.add_session(session=None)  # type: ignore


@pytest.mark.asyncio
async def test_aadd_session(httpx_mock: HTTPXMock):
    session = Session(**mock_session)

    httpx_mock.add_response(status_code=200, json=mock_session)

    async with ZepClient(base_url=API_BASE_URL) as client:
        result = await client.memory.aadd_session(session)

        assert result == session


@pytest.mark.asyncio
async def test_aadd_session_missing_session(httpx_mock: HTTPXMock):
    async with ZepClient(base_url=API_BASE_URL) as client:
        with pytest.raises(ValueError):
            _ = await client.memory.aadd_session(session=None)  # type: ignore


def test_update_session(httpx_mock: HTTPXMock):
    session = Session(**mock_session)

    httpx_mock.add_response(status_code=200, json=mock_session)

    client = ZepClient(base_url=API_BASE_URL)
    result = client.memory.update_session(session)

    assert result == session


def test_update_session_missing_id(httpx_mock: HTTPXMock):
    session = Session(**mock_session)

    session.session_id = None

    client = ZepClient(base_url=API_BASE_URL)

    with pytest.raises(ValueError):
        client.memory.update_session(session=session)  # type: ignore


def test_update_session_missing_session(httpx_mock: HTTPXMock):
    client = ZepClient(base_url=API_BASE_URL)

    with pytest.raises(ValueError):
        client.memory.update_session(session=None)  # type: ignore


def test_update_session_not_found(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=404)

    session = Session(**mock_session)

    client = ZepClient(base_url=API_BASE_URL)

    with pytest.raises(NotFoundError):
        client.memory.update_session(session)  # type: ignore


@pytest.mark.asyncio
async def test_aupdate_session(httpx_mock: HTTPXMock):
    session = Session(**mock_session)

    httpx_mock.add_response(status_code=200, json=mock_session)

    async with ZepClient(base_url=API_BASE_URL) as client:
        result = await client.memory.aupdate_session(session)

        assert result == session


@pytest.mark.asyncio
async def test_aupdate_session_missing_id(httpx_mock: HTTPXMock):
    session = Session(**mock_session)

    session.session_id = None

    async with ZepClient(base_url=API_BASE_URL) as client:
        with pytest.raises(ValueError):
            _ = await client.memory.aupdate_session(session=session)  # type: ignore


@pytest.mark.asyncio
async def test_aupdate_session_missing_session(httpx_mock: HTTPXMock):
    async with ZepClient(base_url=API_BASE_URL) as client:
        with pytest.raises(ValueError):
            _ = await client.memory.aupdate_session(session=None)  # type: ignore


@pytest.mark.asyncio
async def test_aupdate_session_not_found(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=404)

    session = Session(**mock_session)

    client = ZepClient(base_url=API_BASE_URL)

    with pytest.raises(NotFoundError):
        await client.memory.aupdate_session(session)  # type: ignore


@pytest.mark.asyncio
async def test_aget_session_warning(zep_client: ZepClient, httpx_mock: HTTPXMock):
    session = Session(**mock_session)

    httpx_mock.add_response(
        method="GET",
        status_code=200,
        json=session.dict(),
    )

    with pytest.warns(DeprecationWarning):
        response = await zep_client.aget_session(session.session_id)

    assert response == mock_session


mock_sessions = [
    {
        "uuid": str(uuid4()),
        "id": 0,
        "created_at": "2020-12-31T23:59:59",
        "updated_at": "2021-01-01T00:00:00",
        "deleted_at": None,
        "session_id": "abc123",
        "metadata": {},
        "user_id": "user123",
    },
    {
        "uuid": str(uuid4()),
        "id": 1,
        "created_at": "2021-01-01T00:00:00",
        "updated_at": "2021-01-01T00:00:01",
        "deleted_at": None,
        "session_id": "abc124",
        "metadata": {},
    },
]


def validate_sessions(sessions: List[Session]) -> None:
    # Validate the sessions list here
    assert [Session.parse_obj(session) for session in mock_sessions] == sessions


@pytest.mark.asyncio
async def test_list_sessions(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json=mock_sessions)

    client = ZepClient(base_url=API_BASE_URL)
    sessions = client.memory.list_sessions()

    validate_sessions(sessions)


@pytest.mark.asyncio
async def test_alist_sessions(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json=mock_sessions)

    async with ZepClient(base_url=API_BASE_URL) as client:
        sessions = await client.memory.alist_sessions()

        validate_sessions(sessions)


def test_list_all_sessions(httpx_mock: HTTPXMock):
    with ZepClient(base_url=API_BASE_URL) as client:
        httpx_mock.add_response(status_code=200, json=[mock_sessions[0]])
        sessions_generator = client.memory.list_all_sessions(1)
        for i, session in enumerate(sessions_generator):
            assert session == [Session.parse_obj(mock_sessions[i])]
            if i == 0:
                httpx_mock.add_response(status_code=200, json=[mock_sessions[i + 1]])
            else:
                httpx_mock.add_response(status_code=200, json=[])
                with pytest.raises(StopIteration):
                    _ = next(sessions_generator)


@pytest.mark.asyncio
async def test_alist_all_sessions(httpx_mock: HTTPXMock):
    async with ZepClient(base_url=API_BASE_URL) as client:
        httpx_mock.add_response(status_code=200, json=[mock_sessions[0]])
        sessions_generator = client.memory.alist_all_sessions(1)
        i = 0
        try:
            async for session in sessions_generator:
                assert session == [Session.parse_obj(mock_sessions[i])]
                if i == 0:
                    httpx_mock.add_response(
                        status_code=200, json=[mock_sessions[i + 1]]
                    )
                else:
                    httpx_mock.add_response(status_code=200, json=[])
                i += 1
        except StopAsyncIteration:
            pass
