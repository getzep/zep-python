from __future__ import annotations

from typing import List, Optional, Dict

import warnings

import httpx

import json

from zep_python.models import (
    Document,
    DocumentCollection,
)
from zep_python.exceptions import APIError, AuthError, NotFoundError

MAX_DOCUMENTS = 1000

class DocumentClient:
    """
    document_client class implementation for document APIs.

    Attributes
    ----------
    base_url : str
        The base URL of the API.
    aclient : httpx.AsyncClient
        The async client used for making API requests.

    Methods
    -------
    add_documentcollection(documentcollection: DocumentCollection) -> str:
        Asynchronously create a documentcollection.

    update_documentcollection(documentcollection: DocumentCollection) -> str:
        Asynchronously update documentcollection.

    delete_documentcollection(documentcollection_name: str) -> str:
        Asynchronously delete documentcollection.

    get_documentcollection(documentcollection_name: str) -> DocumentCollection:
        Asynchronously gets a documentcollection.

    list_documentcollections() -> List[DocumentCollection]:
        Asynchronously gets all documentcollections.

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

    # Document Collection APIs : Add a document collection
    async def add_documentcollection(
        self, documentcollection: DocumentCollection
    ) -> str:
        """
        Asynchronously create a documentcollection.

        Parameters
        ----------
        documentcollection : DocumentCollection
            A DocumentCollection object representing the
            documentcollection to be create.

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
            documentcollection is None
            or documentcollection.name is None
            or documentcollection.name.strip() == ""
        ):
            raise ValueError("documentcollection name must be provided")

        response = await self.aclient.post(
            "/collection/{documentcollection.name}",
            json=documentcollection.dict(exclude_none=True),
        )

        self._handle_response(response)

        return response.text

    # Document Collection APIs : Update a document collection
    async def update_documentcollection(
        self, documentcollection: DocumentCollection
    ) -> str:
        """
        Asynchronously update documentcollection.

        Parameters
        ----------
        documentcollection : DocumentCollection
            A DocumentCollection object representing the documentcollection
            to be added or updated.

        Returns
        -------
        str
            The response text from the API.

        Raises
        ------
        NotFoundError
            If the documentcollection is not found.

        APIError
            If the API response format is unexpected.
        """
        if (
            documentcollection is None
            or documentcollection.name is None
            or documentcollection.name.strip() == ""
        ):
            raise ValueError("documentcollection name must be provided")

        response = await self.aclient.patch(
            f"/collection/{documentcollection.name}",
            json=documentcollection.dict(exclude_none=True),
        )

        self._handle_response(response)

        return response.text

    # Document Collection APIs : Delete a document collection
    async def delete_documentcollection(self, name: str) -> str:
        """
        Asynchronously delete documentcollection.

        Parameters
        ----------
        name : str
            The name of the documentcollection to be deleted.

        Returns
        -------
        str
            The response text from the API.

        Raises
        ------
        NotFoundError
            If the documentcollection is not found.

        APIError
            If the API response format is unexpected.
        """
        if name is None or name.strip() == "":
            raise ValueError("documentcollection name must be provided")

        response = await self.aclient.delete(
            f"/collection/{name}",
        )

        self._handle_response(response)

        return response.text

    # Document Collection APIs : Get a document collection
    async def get_documentcollection(self, name: str) -> DocumentCollection:
        """
        Asynchronously gets a documentcollection.

        Parameters
        ----------
        name : str
            The name of the documentcollection to get.

        Returns
        -------
        DocumentCollection
            The document collection object.

        Raises
        ------
        NotFoundError
            If the documentcollection is not found.

        APIError
            If the API response format is unexpected.
        """
        if name is None or name.strip() == "":
            raise ValueError("documentcollection name must be provided")
        response = await self.aclient.get(
            f"/collection/{name}",
        )

        self._handle_response(response)

        return DocumentCollection(**response.json())

    # Document Collection APIs : List the documetns in a document collection
    async def list_documentcollections(self) -> List[DocumentCollection]:
        """
        Asynchronously gets all documentcollections.

        Returns
        -------
        List[DocumentCollection]
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
        return [
            DocumentCollection(**documentcollection)
            for documentcollection in response.json()
        ]

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
    async def batchupdate_documents(
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

    async def batchdelete_documents(
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

    async def batchget_documents(
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
