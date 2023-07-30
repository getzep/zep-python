from random import random
from typing import Optional, Union
from uuid import uuid4

import httpx
import pytest
from pydantic import ValidationError
from pytest_httpx import HTTPXMock

from tests.conftest import API_BASE_URL
from zep_python.document import Document
from zep_python.document.collections import (
    LARGE_BATCH_WARNING_LIMIT,
    DocumentCollection,
)
from zep_python.exceptions import APIError, NotFoundError
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


def test_add_documents(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_documents = [gen_mock_document("test_collection", 10) for _ in range(10)]

    uuids = [d.uuid for d in mock_documents]

    mock_collection = generate_mock_collection(1, with_clients=True)

    httpx_mock.add_response(
        method="POST",
        status_code=200,
        json=uuids,
    )

    response = mock_collection.add_documents(
        mock_documents,
    )

    assert response == uuids


@pytest.mark.asyncio
async def test_aupdate_document_valid(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collection = generate_mock_collection(1, with_clients=True)

    httpx_mock.add_response(
        method="PATCH",
        status_code=200,
    )

    await mock_collection.aupdate_document(
        uuid=str(uuid4()),
        description="test_document",
        metadata={"name": "test_document"},
    )


@pytest.mark.asyncio
async def test_aupdate_document_not_found(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collection = generate_mock_collection(1, with_clients=True)

    httpx_mock.add_response(
        method="PATCH",
        status_code=404,
    )

    with pytest.raises(NotFoundError):
        await mock_collection.aupdate_document(
            uuid=str(uuid4()),
            description="test_document",
            metadata={"name": "test_document"},
        )


def test_update_document_valid(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collection = generate_mock_collection(1, with_clients=True)

    httpx_mock.add_response(
        method="PATCH",
        status_code=200,
    )

    mock_collection.update_document(
        uuid=str(uuid4()),
        description="test_document",
        metadata={"name": "test_document"},
    )


@pytest.mark.asyncio
async def test_aupdate_document_invalid_uuid(
    zep_client: ZepClient, httpx_mock: HTTPXMock
):
    mock_collection = generate_mock_collection(1, with_clients=True)

    httpx_mock.add_response(
        method="PATCH",
        status_code=200,
    )

    with pytest.raises(ValueError):
        await mock_collection.aupdate_document(
            uuid=None,  # type: ignore
            description="test_document",
            metadata={"name": "test_document"},
        )


@pytest.mark.asyncio
async def test_aupdate_document_nothing_to_update(
    zep_client: ZepClient, httpx_mock: HTTPXMock
):
    mock_collection = generate_mock_collection(1, with_clients=True)

    httpx_mock.add_response(
        method="PATCH",
        status_code=200,
    )

    with pytest.raises(ValueError):
        await mock_collection.aupdate_document(uuid=str(uuid4()))


@pytest.mark.asyncio
async def test_adelete_document_valid(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collection = generate_mock_collection(1, with_clients=True)

    httpx_mock.add_response(
        method="DELETE",
        status_code=200,
    )

    await mock_collection.adelete_document(str(uuid4()))


@pytest.mark.asyncio
async def test_adelete_document_not_found(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collection = generate_mock_collection(1, with_clients=True)

    httpx_mock.add_response(
        method="DELETE",
        status_code=404,
    )

    with pytest.raises(NotFoundError):
        await mock_collection.adelete_document(str(uuid4()))


@pytest.mark.asyncio
async def test_adelete_document_invalid_uuid(
    zep_client: ZepClient,
):
    mock_collection = generate_mock_collection(1, with_clients=True)

    with pytest.raises(ValueError):
        await mock_collection.adelete_document(None)  # type: ignore


def test_delete_document_valid(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collection = generate_mock_collection(1, with_clients=True)

    httpx_mock.add_response(
        method="DELETE",
        status_code=200,
    )

    mock_collection.delete_document(str(uuid4()))


@pytest.mark.asyncio
async def test_aget_document(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collection = generate_mock_collection(1, with_clients=True)

    mock_document = gen_mock_document("test_collection", 10)

    httpx_mock.add_response(
        method="GET",
        status_code=200,
        json=mock_document.dict(),
    )

    response = await mock_collection.aget_document(mock_document.uuid)

    assert response == mock_document


@pytest.mark.asyncio
async def test_aget_document_not_found(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collection = generate_mock_collection(1, with_clients=True)

    httpx_mock.add_response(
        method="GET",
        status_code=404,
    )

    with pytest.raises(NotFoundError):
        await mock_collection.aget_document(str(uuid4()))


def test_get_document(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collection = generate_mock_collection(1, with_clients=True)

    mock_document = gen_mock_document("test_collection", 10)

    httpx_mock.add_response(
        method="GET",
        status_code=200,
        json=mock_document.dict(),
    )

    response = mock_collection.get_document(mock_document.uuid)

    assert response == mock_document


@pytest.mark.asyncio
async def test_aget_documents(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collection = generate_mock_collection(1, with_clients=True)
    mock_documents = [gen_mock_document("test_collection", i) for i in range(10)]

    httpx_mock.add_response(
        method="POST",
        status_code=200,
        json=[doc.dict() for doc in mock_documents],
    )

    response = await mock_collection.aget_documents(
        [doc.uuid for doc in mock_documents]
    )

    assert response == mock_documents


def test_get_documents(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collection = generate_mock_collection(1, with_clients=True)
    mock_documents = [gen_mock_document("test_collection", i) for i in range(10)]

    httpx_mock.add_response(
        method="POST",
        status_code=200,
        json=[doc.dict() for doc in mock_documents],
    )

    response = mock_collection.get_documents([doc.uuid for doc in mock_documents])

    assert response == mock_documents


@pytest.mark.asyncio
async def test_aget_documents_no_uuids(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collection = generate_mock_collection(1, with_clients=True)

    with pytest.raises(ValueError):
        await mock_collection.aget_documents([])


@pytest.mark.asyncio
async def test_aget_documents_no_collection(
    zep_client: ZepClient,
):
    mock_collection = generate_mock_collection(1, with_clients=False)

    with pytest.raises(ValueError):
        await mock_collection.aget_documents(["uuid"])


@pytest.mark.asyncio
async def test_aget_documents_large_batch(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collection = generate_mock_collection(1, with_clients=True)
    mock_documents = [
        gen_mock_document("test_collection", i)
        for i in range(LARGE_BATCH_WARNING_LIMIT + 1)
    ]

    httpx_mock.add_response(
        method="POST",
        status_code=200,
        json=[doc.dict() for doc in mock_documents],
    )

    with pytest.warns(UserWarning):
        await mock_collection.aget_documents([doc.uuid for doc in mock_documents])


@pytest.mark.asyncio
async def test_aget_documents_api_error(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collection = generate_mock_collection(1, with_clients=True)
    mock_documents = [gen_mock_document("test_collection", i) for i in range(10)]

    httpx_mock.add_response(
        method="POST",
        status_code=400,
        json={"unexpected": "response"},
    )

    with pytest.raises(APIError):
        await mock_collection.aget_documents([doc.uuid for doc in mock_documents])


def test_create_collection_index(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collection = generate_mock_collection(1, with_clients=True)

    httpx_mock.add_response(
        method="POST",
        status_code=200,
    )

    mock_collection.create_index()


@pytest.mark.asyncio
async def test_asearch_documents(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collection = generate_mock_collection(1, with_clients=True)
    mock_documents = [gen_mock_document("test_collection", i) for i in range(10)]

    httpx_mock.add_response(
        method="POST",
        status_code=200,
        json=[doc.dict() for doc in mock_documents],
    )

    response = await mock_collection.asearch("search_text", {"key": "value"}, 10)

    assert response == mock_documents


def test_search_documents(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collection = generate_mock_collection(1, with_clients=True)
    mock_documents = [gen_mock_document("test_collection", i) for i in range(10)]

    httpx_mock.add_response(
        method="POST",
        status_code=200,
        json=[doc.dict() for doc in mock_documents],
    )

    response = mock_collection.search("search_text", {"key": "value"}, 10)

    assert response == mock_documents


@pytest.mark.asyncio
async def test_asearch_documents_no_limit(zep_client: ZepClient, httpx_mock: HTTPXMock):
    mock_collection = generate_mock_collection(1, with_clients=True)
    mock_documents = [gen_mock_document("test_collection", i) for i in range(10)]

    httpx_mock.add_response(
        method="POST",
        status_code=200,
        json=[doc.dict() for doc in mock_documents],
    )

    response = await mock_collection.asearch(
        "search_text",
        {"key": "value"},
    )

    assert response == mock_documents


@pytest.mark.asyncio
async def test_asearch_documents_no_metadata(
    zep_client: ZepClient, httpx_mock: HTTPXMock
):
    mock_collection = generate_mock_collection(1, with_clients=True)
    mock_documents = [gen_mock_document("test_collection", i) for i in range(10)]

    httpx_mock.add_response(
        method="POST",
        status_code=200,
        json=[doc.dict() for doc in mock_documents],
    )

    response = await mock_collection.asearch("search_text")

    assert response == mock_documents


@pytest.mark.asyncio
async def test_asearch_documents_no_collection(
    zep_client: ZepClient, httpx_mock: HTTPXMock
):
    mock_collection = generate_mock_collection(1, with_clients=False)

    with pytest.raises(ValueError):
        await mock_collection.asearch("search_text", {"key": "value"}, 10)


@pytest.mark.asyncio
async def test_asearch_documents_api_error(
    zep_client: ZepClient, httpx_mock: HTTPXMock
):
    mock_collection = generate_mock_collection(1, with_clients=True)

    httpx_mock.add_response(
        method="POST",
        status_code=400,
        json={"unexpected": "response"},
    )

    with pytest.raises(APIError):
        await mock_collection.asearch("search_text", {"key": "value"}, 10)


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
