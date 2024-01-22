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
    SearchScope,
    Session,
)
from zep_python.message.models import Message
from zep_python.utils import SearchType
from zep_python.zep_client import ZepClient

_ = mock_healthcheck, undo_mock_healthcheck

mock_auth = {"api_url": API_BASE_URL, "api_key": "z_12345"}

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

    async with ZepClient(**mock_auth) as client:
        httpx_mock.add_response(status_code=200, json=mock_messages)
        memory = await client.memory.aget_memory(session_id)

        validate_memory(memory)


@pytest.mark.asyncio
async def test_aget_memory_missing_session(httpx_mock: HTTPXMock):
    async with ZepClient(**mock_auth) as client:
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
    async with ZepClient(**mock_auth) as client:
        memory = await client.memory.aget_memory(session_id)

    # there should be two messages
    assert len(memory.messages) == 2


def test_get_memory(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    httpx_mock.add_response(status_code=200, json=mock_messages)

    with ZepClient(**mock_auth) as client:
        memory = client.memory.get_memory(session_id)

        validate_memory(memory)


@pytest.mark.asyncio
async def test_aget_memory_not_found(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    empty_mock_response = {}

    httpx_mock.add_response(status_code=404, json=empty_mock_response)

    async with ZepClient(**mock_auth) as client:
        with pytest.raises(NotFoundError):
            _ = await client.memory.aget_memory(session_id)


@pytest.mark.asyncio
async def test_aadd_memory(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    httpx_mock.add_response(status_code=200, text="OK")

    async with ZepClient(**mock_auth) as client:
        response = await client.memory.aadd_memory(session_id, mock_memory)
        assert response == "OK"


def test_add_memory(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    httpx_mock.add_response(status_code=200, text="OK")

    with ZepClient(**mock_auth) as client:
        response = client.memory.add_memory(session_id, mock_memory)
        assert response == "OK"


@pytest.mark.asyncio
async def test_adelete_memory(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    httpx_mock.add_response(status_code=200, text="Memory deleted")

    async with ZepClient(**mock_auth) as client:
        response = await client.memory.adelete_memory(session_id)

        assert response == "Memory deleted"


@pytest.mark.asyncio
async def test_adelete_memory_session_unknown(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    httpx_mock.add_response(status_code=404)

    async with ZepClient(**mock_auth) as client:
        with pytest.raises(NotFoundError):
            _ = await client.memory.adelete_memory(session_id)


@pytest.mark.asyncio
async def test_asearch_memory(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    search_payload = MemorySearchPayload(
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

    async with ZepClient(**mock_auth) as client:
        search_results = await client.memory.asearch_memory(session_id, search_payload)

        assert len(search_results) == 1
        assert search_results[0].message.uuid == "msg-uuid"
        assert search_results[0].message.role == "user"
        assert search_results[0].message.content == "Test message"
        assert search_results[0].dist == 0.9


@pytest.mark.asyncio
async def test_asearch_memory_mmr(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    search_payload = MemorySearchPayload(
        text="Test query",
        metadata={"where": {"jsonpath": '$.system.entities[*] ? (@.Label == "DATE")'}},
        search_type=SearchType.mmr,
        mmr_lambda=0.5,
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

    async with ZepClient(**mock_auth) as client:
        search_results = await client.memory.asearch_memory(session_id, search_payload)

        assert len(search_results) == 1
        assert search_results[0].message.uuid == "msg-uuid"
        assert search_results[0].message.role == "user"
        assert search_results[0].message.content == "Test message"
        assert search_results[0].dist == 0.9


@pytest.mark.asyncio
async def test_asearch_memory_invalid_search_type(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    search_payload = MemorySearchPayload(
        text="Test query",
        search_type="invalid",
    )

    with ZepClient(**mock_auth) as client:
        with pytest.raises(ValueError):
            _ = await client.memory.asearch_memory(session_id, search_payload)


@pytest.mark.asyncio
async def test_asearch_memory_scope_summary(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    search_payload = MemorySearchPayload(
        text="Test query",
        metadata={"where": {"jsonpath": '$.system.entities[*] ? (@.Label == "DATE")'}},
        search_scope=SearchScope.summary,
        mmr_lambda=0.5,
    )
    mock_response = [
        {
            "summary": {
                "uuid": "msg-uuid",
                "content": "Test summary",
            },
            "dist": 0.9,
        }
    ]

    httpx_mock.add_response(status_code=200, json=mock_response)

    async with ZepClient(**mock_auth) as client:
        search_results = await client.memory.asearch_memory(session_id, search_payload)

        assert len(search_results) == 1
        assert search_results[0].summary.uuid == "msg-uuid"
        assert search_results[0].summary.content == "Test summary"
        assert search_results[0].dist == 0.9


# get session messages


@pytest.mark.asyncio
async def test_aget_session_messages(httpx_mock: HTTPXMock):
    session_id = str(uuid4())
    httpx_mock.add_response(status_code=200, json=mock_messages)

    async with ZepClient(**mock_auth) as client:
        session_messages = await client.message.aget_session_messages(session_id)
        assert len(session_messages) == len(mock_messages["messages"])

        for i in range(len(session_messages)):
            assert session_messages[i].uuid == mock_messages["messages"][i]["uuid"]
            assert session_messages[i].role == mock_messages["messages"][i]["role"]
            assert (
                session_messages[i].content == mock_messages["messages"][i]["content"]
            )
            assert (
                session_messages[i].metadata == mock_messages["messages"][i]["metadata"]
            )
        assert [
            filter_unset_fields(message.dict()) for message in session_messages
        ] == mock_messages["messages"]


@pytest.mark.asyncio
async def test_aget_session_messages_missing_session(httpx_mock: HTTPXMock):
    async with ZepClient(**mock_auth) as client:
        with pytest.raises(ValueError):
            _ = await client.message.aget_session_messages(session_id=None)


@pytest.mark.asyncio
async def test_aget_session_messages_not_found(httpx_mock: HTTPXMock):
    session_id = str(uuid4())
    empty_mock_response = {}
    httpx_mock.add_response(status_code=404, json=empty_mock_response)

    async with ZepClient(**mock_auth) as client:
        with pytest.raises(NotFoundError):
            _ = await client.message.aget_session_messages(session_id)


@pytest.mark.asyncio
async def test_aget_session_messages_throws_500(httpx_mock: HTTPXMock):
    session_id = str(uuid4())
    httpx_mock.add_response(status_code=500)

    async with ZepClient(**mock_auth) as client:
        with pytest.raises(Exception):
            _ = await client.message.aget_session_messages(session_id)


def test_get_session_messages(httpx_mock: HTTPXMock):
    session_id = str(uuid4())
    httpx_mock.add_response(status_code=200, json=mock_messages)

    with ZepClient(**mock_auth) as client:
        session_messages = client.message.get_session_messages(session_id)
        assert len(session_messages) == len(mock_messages["messages"])

        for i in range(len(session_messages)):
            assert session_messages[i].uuid == mock_messages["messages"][i]["uuid"]
            assert session_messages[i].role == mock_messages["messages"][i]["role"]
            assert (
                session_messages[i].content == mock_messages["messages"][i]["content"]
            )
            assert (
                session_messages[i].metadata == mock_messages["messages"][i]["metadata"]
            )
        assert [
            filter_unset_fields(message.dict()) for message in session_messages
        ] == mock_messages["messages"]


def test_get_session_messages_missing_session(httpx_mock: HTTPXMock):
    with ZepClient(**mock_auth) as client:
        with pytest.raises(ValueError):
            _ = client.message.get_session_messages(session_id=None)


def test_get_session_messages_not_found(httpx_mock: HTTPXMock):
    session_id = str(uuid4())
    empty_mock_response = {}
    httpx_mock.add_response(status_code=404, json=empty_mock_response)

    with ZepClient(**mock_auth) as client:
        with pytest.raises(NotFoundError):
            _ = client.message.get_session_messages(session_id)


def test_get_session_messages_throws_500(httpx_mock: HTTPXMock):
    session_id = str(uuid4())
    httpx_mock.add_response(status_code=500)

    with ZepClient(**mock_auth) as client:
        with pytest.raises(Exception):
            _ = client.message.get_session_messages(session_id)


# get session message


@pytest.mark.asyncio
async def test_aget_session_message(httpx_mock: HTTPXMock):
    session_id = str(uuid4())
    message_id = str(uuid4())
    mock_message = {
        "uuid": message_id,
        "role": "user",
        "content": "Test message",
        "metadata": {"key": "value"},
    }
    httpx_mock.add_response(status_code=200, json=mock_message)

    async with ZepClient(**mock_auth) as client:
        session_message = await client.message.aget_session_message(
            session_id, message_id
        )
        assert session_message.uuid == mock_message["uuid"]
        assert session_message.role == mock_message["role"]
        assert session_message.content == mock_message["content"]
        assert session_message.metadata == mock_message["metadata"]
        assert filter_unset_fields(session_message.dict()) == mock_message


@pytest.mark.asyncio
async def test_aget_session_message_missing_session(httpx_mock: HTTPXMock):
    async with ZepClient(**mock_auth) as client:
        with pytest.raises(ValueError):
            _ = await client.message.aget_session_message(
                session_id=None, message_id=str(uuid4())
            )


@pytest.mark.asyncio
async def test_aget_session_message_missing_message(httpx_mock: HTTPXMock):
    async with ZepClient(**mock_auth) as client:
        with pytest.raises(ValueError):
            _ = await client.message.aget_session_message(
                session_id=str(uuid4()), message_id=None
            )


@pytest.mark.asyncio
async def test_aget_session_message_throws_500(httpx_mock: HTTPXMock):
    session_id = str(uuid4())
    message_id = str(uuid4())
    httpx_mock.add_response(status_code=500)

    async with ZepClient(**mock_auth) as client:
        with pytest.raises(Exception):
            _ = await client.message.aget_session_message(session_id, message_id)


def test_get_session_message(httpx_mock: HTTPXMock):
    session_id = str(uuid4())
    message_id = str(uuid4())
    mock_message = {
        "uuid": message_id,
        "role": "user",
        "content": "Test message",
        "metadata": {"key": "value"},
    }
    httpx_mock.add_response(status_code=200, json=mock_message)

    with ZepClient(**mock_auth) as client:
        session_message = client.message.get_session_message(session_id, message_id)
        assert session_message.uuid == mock_message["uuid"]
        assert session_message.role == mock_message["role"]
        assert session_message.content == mock_message["content"]
        assert session_message.metadata == mock_message["metadata"]
        assert filter_unset_fields(session_message.dict()) == mock_message


def test_get_session_message_missing_session(httpx_mock: HTTPXMock):
    with ZepClient(**mock_auth) as client:
        with pytest.raises(ValueError):
            _ = client.message.get_session_message(
                session_id=None, message_id=str(uuid4())
            )


def test_get_session_message_missing_message(httpx_mock: HTTPXMock):
    with ZepClient(**mock_auth) as client:
        with pytest.raises(ValueError):
            _ = client.message.get_session_message(
                session_id=str(uuid4()), message_id=None
            )


def test_get_session_message_throws_500(httpx_mock: HTTPXMock):
    session_id = str(uuid4())
    message_id = str(uuid4())
    httpx_mock.add_response(status_code=500)

    with ZepClient(**mock_auth) as client:
        with pytest.raises(Exception):
            _ = client.message.get_session_message(session_id, message_id)


# update message metadata
@pytest.mark.asyncio
async def test_aupdate_message_metadata(httpx_mock: HTTPXMock):
    session_id = str(uuid4())
    message_id = str(uuid4())
    mock_message = {
        "uuid": message_id,
        "role": "user",
        "content": "Test message",
        "metadata": {"metadata": {"foo": "bar"}},
    }
    httpx_mock.add_response(status_code=200, json=mock_message)

    async with ZepClient(**mock_auth) as client:
        updated_message = await client.message.aupdate_message_metadata(
            session_id, message_id, {"metadata": {"foo": "bar"}}
        )
        assert updated_message.uuid == mock_message["uuid"]
        assert updated_message.role == mock_message["role"]
        assert updated_message.content == mock_message["content"]
        assert updated_message.metadata == mock_message["metadata"]
        assert filter_unset_fields(updated_message.dict()) == mock_message


@pytest.mark.asyncio
async def test_aupdate_message_metadata_missing_session(httpx_mock: HTTPXMock):
    async with ZepClient(**mock_auth) as client:
        with pytest.raises(ValueError):
            _ = await client.message.aupdate_message_metadata(
                session_id=None,
                message_id=str(uuid4()),
                metadata={"metadata": {"foo": "bar"}},
            )


@pytest.mark.asyncio
async def test_aupdate_message_metadata_missing_message(httpx_mock: HTTPXMock):
    async with ZepClient(**mock_auth) as client:
        with pytest.raises(ValueError):
            _ = await client.message.aupdate_message_metadata(
                session_id=str(uuid4()),
                message_id=None,
                metadata={"metadata": {"foo": "bar"}},
            )


@pytest.mark.asyncio
async def test_aupdate_message_metadata_throws_500(httpx_mock: HTTPXMock):
    session_id = str(uuid4())
    message_id = str(uuid4())
    httpx_mock.add_response(status_code=500)

    async with ZepClient(**mock_auth) as client:
        with pytest.raises(Exception):
            _ = await client.message.aupdate_message_metadata(
                session_id, message_id, {"metadata": {"foo": "bar"}}
            )


def test_update_message_metadata(httpx_mock: HTTPXMock):
    session_id = str(uuid4())
    message_id = str(uuid4())
    mock_message = {
        "uuid": message_id,
        "role": "user",
        "content": "Test message",
        "metadata": {"metadata": {"foo": "bar"}},
    }
    httpx_mock.add_response(status_code=200, json=mock_message)

    with ZepClient(**mock_auth) as client:
        updated_message = client.message.update_message_metadata(
            session_id, message_id, {"metadata": {"foo": "bar"}}
        )
        assert updated_message.uuid == mock_message["uuid"]
        assert updated_message.role == mock_message["role"]
        assert updated_message.content == mock_message["content"]
        assert updated_message.metadata == mock_message["metadata"]
        assert filter_unset_fields(updated_message.dict()) == mock_message


def test_update_message_metadata_missing_session(httpx_mock: HTTPXMock):
    with ZepClient(**mock_auth) as client:
        with pytest.raises(ValueError):
            _ = client.message.update_message_metadata(
                session_id=None,
                message_id=str(uuid4()),
                metadata={"metadata": {"foo": "bar"}},
            )


def test_update_message_metadata_missing_message(httpx_mock: HTTPXMock):
    with ZepClient(**mock_auth) as client:
        with pytest.raises(ValueError):
            _ = client.message.update_message_metadata(
                session_id=str(uuid4()),
                message_id=None,
                metadata={"metadata": {"foo": "bar"}},
            )


def test_update_message_metadata_throws_500(httpx_mock: HTTPXMock):
    session_id = str(uuid4())
    message_id = str(uuid4())
    httpx_mock.add_response(status_code=500)

    with ZepClient(**mock_auth) as client:
        with pytest.raises(Exception):
            _ = client.message.update_message_metadata(
                session_id, message_id, {"metadata": {"foo": "bar"}}
            )


@pytest.mark.asyncio
async def test_asearch_memory_invalid_search_scope(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    search_payload = MemorySearchPayload(
        text="Test query",
        search_scope="invalid",
    )

    with ZepClient(**mock_auth) as client:
        with pytest.raises(ValueError):
            _ = await client.memory.asearch_memory(session_id, search_payload)


@pytest.mark.asyncio
async def test_asearch_memory_no_payload(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    async with ZepClient(**mock_auth) as client:
        with pytest.raises(ValueError):
            _ = await client.memory.asearch_memory(session_id, None)  # type: ignore


def test_search_memory(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    search_payload = MemorySearchPayload(
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

    with ZepClient(**mock_auth) as client:
        search_results = client.memory.search_memory(session_id, search_payload)

        assert len(search_results) == 1
        assert search_results[0].message.uuid == "msg-uuid"
        assert search_results[0].message.role == "user"
        assert search_results[0].message.content == "Test message"
        assert search_results[0].dist == 0.9


def test_search_memory_mmr(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    search_payload = MemorySearchPayload(
        text="Test query",
        metadata={"where": {"jsonpath": '$.system.entities[*] ? (@.Label == "DATE")'}},
        search_type=SearchType.mmr,
        mmr_lambda=0.5,
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

    with ZepClient(**mock_auth) as client:
        search_results = client.memory.search_memory(session_id, search_payload)

        assert len(search_results) == 1
        assert search_results[0].message.uuid == "msg-uuid"
        assert search_results[0].message.role == "user"
        assert search_results[0].message.content == "Test message"
        assert search_results[0].dist == 0.9


def test_search_memory_invalid_search_type(httpx_mock: HTTPXMock):
    session_id = str(uuid4())

    search_payload = MemorySearchPayload(
        text="Test query",
        search_type="invalid",
    )

    with ZepClient(**mock_auth) as client:
        with pytest.raises(ValueError):
            _ = client.memory.search_memory(session_id, search_payload)


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
    assert Session.model_validate(mock_session) == session


@pytest.mark.asyncio
async def test_get_session(httpx_mock: HTTPXMock):
    session_id = "abc123"

    httpx_mock.add_response(status_code=200, json=mock_session)

    client = ZepClient(**mock_auth)
    session = client.memory.get_session(session_id)

    validate_session(session)


def test_get_session_missing_id():
    client = ZepClient(**mock_auth)

    with pytest.raises(ValueError):
        client.memory.get_session(session_id=None)  # type: ignore


@pytest.mark.asyncio
async def test_aget_session(httpx_mock: HTTPXMock):
    session_id = "abc123"

    httpx_mock.add_response(status_code=200, json=mock_session)

    async with ZepClient(**mock_auth) as client:
        session = await client.memory.aget_session(session_id)

        validate_session(session)


@pytest.mark.asyncio
async def test_aget_session_missing_id(httpx_mock: HTTPXMock):
    async with ZepClient(**mock_auth) as client:
        with pytest.raises(ValueError):
            _ = await client.memory.aget_session(session_id=None)  # type: ignore


def test_add_session(httpx_mock: HTTPXMock):
    session = Session(**mock_session)

    httpx_mock.add_response(status_code=200, json=mock_session)

    client = ZepClient(**mock_auth)
    result = client.memory.add_session(session)

    assert result == session


def test_add_session_missing_session():
    client = ZepClient(**mock_auth)

    with pytest.raises(ValueError):
        client.memory.add_session(session=None)  # type: ignore


@pytest.mark.asyncio
async def test_aadd_session(httpx_mock: HTTPXMock):
    session = Session(**mock_session)

    httpx_mock.add_response(status_code=200, json=mock_session)

    async with ZepClient(**mock_auth) as client:
        result = await client.memory.aadd_session(session)

        assert result == session


@pytest.mark.asyncio
async def test_aadd_session_missing_session(httpx_mock: HTTPXMock):
    async with ZepClient(**mock_auth) as client:
        with pytest.raises(ValueError):
            _ = await client.memory.aadd_session(session=None)  # type: ignore


def test_update_session(httpx_mock: HTTPXMock):
    session = Session(**mock_session)

    httpx_mock.add_response(status_code=200, json=mock_session)

    client = ZepClient(**mock_auth)
    result = client.memory.update_session(session)

    assert result == session


def test_update_session_missing_id(httpx_mock: HTTPXMock):
    session = Session(**mock_session)

    session.session_id = None

    client = ZepClient(**mock_auth)

    with pytest.raises(ValueError):
        client.memory.update_session(session=session)  # type: ignore


def test_update_session_missing_session(httpx_mock: HTTPXMock):
    client = ZepClient(**mock_auth)

    with pytest.raises(ValueError):
        client.memory.update_session(session=None)  # type: ignore


def test_update_session_not_found(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=404)

    session = Session(**mock_session)

    client = ZepClient(**mock_auth)

    with pytest.raises(NotFoundError):
        client.memory.update_session(session)  # type: ignore


@pytest.mark.asyncio
async def test_aupdate_session(httpx_mock: HTTPXMock):
    session = Session(**mock_session)

    httpx_mock.add_response(status_code=200, json=mock_session)

    async with ZepClient(**mock_auth) as client:
        result = await client.memory.aupdate_session(session)

        assert result == session


@pytest.mark.asyncio
async def test_aupdate_session_missing_id(httpx_mock: HTTPXMock):
    session = Session(**mock_session)

    session.session_id = None

    async with ZepClient(**mock_auth) as client:
        with pytest.raises(ValueError):
            _ = await client.memory.aupdate_session(session=session)  # type: ignore


@pytest.mark.asyncio
async def test_aupdate_session_missing_session(httpx_mock: HTTPXMock):
    async with ZepClient(**mock_auth) as client:
        with pytest.raises(ValueError):
            _ = await client.memory.aupdate_session(session=None)  # type: ignore


@pytest.mark.asyncio
async def test_aupdate_session_not_found(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=404)

    session = Session(**mock_session)

    client = ZepClient(**mock_auth)

    with pytest.raises(NotFoundError):
        await client.memory.aupdate_session(session)  # type: ignore


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
    assert [Session.model_validate(session) for session in mock_sessions] == sessions


@pytest.mark.asyncio
async def test_list_sessions(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json=mock_sessions)

    client = ZepClient(**mock_auth)
    sessions = client.memory.list_sessions()

    validate_sessions(sessions)


@pytest.mark.asyncio
async def test_alist_sessions(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json=mock_sessions)

    async with ZepClient(**mock_auth) as client:
        sessions = await client.memory.alist_sessions()

        validate_sessions(sessions)


def test_list_all_sessions(httpx_mock: HTTPXMock):
    with ZepClient(**mock_auth) as client:
        httpx_mock.add_response(status_code=200, json=[mock_sessions[0]])
        sessions_generator = client.memory.list_all_sessions(1)
        for i, session in enumerate(sessions_generator):
            assert session == [Session.model_validate(mock_sessions[i])]
            if i == 0:
                httpx_mock.add_response(status_code=200, json=[mock_sessions[i + 1]])
            else:
                httpx_mock.add_response(status_code=200, json=[])
                with pytest.raises(StopIteration):
                    _ = next(sessions_generator)


@pytest.mark.asyncio
async def test_alist_all_sessions(httpx_mock: HTTPXMock):
    async with ZepClient(**mock_auth) as client:
        httpx_mock.add_response(status_code=200, json=[mock_sessions[0]])
        sessions_generator = client.memory.alist_all_sessions(1)
        i = 0
        try:
            async for session in sessions_generator:
                assert session == [Session.model_validate(mock_sessions[i])]
                if i == 0:
                    httpx_mock.add_response(
                        status_code=200, json=[mock_sessions[i + 1]]
                    )
                else:
                    httpx_mock.add_response(status_code=200, json=[])
                i += 1
        except StopAsyncIteration:
            pass
