from typing import List
from uuid import uuid4

import pytest
from pydantic import ValidationError
from pytest_httpx import HTTPXMock

from zep_python.document import DocumentCollectionModel, Document
from zep_python.document.collections import DocumentCollection
from zep_python.zep_client import ZepClient


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "name,collection",
    [
        (
            "collection_all_fields",
            DocumentCollection(
                name="test_collection",
                description="Test Collection",
                is_auto_embedded=True,
                embedding_dimensions=10,
            ),
        ),
        (
            "collection_required_fields",
            DocumentCollection(
                name="test_collection",
                embedding_dimensions=10,
            ),
        ),
    ],
)
async def test_add_collection_valid(
    name: str, collection: DocumentCollection, httpx_mock: HTTPXMock, zep_client
):
    # mock call to aadd_collection
    httpx_mock.add_response(method="POST", status_code=200)
    # mock call to aget_collection inside aadd_collection
    httpx_mock.add_response(method="GET", status_code=200, json=collection.dict())

    response = await zep_client.document.aadd_collection(collection)

    assert response == collection


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "name,collection_data",
    [
        (
            "collection_missing_required",
            {
                "name": "test_collection",
                "description": "Test Collection",
                "is_auto_embedded": True,
            },
        ),
        (
            "collection_unknown_field",
            {
                "name": "test_collection",
                "unknown_field": 10,
            },
        ),
    ],
)
async def test_add_collection_invalid(name: str, collection_data: dict, zep_client):
    with pytest.raises(ValidationError):
        _ = DocumentCollection(**collection_data)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "name,collection",
    [
        (
            "collection_all_fields",
            DocumentCollection(
                uuid=uuid4(),
                description="Test Collection",
            ),
        ),
        (
            "collection_required_fields",
            DocumentCollection(
                uuid=uuid4(),
                name="test_collection",
                metadata={"key": "value"},
            ),
        ),
    ],
)
async def test_update_collection_valid(
    name: str, collection: DocumentCollection, httpx_mock: HTTPXMock, zep_client
):
    # mock call to aupdate_collection
    httpx_mock.add_response(method="POST", status_code=200)
    # mock call to aget_collection inside aupdate_collection
    httpx_mock.add_response(method="GET", status_code=200, json=collection.dict())

    response = await zep_client.document.aupdate_collection(collection)

    assert response == collection


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "name,collection_data",
    [
        (
            "collection_missing_required",
            {
                "name": "test_collection",
                "description": "Test Collection",
                "is_auto_embedded": True,
            },
        ),
        (
            "collection_unknown_field",
            {
                "name": "test_collection",
                "unknown_field": 10,
            },
        ),
    ],
)
async def test_update_collection_invalid(name: str, collection_data: dict, zep_client):
    with pytest.raises(ValidationError):
        _ = DocumentCollection(**collection_data)
