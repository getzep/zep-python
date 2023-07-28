from __future__ import annotations

import json
import warnings
from typing import Dict, List, Optional

import httpx

from zep_python.exceptions import APIError, AuthError, NotFoundError
from .models import Document, Collection

MAX_DOCUMENTS = 1000


class DocumentClient:
    """
    DocumentClient implements Zep's document APIs.

    Attributes
    ----------
    aclient : httpx.AsyncClient
        The async client used for making API requests.

    Methods
    -------
    add_collection(collection: DocumentCollection) -> str:
        Asynchronously create a collection.

    update_collection(collection: DocumentCollection) -> str:
        Asynchronously update collection.

    delete_collection(collection_name: str) -> str:
        Asynchronously delete collection.

    get_collection(collection_name: str) -> DocumentCollection:
        Asynchronously gets a collection.

    list_collections() -> List[DocumentCollection]:
        Asynchronously gets all collections.

    """

    def __init__(self, aclient: httpx.AsyncClient) -> None:
        """
        Initialize the zep_documents client.

        Parameters
        ----------
        aclient : httpx.AsyncClient
            The async client used for making API requests.

        client : httpx.Client
            The client used for making API requests.
        """
        self.aclient = aclient

    def _handle_response(
        self, response: httpx.Response, missing_doc: Optional[str] = None
    ) -> None:
        missing_doc = missing_doc or "No query results found"
        if response.status_code == 404:
            raise NotFoundError(missing_doc)

        if response.status_code == 401:
            raise AuthError(response)

        if response.status_code != 200:
            raise APIError(response)

    async def aadd_collection(self, collection: Collection) -> str:
        """
        Asynchronously create a collection.

        Parameters
        ----------
        collection : Collection
            A DocumentCollection object representing the
            collection to be created.

        Returns
        -------
        str
            The response text from the API.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if (
            collection is None
            or collection.name is None
            or collection.name.strip() == ""
        ):
            raise ValueError("collection name must be provided")

        response = await self.aclient.post(
            "/collection/{collection.name}",
            json=collection.dict(exclude_none=True),
        )

        self._handle_response(response)

        return response.text

    # Document Collection APIs : Update a document collection
    async def update_collection(self, collection: Collection) -> str:
        """
        Asynchronously update collection.

        Parameters
        ----------
        collection : Collection
            A DocumentCollection object representing the collection
            to be added or updated.

        Returns
        -------
        str
            The response text from the API.

        Raises
        ------
        NotFoundError
            If the collection is not found.

        APIError
            If the API response format is unexpected.
        """
        if (
            collection is None
            or collection.name is None
            or collection.name.strip() == ""
        ):
            raise ValueError("collection name must be provided")

        response = await self.aclient.patch(
            f"/collection/{collection.name}",
            json=collection.dict(exclude_none=True),
        )

        self._handle_response(response)

        return response.text

    # Document Collection APIs : Delete a document collection
    async def delete_collection(self, name: str) -> str:
        """
        Asynchronously delete collection.

        Parameters
        ----------
        name : str
            The name of the collection to be deleted.

        Returns
        -------
        str
            The response text from the API.

        Raises
        ------
        NotFoundError
            If the collection is not found.

        APIError
            If the API response format is unexpected.
        """
        if name is None or name.strip() == "":
            raise ValueError("collection name must be provided")

        response = await self.aclient.delete(
            f"/collection/{name}",
        )

        self._handle_response(response)

        return response.text

    # Document Collection APIs : Get a document collection
    async def get_collection(self, name: str) -> Collection:
        """
        Asynchronously gets a collection.

        Parameters
        ----------
        name : str
            The name of the collection to get.

        Returns
        -------
        Collection
            The document collection object.

        Raises
        ------
        NotFoundError
            If the collection is not found.

        APIError
            If the API response format is unexpected.
        """
        if name is None or name.strip() == "":
            raise ValueError("collection name must be provided")
        response = await self.aclient.get(
            f"/collection/{name}",
        )

        self._handle_response(response)

        return Collection(**response.json())

    # Document Collection APIs : List the documetns in a document collection
    async def list_collections(self) -> List[Collection]:
        """
        Asynchronously gets all collections.

        Returns
        -------
        List[Collection]
            The list of document collection objects.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        response = await self.aclient.get(
            "/collection",
        )

        self._handle_response(response)
        return [Collection(**collection) for collection in response.json()]

    # Document APIs : Add a document
    async def add_document(
        self, collection_name: str, documents: List[Document]
    ) -> List[str]:
        """
        Asynchronously create a document.

        Parameters
        ----------
        collection_name : str
            The name of the document collection to add the document to.

        documents : List[Document]
            A list of Document objects representing the documents to be create.

        Returns
        -------
        str
            The response text from the API.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if collection_name is None or collection_name.strip() == "":
            raise ValueError("document collection name must be provided")

        if documents is None:
            raise ValueError("document list must be provided")

        documents_dicts = [document.dict(exclude_none=True) for document in documents]

        response = await self.aclient.post(
            f"/collection/{collection_name}/document",
            json=documents_dicts,
        )

        self._handle_response(response)

        return json.loads(response.text)

    # Document APIs : Update a document by uuid
    async def update_document(self, collection_name: str, document: Document) -> str:
        """
        Asynchronously update document by UUID.

        Parameters
        ----------
        collection_name : str
            The name of the document collection to update the document to.
        document : Document
            A Document object representing the document to be added or updated.

        Returns
        -------
        str
            The response text from the API.

        Raises
        ------
        NotFoundError
            If the document is not found.

        APIError
            If the API response format is unexpected.
        """
        if collection_name is None or collection_name.strip() == "":
            raise ValueError("document collection name must be provided")

        if document is None or document.uuid is None or document.uuid.strip() == "":
            raise ValueError("document uuid must be provided")

        response = await self.aclient.patch(
            f"/collection/{collection_name}/document/uuid/{document.uuid}",
            json=document.dict(exclude_none=True),
        )

        self._handle_response(response)

        return response.text

    # Document APIs : Delete a document
    async def delete_document(self, collection_name: str, document_uuid: str) -> str:
        """
        Asynchronously delete document.

        Parameters
        ----------
        collection_name : str
            The name of the document collection to delete the document from.
        document_uuid : str
            The uuid of the document to be deleted.

        Returns
        -------
        str
            The response text from the API.

        Raises
        ------
        NotFoundError
            If the document is not found.

        APIError
            If the API response format is unexpected.
        """
        if collection_name is None or collection_name.strip() == "":
            raise ValueError("document collection name must be provided")

        if document_uuid is None or document_uuid.strip() == "":
            raise ValueError("document uuid must be provided")

        response = await self.aclient.delete(
            f"/collection/{collection_name}/document/uuid/{document_uuid}",
        )

        self._handle_response(response)

        return response.text

    # Document APIs : Get a document
    async def get_document(self, collection_name: str, document_uuid: str) -> Document:
        """
        Asynchronously gets a document.

        Parameters
        ----------
        collection_name : str
            The name of the document collection to get the document from.

        document_uuid : str
            The name of the document to get.

        Returns
        -------
        Document
            The document object.

        Raises
        ------
        NotFoundError
            If the document is not found.

        APIError
            If the API response format is unexpected.
        """
        if collection_name is None or collection_name.strip() == "":
            raise ValueError("document name must be provided")

        if document_uuid is None or document_uuid.strip() == "":
            raise ValueError("document uuid must be provided")

        response = await self.aclient.get(
            f"/collection/{collection_name}/document/uuid/{document_uuid}",
        )

        self._handle_response(response)

        return Document(**response.json())

    # Document Batch APIs
    async def batch_update_documents(
        self, collection_name: str, documents: List[Document]
    ) -> str:
        """
        Asynchronously batch update documents.

        Parameters
        ----------
        collection_name : str
            The name of the document collection to update the documents to.
        documents : List[Document]
            A list of Document objects representing the documents to be added
            or updated.

        Returns
        -------
        str
            The response text from the API.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if collection_name is None or collection_name.strip() == "":
            raise ValueError("document collection name must be provided")

        if documents is None:
            raise ValueError("document list must be provided")

        if len(documents) > MAX_DOCUMENTS:
            warnings.warn(
                f"The number of documents exceeds the limit of {MAX_DOCUMENTS}. "
                + f"Only the first {MAX_DOCUMENTS} documents will be updated."
            )

        # Limit the number of documents updated
        documents = documents[:MAX_DOCUMENTS]

        documents_dicts = [document.dict(exclude_none=True) for document in documents]

        response = await self.aclient.patch(
            f"/collection/{collection_name}/document/batchUpdate",
            json=documents_dicts,
        )

        self._handle_response(response)

        return response.text

    async def batch_delete_documents(
        self, collection_name: str, document_uuids: List[str]
    ) -> str:
        """
        Asynchronously batch delete documents.

        Parameters
        ----------
        collection_name : str
            The name of the document collection to delete the documents from.
        document_uuids : List[str]
            A list of document uuids to be deleted.

        Returns
        -------
        str
            The response text from the API.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if collection_name is None or collection_name.strip() == "":
            raise ValueError("document collection name must be provided")

        if document_uuids is None:
            raise ValueError("document uuid list must be provided")

        if len(document_uuids) > MAX_DOCUMENTS:
            warnings.warn(
                f"The number of documents exceeds the limit of {MAX_DOCUMENTS}. "
                + f"Only the first {MAX_DOCUMENTS} documents will be deleted."
            )

        # Limit the number of documents fetched
        document_uuids = document_uuids[:MAX_DOCUMENTS]

        response = await self.aclient.post(
            f"/collection/{collection_name}/document/batchDelete",
            json=document_uuids,
        )

        self._handle_response(response)

        return response.text

    async def batch_get_documents(
        self, collection_name: str, document_identifiers: Dict[str, List[str]]
    ) -> List[Document]:
        """
        Asynchronously batch gets documents.

        Parameters
        ----------
        collection_name : str
            The name of the document collection to get the documents from.
        document_identifiers : Dict[str, List[str]]
            A list of document identifiers to be retrieved.

        Returns
        -------
        List[Document]
            The list of document objects.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if collection_name is None or collection_name.strip() == "":
            raise ValueError("document collection name must be provided")

        if not document_identifiers:
            raise ValueError("document identifiers must be provided")

        for key, identifiers in document_identifiers.items():
            if len(identifiers) > MAX_DOCUMENTS:
                warnings.warn(
                    f"The number of documents for {key} exceeds the limit"
                    + f" of {MAX_DOCUMENTS}. "
                    + f"Only the first {MAX_DOCUMENTS} documents will be "
                    + "fetched."
                )
                document_identifiers[key] = identifiers[:MAX_DOCUMENTS]

        response = await self.aclient.post(
            f"/collection/{collection_name}/document/batchGet",
            json=document_identifiers,
        )

        self._handle_response(response)

        return [Document(**document) for document in response.json()]
