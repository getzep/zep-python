from __future__ import annotations

from typing import List

import httpx

from zep_python.exceptions import handle_response

from .models import CollectionModel


class DocumentClient:
    """
    DocumentClient implements Zep's document APIs.

    Attributes
    ----------
    client : httpx.Client
        The client used for making API requests.
    aclient : httpx.AsyncClient
        The async client used for making API requests.

    Methods
    -------
    aadd_collection(collection: DocumentCollection) -> str:
        Asynchronously create a collection.

    aupdate_collection(collection: DocumentCollection) -> str:
        Asynchronously update collection.

    adelete_collection(collection_name: str) -> str:
        Asynchronously delete collection.

    aget_collection(collection_name: str) -> DocumentCollection:
        Asynchronously gets a collection.

    alist_collections() -> List[DocumentCollection]:
        Asynchronously gets all collections.

    """

    aclient: httpx.AsyncClient
    client: httpx.Client

    def __init__(self, aclient: httpx.AsyncClient, client: httpx.Client) -> None:
        """
        Initialize the DocumentClient with the specified httpx clients.
        """
        self.aclient = aclient
        self.client = client

    async def aadd_collection(self, collection: CollectionModel) -> str:
        """
        Asynchronously create a collection.

        Parameters
        ----------
        collection : CollectionModel
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

        handle_response(response)

        return response.text

    def add_collection(self, collection: CollectionModel) -> str:
        if (
            collection is None
            or collection.name is None
            or collection.name.strip() == ""
        ):
            raise ValueError("collection name must be provided")

        response = self.client.post(
            "/collection/{collection.name}",
            json=collection.dict(exclude_none=True),
        )

        handle_response(response)

        return response.text

    # Document Collection APIs : Get a document collection
    async def aget_collection(self, name: str) -> CollectionModel:
        """
        Asynchronously gets a collection.

        Parameters
        ----------
        name : str
            The name of the collection to get.

        Returns
        -------
        CollectionModel
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

        handle_response(response)

        return CollectionModel(**response.json())

    def get_collection(self, name: str) -> CollectionModel:
        if name is None or name.strip() == "":
            raise ValueError("collection name must be provided")
        response = self.client.get(
            f"/collection/{name}",
        )

        handle_response(response)

        return CollectionModel(**response.json())

    # Document Collection APIs : List the documetns in a document collection
    async def alist_collections(self) -> List[CollectionModel]:
        """
        Asynchronously gets all collections.

        Returns
        -------
        List[CollectionModel]
            The list of document collection objects.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        response = await self.aclient.get(
            "/collection",
        )

        handle_response(response)
        return [CollectionModel(**collection) for collection in response.json()]

    def list_collections(self) -> List[CollectionModel]:
        response = self.client.get(
            "/collection",
        )

        handle_response(response)
        return [CollectionModel(**collection) for collection in response.json()]

    async def adelete_collection(self, collection_name: str) -> None:
        """
        Asynchronously delete collection.

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
        """
        if collection_name is None or collection_name.strip() == "":
            raise ValueError("collection name must be provided")

        response = await self.aclient.delete(
            f"/collection/{collection_name}",
        )

        handle_response(response)

    def delete_collection(self, collection_name: str) -> None:
        if collection_name is None or collection_name.strip() == "":
            raise ValueError("collection name must be provided")

        response = self.client.delete(
            f"/collection/{collection_name}",
        )

        handle_response(response)
