from __future__ import annotations

import urllib.parse
from typing import Any, Dict, List, Optional

import httpx

from zep_python.exceptions import handle_response
from zep_python.utils import filter_dict

from .collections import DocumentCollection

DEFAULT_EMBEDDING_DIMENSIONS = 1024


class DocumentClient:
    """
    This class implements Zep's document APIs.

    Attributes:
        client (httpx.Client): Synchronous API client.
        aclient (httpx.AsyncClient): Asynchronous API client.

    Methods:
        aadd_collection(name: str,
                    description: Optional[str] = "",
                    metadata: Optional[Dict[str, Any]] = None) -> DocumentCollection:
            Asynchronously creates a collection.

        add_collection(name: str,
                       description: Optional[str] = "",
                       metadata: Optional[Dict[str, Any]] = None) -> DocumentCollection:
            Synchronously creates a collection.

        aupdate_collection(name: str, description: Optional[str] = "",
                           metadata: Optional[Dict[str, Any]] = None
                           ) -> DocumentCollection:
            Asynchronously updates a collection.

        update(name: str, description: Optional[str] = "",
               metadata: Optional[Dict[str, Any]] = None) -> DocumentCollection:
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
        self,
        name: str,
        description: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> DocumentCollection:
        """
        Asynchronously creates a collection.

        Parameters
        ----------
        name : str
            The name of the collection to be created.
        description: str
            The description of the collection to be created.
        metadata : Optional[Dict[str, Any]], optional
            A dictionary of metadata to be associated with the collection,
            by default None.

        Returns
        -------
        DocumentCollection
            The newly created collection object, retrieved from the server.

        Raises
        ------
        APIError
            If the API response format is unexpected, or if the server returns an error.
        """

        collection = DocumentCollection(
            name=name,
            description=description,
            embedding_dimensions=DEFAULT_EMBEDDING_DIMENSIONS,
            metadata=metadata,
            is_auto_embedded=True,
        )

        response = await self.aclient.post(
            f"/collections/{urllib.parse.quote_plus(name)}",
            json=collection.model_dump(exclude_none=True, exclude_unset=True),
        )

        handle_response(response)

        return await self.aget_collection(collection.name)

    def add_collection(
        self,
        name: str,
        description: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> DocumentCollection:
        """
        Creates a collection.

        Parameters
        ----------
        name : str
            The name of the collection to be created.
        description: str
            The description of the collection to be created.
        metadata : Optional[Dict[str, Any]], optional
            A dictionary of metadata to be associated with the collection,
            by default None.

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

        collection = DocumentCollection(
            name=name,
            description=description,
            embedding_dimensions=DEFAULT_EMBEDDING_DIMENSIONS,
            metadata=metadata,
            is_auto_embedded=True,
        )

        response = self.client.post(
            f"/collections/{urllib.parse.quote_plus(name)}",
            json=collection.model_dump(exclude_none=True, exclude_unset=True),
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
            f"/collections/{urllib.parse.quote_plus(name)}",
        )

        handle_response(response)

        filtered_response = filter_dict(response.json())

        return DocumentCollection(
            client=self.client, aclient=self.aclient, **filtered_response
        )

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
            f"/collections/{urllib.parse.quote_plus(name)}",
        )

        handle_response(response)

        filtered_response = filter_dict(response.json())

        return DocumentCollection(
            client=self.client, aclient=self.aclient, **filtered_response
        )

    async def aupdate_collection(
        self,
        name: str,
        description: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> DocumentCollection:
        """
        Asynchronously updates a collection.

        Parameters
        ----------
        name : str
            Collection name.
        description: Optional[str], optional
            Collection description.
        metadata : Optional[Dict[str, Any]], optional
            A dictionary of metadata to be associated with the collection.

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

        collection = DocumentCollection(
            name=name,
            description=description,
            metadata=metadata,
        )

        response = await self.aclient.patch(
            f"/collections/{urllib.parse.quote_plus(collection.name)}",
            json=collection.model_dump(exclude_none=True, exclude_unset=True),
        )

        handle_response(response)

        return await self.aget_collection(collection.name)

    def update_collection(
        self,
        name: str,
        description: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> DocumentCollection:
        """
        Updates a collection.

        Parameters
        ----------
        name : str
            Collection name.
        description: Optional[str], optional
            Collection description.
        metadata : Optional[Dict[str, Any]], optional
            A dictionary of metadata to be associated with the collection.

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

        collection = DocumentCollection(
            name=name,
            description=description,
            metadata=metadata,
        )

        response = self.client.patch(
            f"/collections/{urllib.parse.quote_plus(collection.name)}",
            json=collection.model_dump(exclude_none=True, exclude_unset=True),
        )

        handle_response(response)

        return self.get_collection(collection.name)

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
            "/collections",
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
            "/collections",
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
            f"/collections/{urllib.parse.quote_plus(collection_name)}",
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
            f"/collections/{urllib.parse.quote_plus(collection_name)}",
        )

        handle_response(response)
