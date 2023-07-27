# mypy: ignore-errors

import pytest
from pytest_httpx import HTTPXMock

from tests.fixtures import API_BASE_URL, mock_healthcheck, undo_mock_healthcheck
from zep_python import APIError
from zep_python.zep_client import ZepClient, concat_url

_ = mock_healthcheck, undo_mock_healthcheck


@pytest.mark.usefixtures("undo_mock_healthcheck")
def test_client_connect_healthcheck_fail(httpx_mock: HTTPXMock):
    with pytest.raises(APIError):
        ZepClient(base_url=API_BASE_URL)


@pytest.mark.usefixtures("undo_mock_healthcheck")
def test_client_connect_healthcheck_pass(httpx_mock: HTTPXMock):
    """Explicitly undo the mock healthcheck and then add a new mock response"""
    httpx_mock.add_response(status_code=200, text=".")

    ZepClient(base_url=API_BASE_URL)


@pytest.mark.asyncio
async def test_set_authorization_header(httpx_mock: HTTPXMock):
    with ZepClient(base_url=API_BASE_URL, api_key="myapikey") as client:
        httpx_mock.add_response(status_code=200)
        response = await client.aclient.get(f"{client.base_url}/my-endpoint")

    assert response.status_code == 200
    assert "Authorization" in response.request.headers
    assert response.request.headers["Authorization"] == "Bearer myapikey"


@pytest.mark.usefixtures("undo_mock_healthcheck")
def test_concat_url():
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
