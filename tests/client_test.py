# mypy: ignore-errors

import pytest
from packaging.version import Version
from pytest_httpx import HTTPXMock

from tests.conftest import API_BASE_URL, mock_healthcheck, undo_mock_healthcheck
from zep_python import APIError
from zep_python.zep_client import ZepClient, concat_url, parse_version_string

_ = mock_healthcheck, undo_mock_healthcheck


@pytest.mark.usefixtures("undo_mock_healthcheck")
def test_client_connect_healthcheck_fail():
    with pytest.raises(APIError):
        ZepClient(base_url=API_BASE_URL, project_api_key='z_test-api-key')


@pytest.mark.usefixtures("undo_mock_healthcheck")
def test_client_connect_healthcheck_pass(httpx_mock: HTTPXMock):
    """Explicitly undo the mock healthcheck and then add a new mock response"""
    httpx_mock.add_response(status_code=200, text=".")

    ZepClient(base_url=API_BASE_URL, project_api_key='z_test-api-key')


@pytest.mark.asyncio
async def test_set_cloud_authorization_header(httpx_mock: HTTPXMock):
    with ZepClient(base_url=API_BASE_URL, api_key=None, project_api_key="z_test-api-key") as client:
        httpx_mock.add_response(status_code=200)
        response = await client.aclient.get(f"{client.base_url}/my-endpoint")

    assert response.status_code == 200
    assert "Authorization" in response.request.headers
    assert response.request.headers["Authorization"] == "Api-Key z_test-api-key"

@pytest.mark.asyncio
async def test_set_open_source_authorization_header(httpx_mock: HTTPXMock):
    with ZepClient(base_url=API_BASE_URL, api_key="myapikey", project_api_key=None) as client:
        httpx_mock.add_response(status_code=200)
        response = await client.aclient.get(f"{client.base_url}/my-endpoint")

    assert response.status_code == 200
    assert "Authorization" in response.request.headers
    assert response.request.headers["Authorization"] == "Bearer myapikey"


@pytest.mark.usefixtures("undo_mock_healthcheck")
def test_concat_url():
    assert concat_url("https://server.com", "/v1/api") == "https://server.com/v1/api"
    assert (
        concat_url("https://server.com/zep", "/v1/api")
        == "https://server.com/zep/v1/api"
    )
    assert (
        concat_url("https://server.com/zep/", "/v1/api")
        == "https://server.com/zep/v1/api"
    )
    assert (
        concat_url("https://server.com/zep", "v1/api")
        == "https://server.com/zep/v1/api"
    )
    assert (
        concat_url("https://server.com/zep/", "v1/api")
        == "https://server.com/zep/v1/api"
    )


def test_parse_version_string_with_dash():
    assert parse_version_string("1.2.3-456") == Version("1.2.3")


def test_parse_version_string_with_dash_and_empty_prefix():
    assert parse_version_string("-456") == Version("0.0.0")


def test_parse_version_string_with_dash_and_empty_prefix():
    assert parse_version_string("abc") == Version("0.0.0")


def test_parse_version_string_without_dash():
    assert parse_version_string("1.2.3") == Version("0.0.0")


def test_parse_version_string_empty():
    assert parse_version_string("") == Version("0.0.0")


def test_parse_version_string_none():
    with pytest.raises(TypeError):
        parse_version_string(None)
