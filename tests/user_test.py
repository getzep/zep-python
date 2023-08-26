# mypy: ignore-errors

from uuid import uuid4

import pytest
from pytest_httpx import HTTPXMock

from zep_python import NotFoundError
from zep_python.user.models import (
    CreateUserRequest,
    UpdateUserRequest,
    User,
)
from zep_python.zep_client import ZepClient

mock_user = {
    "user_id": "user-id",
    "name": "Test User",
    "email": "test@example.com",
    "metadata": {"key": "value"},
}


def validate_user(user: User):
    assert User.parse_obj(mock_user) == user


@pytest.mark.asyncio
async def test_aget_user(httpx_mock: HTTPXMock, zep_client: ZepClient):
    user_id = "user-id"

    httpx_mock.add_response(status_code=200, json=mock_user)

    async with zep_client:
        user = await zep_client.user.aget(user_id)

        validate_user(user)


@pytest.mark.asyncio
async def test_aget_user_missing_id(httpx_mock: HTTPXMock, zep_client: ZepClient):
    async with zep_client:
        with pytest.raises(ValueError):
            _ = await zep_client.user.aget(user_id=None)  # type: ignore


def test_get_user(httpx_mock: HTTPXMock, zep_client: ZepClient):
    user_id = "user-id"

    httpx_mock.add_response(status_code=200, json=mock_user)

    with zep_client:
        user = zep_client.user.get(user_id)

        validate_user(user)


@pytest.mark.asyncio
async def test_aget_user_not_found(httpx_mock: HTTPXMock, zep_client: ZepClient):
    user_id = "user-id"

    httpx_mock.add_response(status_code=404)

    async with zep_client:
        with pytest.raises(NotFoundError):
            _ = await zep_client.user.aget(user_id)


@pytest.mark.asyncio
async def test_aadd_user(httpx_mock: HTTPXMock, zep_client: ZepClient):
    user = CreateUserRequest(**mock_user)

    httpx_mock.add_response(status_code=200, json=mock_user)

    async with zep_client:
        response = await zep_client.user.aadd(user)

        validate_user(response)


def test_add_user(httpx_mock: HTTPXMock, zep_client: ZepClient):
    user = CreateUserRequest(**mock_user)

    httpx_mock.add_response(status_code=200, json=mock_user)

    with zep_client:
        response = zep_client.user.add(user)

        validate_user(response)


@pytest.mark.asyncio
async def test_aupdate_user(httpx_mock: HTTPXMock, zep_client: ZepClient):
    user = UpdateUserRequest(**mock_user)

    httpx_mock.add_response(status_code=200, json=mock_user)

    async with zep_client:
        response = await zep_client.user.aupdate(user)

        validate_user(response)


def test_update_user(httpx_mock: HTTPXMock, zep_client: ZepClient):
    user = UpdateUserRequest(**mock_user)

    httpx_mock.add_response(status_code=200, json=mock_user)

    with zep_client:
        response = zep_client.user.update(user)

        validate_user(response)


@pytest.mark.asyncio
async def test_adelete_user(httpx_mock: HTTPXMock, zep_client: ZepClient):
    user_id = "user-id"

    httpx_mock.add_response(status_code=200)

    async with zep_client:
        await zep_client.user.adelete(user_id)


def test_delete_user(httpx_mock: HTTPXMock, zep_client: ZepClient):
    user_id = "user-id"

    httpx_mock.add_response(status_code=200)

    with zep_client:
        zep_client.user.delete(user_id)


@pytest.mark.asyncio
async def test_alist_users(httpx_mock: HTTPXMock, zep_client: ZepClient):
    mock_users = [mock_user, mock_user]

    httpx_mock.add_response(status_code=200, json=mock_users)

    async with zep_client:
        users = await zep_client.user.alist()

        for user in users:
            validate_user(user)


def test_list_users(httpx_mock: HTTPXMock, zep_client: ZepClient):
    mock_users = [mock_user, mock_user]

    httpx_mock.add_response(status_code=200, json=mock_users)

    with zep_client:
        users = zep_client.user.list()

        for user in users:
            validate_user(user)
