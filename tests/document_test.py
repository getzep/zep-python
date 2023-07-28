from typing import List
from uuid import uuid4

import pytest
from pytest_httpx import HTTPXMock

from tests.fixtures import API_BASE_URL, mock_healthcheck, undo_mock_healthcheck
from zep_python.document import Document, Collection
from zep_python.zep_client import ZepClient

_ = mock_healthcheck, undo_mock_healthcheck

mock_collection_id = str(uuid4())
mock_collection = Collection(
    name="mock_collection",
    description="Mock Collection",
    metadata={"key": "value"},
    embedding_dimensions=768,
    is_auto_embedded=True,
)


mock_document_uuid = str(uuid4())
mock_document_id = str(uuid4())
mock_document_uuid2 = str(uuid4())

mock_document = Document(
    document_id=mock_document_id,
    uuid=mock_document_uuid,
    content="mock content",
    metadata={"key": "value"},
    embedding=[1.0, 2.0, 3.0],
)


mock_modified_document = Document(
    uuid=mock_document_uuid,
    metadata={"jelly": "fish"},
)

mock_batch_document = [
    Document(
        document_id="1",
        uuid=mock_document_uuid,
        content="mock content",
        metadata={"key": "value"},
        embedding=[1.0, 2.0, 3.0],
    ),
    Document(
        document_id="2",
        uuid=mock_document_uuid2,
        content="mock content",
        metadata={"key": "value"},
        embedding=[1.0, 2.0, 3.0],
    ),
]

mock_getbatchrequest_by_uuid = {
    "uuids": [mock_document_uuid, mock_document_uuid2],
}

mock_getbatchrequest_by_id = {
    "document_ids": [mock_document_id, "2"],
}


def validate__collection(collection: Collection) -> None:
    assert collection.name == "mock_collection"
    assert collection.description == "Mock Collection"
    assert collection.metadata == {"key": "value"}
    assert collection.embedding_dimensions == 768
    assert collection.is_auto_embedded is True


def validate__document(document: Document) -> None:
    assert document.uuid == mock_document_uuid
    assert document.document_id == mock_document_id
    assert document.content == "mock content"
    assert document.metadata == {"key": "value"}
    assert document.embedding == [1.0, 2.0, 3.0]


def validate__batchdocument(documents: List[Document]) -> None:
    # Predefined collection and document objects
    Collection(
        name="mock_collection", description="Mock Collection", id=mock_collection_id
    )


@pytest.mark.asyncio
async def test_add_collection(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json="Collection Added")

    async with ZepClient(base_url=API_BASE_URL) as client:
        response = await client.document.aadd_collection(mock_collection)

        assert response == '"Collection Added"'


@pytest.mark.asyncio
async def test_get_collection(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json=mock_collection.dict())

    async with ZepClient(base_url=API_BASE_URL) as client:
        collection = await client.get_collection(mock_collection_id)

        validate__collection(collection)


@pytest.mark.asyncio
async def test_update_collection(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json="Collection Updated")

    async with ZepClient(base_url=API_BASE_URL) as client:
        response = await client.update_collection(mock_collection)

        assert response == '"Collection Updated"'


@pytest.mark.asyncio
async def test_delete_collection(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json="Collection Deleted")

    async with ZepClient(base_url=API_BASE_URL) as client:
        status = await client.delete_collection(mock_collection_id)

        assert status == '"Collection Deleted"'


@pytest.mark.asyncio
async def test_get_document(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json=mock_document.dict())

    async with ZepClient(base_url=API_BASE_URL) as client:
        document = await client.get_document(mock_collection_id, mock_document_id)

        assert document == mock_document


@pytest.mark.asyncio
async def test_add_document(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json=[mock_document_id])

    async with ZepClient(base_url=API_BASE_URL) as client:
        document_ids: List[str] = await client.add_document(
            mock_collection_id, [mock_document]
        )

        assert document_ids[0] == mock_document_id


@pytest.mark.asyncio
async def test_update_document(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json="Document Updated")

    async with ZepClient(base_url=API_BASE_URL) as client:
        status = await client.update_document(
            mock_collection_id, mock_modified_document
        )

        assert status == '"Document Updated"'


@pytest.mark.asyncio
async def test_delete_document(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json="Document Deleted")

    async with ZepClient(base_url=API_BASE_URL) as client:
        status = await client.delete_document(mock_collection_id, mock_document_id)

        assert status == '"Document Deleted"'


@pytest.mark.asyncio
async def test_batchupdate_documents(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json="Batch Updated")

    async with ZepClient(base_url=API_BASE_URL) as client:
        status = await client.batchupdate_documents(mock_collection_id, [mock_document])

        assert status == '"Batch Updated"'


@pytest.mark.asyncio
async def test_batchdelete_documents(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json="Batch Deleted")

    async with ZepClient(base_url=API_BASE_URL) as client:
        status = await client.batchdelete_documents(
            mock_collection_id, [mock_document_id]
        )

        assert status == '"Batch Deleted"'


@pytest.mark.asyncio
async def test_batchget_documents_byid(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json=[mock_document.dict()])

    async with ZepClient(base_url=API_BASE_URL) as client:
        documents = await client.batchget_documents_byid(
            mock_collection_id, mock_getbatchrequest_by_id
        )
        print(documents)

        assert documents[0].dict() == mock_document.dict()


@pytest.mark.asyncio
async def test_batchget_documents_byuuid(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json=[mock_document.dict()])

    async with ZepClient(base_url=API_BASE_URL) as client:
        documents = await client.batchget_documents_byuuid(
            mock_collection_id, mock_getbatchrequest_by_uuid
        )
        print(documents)

        assert documents[0].dict() == mock_document.dict()
