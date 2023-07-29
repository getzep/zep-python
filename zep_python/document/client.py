from __future__ import annotations

from typing import List

import httpx

from zep_python.utils import filter_dict
from zep_python.exceptions import handle_response
from .collections import DocumentCollection


class DocumentClient:
    """
    Implements Zep's document APIs.

    Attributes
    ----------
    client : httpx.Client
        Synchronous API client.
    aclient : httpx.AsyncClient
        Asynchronous API client.

    Methods
    -------
    aadd_collection(collection: DocumentCollection) -> str:
        Asynchronously creates a collection.
    add_collection(collection: DocumentCollection) -> str:
        Synchronously creates a collection.

    aupdate_collection(collection: DocumentCollection) -> str:
        Asynchronously updates a collection.
    update(collection: DocumentCollection) -> str:
        Synchronously updates a collection.

    adelete_collection(collection_name: str) -> str:
        Asynchronously deletes a collection.
    delete_collection(collection_name: str) -> str:
        Synchronously deletes a collection.

    aget_collection(collection_name: str) -> DocumentCollection:
        Asynchronously retrieves a collection.
    get_collection(collection_name: str) -> DocumentCollection:
        Synchronously retrieves a collection.

    alist_collections() -> List[DocumentCollection]:
        Asynchronously retrieves all collections.
    list_collections() -> List[DocumentCollection]:
        Synchronously retrieves all collections.
    """

    def __init__(self, aclient: httpx.AsyncClient, client: httpx.Client) -> None:
        """
        Initialize the DocumentClient with the specified httpx clients.
        """
        self.aclient = aclient
        self.client = client

    async def aadd_collection(
        self, collection: DocumentCollection
    ) -> DocumentCollection:
        """
        Asynchronously creates a collection.

        Parameters
        ----------
        collection : DocumentCollection
            A DocumentCollection object representing the collection to be created. The
            collection name and embedding_dimensions must be provided.

        Returns
        -------
        DocumentCollection
            The newly created collection object, retrieved from the server.

        Raises
        ------
        APIError
            If the API response format is unexpected, or if the server returns an error.
        """

        response = await self.aclient.post(
            "/collection/{collection_create.name}",
            json=collection.dict(exclude_none=True),
        )

        handle_response(response)

        return await self.aget_collection(collection.name)

    def add_collection(self, collection: DocumentCollection) -> DocumentCollection:
        """
        Creates a collection.

        Parameters
        ----------
        collection : DocumentCollection
            A DocumentCollection object representing the collection to be created. The
            collection name and embedding_dimensions must be provided.

        Returns
        -------
        DocumentCollection
            The newly created collection object, retrieved from the server.

        Raises
        ------
        APIError
            If the API response format is unexpected, or if the server returns an error.
        AuthError
            If the API key is invalid.
        """

        validated_dict = DocumentCollection(
            operation="create", **collection.dict(exclude_none=True)
        ).dict(exclude_none=True)

        response = self.client.post(
            "/collection/{collection_create.name}",
            json=validated_dict,
        )

        handle_response(response)

        return self.get_collection(collection.name)

    # Document Collection APIs : Get a document collection
    async def aget_collection(self, name: str) -> DocumentCollection:
        """
        Asynchronously retrieves a collection.

        Parameters
        ----------
        name : str
            Collection name.

        Returns
        -------
        DocumentCollection
            Retrieved collection.

        Raises
        ------
        ValueError
            If no collection name is provided.
        NotFoundError
            If collection not found.
        APIError
            If API response is unexpected.
        AuthError
            If the API key is invalid.
        """
        if name is None or name.strip() == "":
            raise ValueError("collection name must be provided")
        response = await self.aclient.get(
            f"/collection/{name}",
        )

        handle_response(response)

        filtered_response = filter_dict(response.json())

        return DocumentCollection(**filtered_response)

    def get_collection(self, name: str) -> DocumentCollection:
        """
        Retrieves a collection.

        Parameters
        ----------
        name : str
            Collection name.

        Returns
        -------
        DocumentCollection
            Retrieved collection.

        Raises
        ------
        ValueError
            If no collection name is provided.
        NotFoundError
            If collection not found.
        APIError
            If API response is unexpected.
        AuthError
            If the API key is invalid.
        """
        if name is None or name.strip() == "":
            raise ValueError("collection name must be provided")
        response = self.client.get(
            f"/collection/{name}",
        )

        handle_response(response)

        filtered_response = filter_dict(response.json())

        return DocumentCollection(**filtered_response)

    async def aupdate_collection(
        self, collection: DocumentCollection
    ) -> DocumentCollection:
        """
        Asynchronously updates a collection.

        Returns
        -------
        DocumentCollection
            Updated collection.

        Raises
        ------
        NotFoundError
            If collection not found.
        APIError
            If API response is unexpected.
        AuthError
            If the API key is invalid.
        """

        if collection.name is None or collection.name.strip() == "":
            raise ValueError("collection name must be provided")

        response = await self.aclient.patch(
            f"/collection/{collection.name}",
            json=collection.dict(exclude_none=True),
        )

        handle_response(response)

        return await self.aget_collection(collection.name)

    def update(self, collection: DocumentCollection) -> DocumentCollection:
        """
        Updates a collection.

        Returns
        -------
        DocumentCollection
            Updated collection.

        Raises
        ------
        NotFoundError
            If collection not found.
        APIError
            If API response is unexpected.
        AuthError
            If the API key is invalid.
        """

        if collection.name is None or collection.name.strip() == "":
            raise ValueError("collection name must be provided")

        response = self.client.patch(
            f"/collection/{collection.name}",
            json=collection.dict(exclude_none=True),
        )

        handle_response(response)

        return self.get_collection(collection.name)

    # Document Collection APIs : List the documetns in a document collection
    async def alist_collections(self) -> List[DocumentCollection]:
        """
        Asynchronously lists all collections.

        Returns
        -------
        List[DocumentCollection]
            The list of document collection objects.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        AuthError
            If the API key is invalid.
        """
        response = await self.aclient.get(
            "/collection",
        )

        handle_response(response)
        return [DocumentCollection(**collection) for collection in response.json()]

    def list_collections(self) -> List[DocumentCollection]:
        """
        Lists all collections.

        Returns
        -------
        List[DocumentCollection]
            The list of document collection objects.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        AuthError
            If the API key is invalid.
        """
        response = self.client.get(
            "/collection",
        )

        handle_response(response)
        return [DocumentCollection(**collection) for collection in response.json()]

    async def adelete_collection(self, collection_name: str) -> None:
        """
        Asynchronously delete a collection.

        Parameters
        ----------
        collection_name : str
            The name of the collection to delete.

        Returns
        -------
        None

        Raises
        ------
        NotFoundError
            If the collection is not found.
        APIError
            If the API response format is unexpected.
        AuthError
            If the API key is invalid.
        """
        if collection_name is None or collection_name.strip() == "":
            raise ValueError("collection name must be provided")

        response = await self.aclient.delete(
            f"/collection/{collection_name}",
        )

        handle_response(response)

    def delete_collection(self, collection_name: str) -> None:
        """
        Deletes a collection.

        Parameters
        ----------
        collection_name : str
            The name of the collection to delete.

        Returns
        -------
        None

        Raises
        ------
        NotFoundError
            If the collection is not found.
        APIError
            If the API response format is unexpected.
        AuthError
            If the API key is invalid.
        """
        if collection_name is None or collection_name.strip() == "":
            raise ValueError("collection name must be provided")

        response = self.client.delete(
            f"/collection/{collection_name}",
        )

        handle_response(response)
