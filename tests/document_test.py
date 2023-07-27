from typing import Dict, List
from uuid import uuid4

import pytest
from pytest_httpx import HTTPXMock

from zep_python import NotFoundError
from zep_python.models import Document, DocumentCollection
from zep_python.zep_client import ZepClient

api_base_url = "http://localhost/api/v1"

mock_collection_id = str(uuid4())
mock_collection = DocumentCollection(
    name="mock_collection",
    description="Mock Collection",
    metadata={"key": "value"},
    embedding_dimensions=768,
    embedding_model_name="bert-base-uncased",
    distance_function="cosine",
    is_normalized=True,
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

mock_modifieddocument = Document(
    uuid=mock_document_uuid,
    metadata={"jelly": "fish"},
)

mock_batchdocument = [
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

mock_getbatchrequest_byuuid = {
    "uuids": [mock_document_uuid, mock_document_uuid2],
}

mock_getbatchrequest_byid = {
    "document_ids": [mock_document_id, "2"],
}


def validate__collection(collection: DocumentCollection) -> None:
    assert collection.name == "mock_collection"
    assert collection.description == "Mock Collection"
    assert collection.metadata == {"key": "value"}
    assert collection.embedding_dimensions == 768
    assert collection.embedding_model_name == "bert-base-uncased"
    assert collection.distance_function == "cosine"
    assert collection.is_normalized == True


def validate__document(document: Document) -> None:
    assert document.id == mock_document_id
    assert document.uuid == mock_document_uuid
    assert document.content == "mock content"
    assert document.metadata == {"key": "value"}
    assert document.embedding == [1.0, 2.0, 3.0]


def validate__batchdocument(documents: List[Document]) -> None:
    # Predefined collection and document objects
    mock_collection = DocumentCollection(
        name="mock_collection", description="Mock Collection", id=mock_collection_id
    )


mock_document = Document(id=mock_document_id, data={"key": "value"})


@pytest.mark.asyncio
async def test_add_collection(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json="Collection Added")

    async with ZepClient(base_url=api_base_url) as client:
        response = await client.add_collection(mock_collection)

        assert response == '"Collection Added"'


@pytest.mark.asyncio
async def test_get_collection(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json=mock_collection.dict())

    async with ZepClient(base_url=api_base_url) as client:
        collection = await client.get_collection(mock_collection_id)

        validate__collection(collection)


@pytest.mark.asyncio
async def test_update_collection(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json="Collection Updated")

    async with ZepClient(base_url=api_base_url) as client:
        response = await client.update_collection(mock_collection)

        assert response == '"Collection Updated"'


@pytest.mark.asyncio
async def test_delete_collection(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json="Collection Deleted")

    async with ZepClient(base_url=api_base_url) as client:
        status = await client.delete_collection(mock_collection_id)

        assert status == '"Collection Deleted"'


@pytest.mark.asyncio
async def test_get_document(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json=mock_document.dict())

    async with ZepClient(base_url=api_base_url) as client:
        document = await client.get_document(mock_collection_id, mock_document_id)

        assert document == mock_document


@pytest.mark.asyncio
async def test_add_document(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json={"ids": [mock_document_id]})

    async with ZepClient(base_url=api_base_url) as client:
        document_ids = await client.add_document(mock_collection_id, [mock_document])

        assert document_ids["ids"] == [mock_document_id]


@pytest.mark.asyncio
async def test_update_document(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json="Document Updated")

    async with ZepClient(base_url=api_base_url) as client:
        status = await client.update_document(mock_collection_id, mock_modifieddocument)

        assert status == '"Document Updated"'


@pytest.mark.asyncio
async def test_delete_document(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json="Document Deleted")

    async with ZepClient(base_url=api_base_url) as client:
        status = await client.delete_document(mock_collection_id, mock_document_id)

        assert status == '"Document Deleted"'


@pytest.mark.asyncio
async def test_batchupdate_documents(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json="Batch Updated")

    async with ZepClient(base_url=api_base_url) as client:
        status = await client.batchupdate_documents(mock_collection_id, [mock_document])

        assert status == '"Batch Updated"'


@pytest.mark.asyncio
async def test_batchdelete_documents(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json="Batch Deleted")

    async with ZepClient(base_url=api_base_url) as client:
        status = await client.batchdelete_documents(
            mock_collection_id, [mock_document_id]
        )

        assert status == '"Batch Deleted"'


@pytest.mark.asyncio
async def test_batchget_documents_byid(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json=[mock_document.dict()])

    async with ZepClient(base_url=api_base_url) as client:
        documents = await client.batchget_documents_byid(
            mock_collection_id, mock_getbatchrequest_byid
        )
        print(documents)

        assert documents[0].dict() == mock_document.dict()


@pytest.mark.asyncio
async def test_batchget_documents_byuuid(httpx_mock: HTTPXMock):
    httpx_mock.add_response(status_code=200, json=[mock_document.dict()])

    async with ZepClient(base_url=api_base_url) as client:
        documents = await client.batchget_documents_byuuid(
            mock_collection_id, mock_getbatchrequest_byuuid
        )
        print(documents)

        assert documents[0].dict() == mock_document.dict()
