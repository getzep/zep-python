from __future__ import annotations

from typing import List, Optional

import httpx

from zep_python.models import (
    Document,
    DocumentCollection,
)
from zep_python.exceptions import APIError, AuthError, NotFoundError


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
        print(documentcollection)
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
    async def delete_documentcollection(self, documentcollection_name: str) -> str:
        """
        Asynchronously delete documentcollection.

        Parameters
        ----------
        documentcollection_name : str
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
        if documentcollection_name is None or documentcollection_name.strip() == "":
            raise ValueError("documentcollection name must be provided")

        response = await self.aclient.delete(
            "/collection/{documentcollection_name}",
        )

        self._handle_response(response)

        return response.text

    # Document Collection APIs : Get a document collection
    async def get_documentcollection(
        self, documentcollection_name: str
    ) -> DocumentCollection:
        """
        Asynchronously gets a documentcollection.

        Parameters
        ----------
        documentcollection_name : str
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
        if documentcollection_name is None or documentcollection_name.strip() == "":
            raise ValueError("documentcollection name must be provided")

        response = await self.aclient.get(
            "/collection/{documentcollection_name}",
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
    async def add_document(self, document: Document) -> str:
        """
        Asynchronously create a document.

        Parameters
        ----------
        document : Document
            A Document object representing the document to be create.

        Returns
        -------
        str
            The response text from the API.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if document is None or document.id is None or document.id.strip() == "":
            raise ValueError("document id must be provided")

        response = await self.aclient.post(
            "/document",
            json=document.dict(exclude_none=True),
        )

        self._handle_response(response)

        return response.text

    # Document APIs : Update a document
    async def update_document(self, document: Document) -> str:
        """
        Asynchronously update document.

        Parameters
        ----------
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
        if document is None or document.id is None or document.id.strip() == "":
            raise ValueError("document name must be provided")

        response = await self.aclient.patch(
            "/document/{document.name}",
            json=document.dict(exclude_none=True),
        )

        self._handle_response(response)

        return response.text

    # Document APIs : Delete a document
    async def delete_document(self, document_name: str) -> str:
        """
        Asynchronously delete document.

        Parameters
        ----------
        document_name : str
            The name of the document to be deleted.

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
        if document_name is None or document_name.strip() == "":
            raise ValueError("document name must be provided")

        response = await self.aclient.delete(
            "/document/{document_name}",
        )

        self._handle_response(response)

        return response.text

    # Document APIs : Get a document
    async def get_document(self, document_name: str) -> Document:
        """
        Asynchronously gets a document.

        Parameters
        ----------
        document_name : str
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
        if document_name is None or document_name.strip() == "":
            raise ValueError("document name must be provided")

        response = await self.aclient.get(
            "/document/{document_name}",
        )

        self._handle_response(response)

        return Document(**response.json())

    # Document APIs : List the documents
    async def list_documents(self) -> List[Document]:
        """
        Asynchronously gets all documents.

        Returns
        -------
        List[Document]
            The list of document objects.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        response = await self.aclient.get(
            "/document",
        )

        self._handle_response(response)
        return [Document(**document) for document in response.json()]

    # Document Bulk APIs
