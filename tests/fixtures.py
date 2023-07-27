# mypy: ignore-errors

import pytest
from pytest_httpx import HTTPXMock

API_BASE_URL = "http://localhost:8000/api/v1"


@pytest.fixture(autouse=True)
def mock_healthcheck(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, text=".")
    yield


@pytest.fixture
def undo_mock_healthcheck(httpx_mock: HTTPXMock):
    httpx_mock.reset(False)
    yield


@pytest.fixture
def assert_all_responses_were_requested() -> bool:
    return False
