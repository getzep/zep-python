from random import random
from typing import Union, Optional
from uuid import uuid4

import httpx
import pytest
from pydantic import ValidationError
from pytest_httpx import HTTPXMock

from tests.conftest import API_BASE_URL
from zep_python.document import Document
from zep_python.document.collections import DocumentCollection
from zep_python.exceptions import NotFoundError
from zep_python.zep_client import ZepClient

validation_error_types = (ValidationError, ValueError)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "name,collection_data",
    [
        (
            "collection_all_fields",
            {
                "name": "test_collection",
                "description": "Test Collection",
                "metadata": {"key": "value"},
                "is_auto_embedded": True,
                "embedding_dimensions": 10,
            },
        ),
        (
            "collection_required_fields",
            {
                "name": "test_collection",
                "embedding_dimensions": 10,
            },
        ),
    ],
)
async def test_add_collection_valid(
    name: str, collection_data: dict, httpx_mock: HTTPXMock, zep_client
):
    # mock call to aadd_collection
    httpx_mock.add_response(method="POST", status_code=200)
    # mock call to aget_collection inside aadd_collection
    httpx_mock.add_response(method="GET", status_code=200, json=collection_data)

    response = await zep_client.document.aadd_collection(**collection_data)

    assert response == DocumentCollection(**collection_data)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "name,collection_data",
    [
        (
            "collection_missing_required",
            {
                "name": "",
                "description": "Test Collection",
                "is_auto_embedded": True,
                "embedding_dimensions": 10,
            },
        ),
        (
            "collection_dims_none",
            {
                "name": "test_collection",
                "embedding_dimensions": None,
            },
        ),
    ],
)
async def test_add_collection_invalid(name: str, collection_data: dict, zep_client):
    with pytest.raises(validation_error_types):
        _ = await zep_client.document.aadd_collection(**collection_data)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "name,collection_data",
    [
        (
            "collection_all_fields",
            {
                "name": "test_collection",
                "description": "Test Collection",
                "metadata": {"key": "value"},
            },
        ),
        (
            "collection_required_fields",
            {
                "name": "test_collection",
            },
        ),
    ],
)
async def test_update_collection_valid(
    name: str, collection_data: dict, httpx_mock: HTTPXMock, zep_client
):
    # mock call to aupdate_collection
    httpx_mock.add_response(method="PATCH", status_code=200)
    # mock call to aget_collection inside aupdate_collection
    httpx_mock.add_response(method="GET", status_code=200, json=collection_data)

    response = await zep_client.document.aupdate_collection(**collection_data)

    assert response == DocumentCollection(**collection_data)


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "name,collection_data",
    [
        (
            "collection_missing_required",
            {
                "name": "",
                "description": "Test Collection",
            },
        ),
        (
            "collection_metadata_not_dict",
            {
                "name": "test_collection",
                "metadata": "hello",
            },
        ),
    ],
)
async def test_update_collection_invalid(name: str, collection_data: dict, zep_client):
    with pytest.raises(validation_error_types):  # type: ignore
        _ = await zep_client.document.aupdate_collection(**collection_data)


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


def test_collection_method_call_without_httpx(zep_client: ZepClient):
    mock_collection = generate_mock_collection(1)
    with pytest.raises(ValueError):
        _ = mock_collection.add_documents(
            [
                gen_mock_document(
                    "test",
                )
            ]
        )


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


@pytest.mark.asyncio
async def test_aadd_documents(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_documents = [gen_mock_document("test_collection", 10) for _ in range(10)]

    uuids = [d.uuid for d in mock_documents]

    mock_collection = generate_mock_collection(1, with_clients=True)

    httpx_mock.add_response(
        method="POST",
        status_code=200,
        json=uuids,
    )

    response = await mock_collection.aadd_documents(
        mock_documents,
    )

    assert response == uuids


def generate_mock_collection(
    col_id: Union[int, str], with_clients: bool = False
) -> DocumentCollection:
    clients = {}
    if with_clients:
        clients = {
            "client": httpx.Client(base_url=API_BASE_URL),
            "aclient": httpx.AsyncClient(base_url=API_BASE_URL),
        }
    return DocumentCollection(
        **clients,
        uuid=str(uuid4()),
        name=f"test_collection_{col_id}",
        description="Test Collection",
        is_auto_embedded=True,
        embedding_dimensions=10,
    )


def gen_mock_document(
    collection_name: str,
    embedding_dimensions: Optional[int] = None,
) -> Document:
    embedding = (
        [random() for _ in range(embedding_dimensions)]
        if embedding_dimensions
        else None
    )

    return Document(
        uuid=str(uuid4()),
        collection_name=collection_name,
        content="Test Document",
        embedding=embedding,
        metadata={"key": "value"},
    )
