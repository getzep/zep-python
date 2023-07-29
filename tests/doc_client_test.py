from typing import List, Type, Union
from uuid import uuid4

import pytest
from pydantic import ValidationError
from pytest_httpx import HTTPXMock

from zep_python.document import DocumentCollectionModel, Document
from zep_python.document.collections import DocumentCollection
from zep_python.zep_client import ZepClient
from zep_python.exceptions import NotFoundError, APIError

validation_error_types = (ValidationError, ValueError)


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
                "embedding_dimensions": 10,
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
                name="test_collection",
                description="Test Collection",
                metadata={"key": "value"},
            ),
        ),
        (
            "collection_required_fields",
            DocumentCollection(
                name="test_collection",
            ),
        ),
    ],
)
async def test_update_collection_valid(
    name: str, collection: DocumentCollection, httpx_mock: HTTPXMock, zep_client
):
    # mock call to aupdate_collection
    httpx_mock.add_response(method="PATCH", status_code=200)
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
                "description": "Test Collection",
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
    with pytest.raises(validation_error_types):  # type: ignore
        _ = DocumentCollection(**collection_data)


@pytest.mark.asyncio
async def test_list_collections(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collections = [generate_mock_collection(i).dict() for i in range(10)]
    httpx_mock.add_response(
        method="GET",
        status_code=200,
        json=mock_collections,
    )

    response = await zep_client.document.alist_collections()

    assert response == mock_collections


@pytest.mark.asyncio
async def test_get_collection(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collection = generate_mock_collection(1)
    httpx_mock.add_response(
        method="GET",
        status_code=200,
        json=mock_collection.dict(),
    )

    response = await zep_client.document.aget_collection(mock_collection.name)

    assert response == mock_collection


@pytest.mark.asyncio
async def test_get_collection_missing_name(
    zep_client: ZepClient, httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="GET",
        status_code=200,
    )

    with pytest.raises(ValueError):
        _ = await zep_client.document.aget_collection("")


@pytest.mark.asyncio
async def test_get_collection_not_found(zep_client: ZepClient, httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        method="GET",
        status_code=404,
    )

    with pytest.raises(NotFoundError):
        _ = await zep_client.document.aget_collection("unknown")


@pytest.mark.asyncio
async def test_delete_collection(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collection = generate_mock_collection(1)
    httpx_mock.add_response(
        method="DELETE",
        status_code=200,
    )

    response = await zep_client.document.adelete_collection(mock_collection.name)

    assert response is None


@pytest.mark.asyncio
async def test_delete_collection_missing_name(zep_client: ZepClient):
    with pytest.raises(ValueError):
        _ = await zep_client.document.adelete_collection("")


@pytest.mark.asyncio
async def test_delete_collection_not_found(
    zep_client: ZepClient, httpx_mock: HTTPXMock
):
    httpx_mock.add_response(
        method="DELETE",
        status_code=404,
    )

    with pytest.raises(NotFoundError):
        _ = await zep_client.document.adelete_collection("unknown")


def generate_mock_collection(col_id: Union[int, str]) -> DocumentCollection:
    return DocumentCollection(
        uuid=str(uuid4()),
        name=f"test_collection_{col_id}",
        description="Test Collection",
        is_auto_embedded=True,
        embedding_dimensions=10,
    )
