import warnings
from typing import Any, Dict, List, Optional, Tuple

import httpx
from pydantic import PrivateAttr

from zep_python.exceptions import handle_response
from zep_python.utils import filter_dict

from .models import Document, DocumentCollectionModel

MIN_DOCS_TO_INDEX = 10_000
LARGE_BATCH_WARNING_LIMIT = 1000
LARGE_BATCH_WARNING = (
    f"Batch size is greater than {LARGE_BATCH_WARNING_LIMIT}. "
    "This may result in slow performance or out-of-memory failures."
)


class DocumentCollection(DocumentCollectionModel):
    __doc__ = DocumentCollectionModel.__doc__

    _client: Optional[httpx.Client] = PrivateAttr(default=None)
    _aclient: Optional[httpx.AsyncClient] = PrivateAttr(default=None)

    def __init__(
        self,
        aclient: Optional[httpx.AsyncClient] = None,
        client: Optional[httpx.Client] = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self._aclient = aclient
        self._client = client

    @property
    def status(self) -> str:
        """
        Get the status of the collection.

        Returns
        -------
        str
            The status of the collection.

            `ready`: All documents have been embedded and the collection is ready for
            search.

            `pending`: The collection is still processing.
        """
        if self.document_count and (
            self.document_embedded_count == self.document_count
        ):
            return "ready"
        else:
            return "pending"

    async def aadd_documents(self, documents: List[Document]) -> List[str]:
        """
        Asynchronously create documents.


        documents : List[Document]
            A list of Document objects representing the documents to create.

        Returns
        -------
        List[str]
            The UUIDs of the created documents.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """

        if not self._aclient:
            raise ValueError(
                "Can only add documents once a collection has been created"
            )

        if documents is None:
            raise ValueError("document list must be provided")

        documents_dicts = [document.dict(exclude_none=True) for document in documents]

        response = await self._aclient.post(
            f"/collection/{self.name}/document",
            json=documents_dicts,
        )

        handle_response(response)

        return response.json()

    def add_documents(self, documents: List[Document]) -> List[str]:
        """
        Create documents.


        documents : List[Document]
            A list of Document objects representing the documents to create.

        Returns
        -------
        List[str]
            The UUIDs of the created documents.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if not self._client:
            raise ValueError(
                "Can only add documents once a collection has been created"
            )

        if documents is None:
            raise ValueError("document list must be provided")

        documents_dicts = [document.dict(exclude_none=True) for document in documents]

        response = self._client.post(
            f"/collection/{self.name}/document",
            json=documents_dicts,
        )

        handle_response(response)

        return response.json()

    async def aupdate_document(
        self,
        uuid: str,
        description: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Asynchronously update document by UUID.

        Parameters
        ----------
        uuid : str
            The UUID of the document to update.
        description : Optional[str]
            The description of the document.
        metadata : Optional[Dict[str, Any]]
            The metadata of the document.

        Returns
        -------
        None

        Raises
        ------
        NotFoundError
            If the document is not found.

        APIError
            If the API response format is unexpected.
        """
        if not self._aclient:
            raise ValueError(
                "Can only update documents once a collection has been retrieved or"
                " created"
            )

        if uuid is None:
            raise ValueError("document uuid must be provided")

        if description is None and metadata is None:
            raise ValueError("description or metadata must be provided")

        payload = filter_dict({"description": description, "metadata": metadata})

        response = await self._aclient.patch(
            f"/collection/{self.name}/document/uuid/{uuid}",
            json=payload,
        )

        handle_response(response)

    def update_document(
        self,
        uuid: str,
        document_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Update document by UUID.

        Parameters
        ----------
        uuid : str
            The UUID of the document to update.
        document_id : Optional[str]
            The document_id of the document.
        metadata : Optional[Dict[str, Any]]
            The metadata of the document.

        Returns
        -------
        None

        Raises
        ------
        NotFoundError
            If the document is not found.

        APIError
            If the API response format is unexpected.
        """
        if not self._client:
            raise ValueError(
                "Can only update documents once a collection has been retrieved or"
                " created"
            )

        if uuid is None:
            raise ValueError("document uuid must be provided")

        if document_id is None and metadata is None:
            raise ValueError("document_id or metadata must be provided")

        payload = filter_dict({"document_id": document_id, "metadata": metadata})

        response = self._client.patch(
            f"/collection/{self.name}/document/uuid/{uuid}",
            json=payload,
        )

        handle_response(response)

    async def adelete_document(self, uuid: str) -> None:
        """
        Asynchronously delete document.

        Parameters
        ----------
        uuid: str
            The uuid of the document to be deleted.

        Returns
        -------
        None

        Raises
        ------
        NotFoundError
            If the document is not found.

        APIError
            If the API response format is unexpected.
        """
        if not self._aclient:
            raise ValueError(
                "Can only delete a document once a collection has been retrieved"
            )

        if uuid is None or uuid.strip() == "":
            raise ValueError("document uuid must be provided")

        response = await self._aclient.delete(
            f"/collection/{self.name}/document/uuid/{uuid}",
        )

        handle_response(response)

    def delete_document(self, uuid: str) -> None:
        """
        Delete document.

        Parameters
        ----------
        uuid: str
            The uuid of the document to be deleted.

        Returns
        -------
        None

        Raises
        ------
        NotFoundError
            If the document is not found.

        APIError
            If the API response format is unexpected.
        """
        if not self._client:
            raise ValueError(
                "Can only delete a document once a collection has been retrieved"
            )

        if uuid is None or uuid.strip() == "":
            raise ValueError("document uuid must be provided")

        response = self._client.delete(
            f"/collection/{self.name}/document/uuid/{uuid}",
        )

        handle_response(response)

    async def aget_document(self, uuid: str) -> Document:
        """
        Asynchronously gets a document.

        Parameters
        ----------
        uuid: str
            The name of the document to get.

        Returns
        -------
        Document
            The retrieved document.

        Raises
        ------
        NotFoundError
            If the document is not found.

        APIError
            If the API response format is unexpected.
        """
        if not self._aclient:
            raise ValueError(
                "Can only get a document once a collection has been retrieved"
            )

        if uuid is None or uuid.strip() == "":
            raise ValueError("document uuid must be provided")

        response = await self._aclient.get(
            f"/collection/{self.name}/document/uuid/{uuid}",
        )

        handle_response(response)

        return Document(**response.json())

    def get_document(self, uuid: str) -> Document:
        """
        Gets a document.

        Parameters
        ----------
        uuid: str
            The name of the document to get.

        Returns
        -------
        Document
            The retrieved document.

        Raises
        ------
        NotFoundError
            If the document is not found.

        APIError
            If the API response format is unexpected.
        """
        if not self._client:
            raise ValueError(
                "Can only get a document once a collection has been retrieved"
            )

        if uuid is None or uuid.strip() == "":
            raise ValueError("document uuid must be provided")

        response = self._client.get(
            f"/collection/{self.name}/document/uuid/{uuid}",
        )

        handle_response(response)

        return Document(**response.json())

    async def aget_documents(self, uuids: List[str]) -> List[Document]:
        """
        Asynchronously gets a list of documents.

        Parameters
        ----------
        uuids: List[str]
            The list of document uuids to get.

        Returns
        -------
        List[Document]
            The list of document objects.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if not self._aclient:
            raise ValueError(
                "Can only get documents once a collection has been retrieved"
            )

        if not uuids or len(uuids) == 0:
            raise ValueError("document uuids must be provided")

        if len(uuids) > LARGE_BATCH_WARNING_LIMIT:
            warnings.warn(LARGE_BATCH_WARNING, stacklevel=2)

        response = await self._aclient.post(
            f"/collection/{self.name}/document/list/get",
            json={"uuids": uuids},
        )

        handle_response(response)

        return [Document(**document) for document in response.json()]

    def get_documents(self, uuids: List[str]) -> List[Document]:
        """
        Gets a list of documents.

        Parameters
        ----------
        uuids: List[str]
            The list of document uuids to get.

        Returns
        -------
        List[Document]
            The list of document objects.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if not self._client:
            raise ValueError(
                "Can only get documents once a collection has been retrieved"
            )

        if not uuids or len(uuids) == 0:
            raise ValueError("document uuids must be provided")

        if len(uuids) > LARGE_BATCH_WARNING_LIMIT:
            warnings.warn(LARGE_BATCH_WARNING, stacklevel=2)

        response = self._client.post(
            f"/collection/{self.name}/document/list/get",
            json={"uuids": uuids},
        )

        handle_response(response)

        return [Document(**document) for document in response.json()]

    def create_index(
        self,
        force: bool = False,
    ) -> None:
        """
        Creates an index for a DocumentCollection.

        Parameters
        ----------
        force : bool, optional
            If True, forces the creation of the index even if the number of documents
            is less than then minimum recommended for indexing. Defaults to False.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if not self._client:
            raise ValueError("Can only index a collection it has been retrieved")

        if (
            not force
            and self.document_count
            and (self.document_count <= MIN_DOCS_TO_INDEX)
        ):
            raise ValueError(
                f"Collection must have at least {MIN_DOCS_TO_INDEX} documents to be"
                " indexed. Please see the Zep documentation on index best practices."
                " Pass force=True to override."
            )

        params = filter_dict({"force": force})

        response = self._client.post(
            f"/collection/{self.name}/index/create",
            params=params,
        )

        handle_response(response)

    async def asearch_return_query_vector(
        self,
        text: Optional[str] = None,
        embedding: Optional[List[float]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        limit: Optional[int] = None,
    ) -> Tuple[List[Document], List[float]]:
        if not self._aclient:
            raise ValueError(
                "Can only search documents once a collection has been retrieved"
            )

        if text is None and embedding is None and metadata is None:
            raise ValueError("One of text, embedding, or metadata must be provided.")

        if text is not None and not isinstance(text, str):
            raise ValueError("Text must be a string.")

        url = f"/collection/{self.name}/search"
        params = {"limit": limit} if limit is not None and limit > 0 else {}

        response = await self._aclient.post(
            url,
            params=params,
            json={"text": text, "embedding": embedding, "metadata": metadata},
        )

        # If the collection is not found, return an empty list
        if response.status_code == 404:
            return [], []

        # Otherwise, handle the response for other errors
        handle_response(response)

        return (
            [Document(**document) for document in response.json()["results"]],
            response.json()["query_vector"],
        )

    async def asearch(
        self,
        text: Optional[str] = None,
        embedding: Optional[List[float]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        limit: Optional[int] = None,
    ) -> List[Document]:
        """
        Async search over documents in a collection based on provided search criteria.
        One of text, embedding, or metadata must be provided.

        Returns an empty list if no documents are found.

        Parameters
        ----------
        text : Optional[str], optional
            The search text.
        embedding : Optional[List[float]], optional
            The embedding vector to search for.
        metadata : Optional[Dict[str, Any]], optional
            Document metadata to filter on.
        limit : Optional[int], optional
            Limit the number of returned documents.

        Returns
        -------
        List[Document]
            The list of documents that match the search criteria.

        Raises
        ------
        APIError
            If the API response format is unexpected or there's an error from the API.
        """
        results, _ = await self.asearch_return_query_vector(
            text=text, embedding=embedding, metadata=metadata, limit=limit
        )

        return results

    def search_return_query_vector(
        self,
        text: Optional[str] = None,
        embedding: Optional[List[float]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        limit: Optional[int] = None,
    ) -> Tuple[List[Document], List[float]]:
        if not self._client:
            raise ValueError(
                "Can only search documents once a collection has been retrieved"
            )

        if text is None and embedding is None and metadata is None:
            raise ValueError("One of text, embedding, or metadata must be provided.")

        if text is not None and not isinstance(text, str):
            raise ValueError("Text must be a string.")

        url = f"/collection/{self.name}/search"
        params = {"limit": limit} if limit is not None and limit > 0 else {}

        response = self._client.post(
            url,
            params=params,
            json={"text": text, "embedding": embedding, "metadata": metadata},
        )

        # If the collection is not found, return an empty list
        if response.status_code == 404:
            return [], []

        # Otherwise, handle the response for other errors
        handle_response(response)

        return (
            [Document(**document) for document in response.json()["results"]],
            response.json()["query_vector"],
        )

    def search(
        self,
        text: Optional[str] = None,
        embedding: Optional[List[float]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        limit: Optional[int] = None,
    ) -> List[Document]:
        """
        Searches over documents in a collection based on provided search criteria.
        One of text, embedding, or metadata must be provided.

        Returns an empty list if no documents are found.

        Parameters
        ----------
        text : Optional[str], optional
            The search text.
        embedding : Optional[List[float]], optional
            The embedding vector to search for.
        metadata : Optional[Dict[str, Any]], optional
            Document metadata to filter on.
        limit : Optional[int], optional
            Limit the number of returned documents.

        Returns
        -------
        List[Document]
            The list of documents that match the search criteria.

        Raises
        ------
        APIError
            If the API response format is unexpected or there's an error from the API.
        """
        results, _ = self.search_return_query_vector(
            text=text, embedding=embedding, metadata=metadata, limit=limit
        )

        return results
