import warnings
from typing import TYPE_CHECKING, Any, Dict, Generator, List, Optional, Tuple

import httpx

if TYPE_CHECKING:
    from pydantic import PrivateAttr
else:
    try:
        from pydantic.v1 import PrivateAttr
    except ImportError:
        from pydantic import PrivateAttr

from zep_python.exceptions import handle_response
from zep_python.utils import SearchType, filter_dict

from .models import Document, DocumentCollectionModel, DocumentSearchPayload

MIN_DOCS_TO_INDEX = 10_000
DEFAULT_BATCH_SIZE = 500
LARGE_BATCH_WARNING_LIMIT = 1000
LARGE_BATCH_WARNING = (
    f"Batch size is greater than {LARGE_BATCH_WARNING_LIMIT}. "
    "This may result in slow performance or out-of-memory failures."
)


def generate_batches(
    documents: List[Document], batch_size: int
) -> Generator[List[Dict[str, Any]], None, None]:
    """Generate batches of documents to be sent to the API."""

    document_dicts = (doc.dict(exclude_none=True) for doc in documents)
    batches = (
        [
            doc
            for doc in (next(document_dicts, None) for _ in range(batch_size))
            if doc is not None
        ]
        for _ in range(0, len(documents), batch_size)
    )
    return batches


class DocumentCollection(DocumentCollectionModel):
    __doc__ = DocumentCollectionModel.__doc__ or ""

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

    async def aadd_documents(
        self,
        documents: List[Document],
        batch_size: int = DEFAULT_BATCH_SIZE,
    ) -> List[str]:
        """
        Asynchronously create documents.


        documents : List[Document]
            A list of Document objects representing the documents to create.
        batch_size : int, optional
            The number of documents to upload in each batch. Defaults to 500.

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

        uuids: List[str] = []
        for batch in generate_batches(documents, batch_size):
            response = await self._aclient.post(
                f"/collection/{self.name}/document",
                json=batch,
            )

            handle_response(response)

            uuids.extend(response.json())

        return uuids

    def add_documents(
        self,
        documents: List[Document],
        batch_size: int = DEFAULT_BATCH_SIZE,
    ) -> List[str]:
        """
        Create documents.


        documents : List[Document]
            A list of Document objects representing the documents to create.

        Returns
        -------
        List[str]
            The UUIDs of the created documents.
        batch_size : int, optional
            The number of documents to upload in each batch. Defaults to 500.

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

        uuids: List[str] = []
        for batch in generate_batches(documents, batch_size):
            response = self._client.post(
                f"/collection/{self.name}/document",
                json=batch,
            )

            handle_response(response)

            uuids.extend(response.json())

        return uuids

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
        search_type: Optional[str] = None,
        mmr_lambda: Optional[float] = None,
    ) -> Tuple[List[Document], List[float]]:
        if not self._aclient:
            raise ValueError(
                "Can only search documents once a collection has been retrieved"
            )

        if text is None and embedding is None and metadata is None:
            raise ValueError("One of text, embedding, or metadata must be provided.")

        if text is not None and not isinstance(text, str):
            raise ValueError("Text must be a string.")

        search_type_value = SearchType(search_type or "similarity")

        payload = DocumentSearchPayload(
            text=text,
            embedding=embedding,
            metadata=metadata,
            search_type=search_type_value,
            mmr_lambda=mmr_lambda,
        )

        url = f"/collection/{self.name}/search"
        params = {"limit": limit} if limit is not None and limit > 0 else {}

        response = await self._aclient.post(
            url,
            params=params,
            json=payload.dict(exclude_none=True),
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
        search_type: Optional[str] = None,
        mmr_lambda: Optional[float] = None,
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
        search_type : Optional[str], optional
            The type of search to perform. Defaults to "similarity".
            Must be one of "similarity" or "mmr".
        mmr_lambda : Optional[float], optional
            The lambda parameter for the MMR Reranking Algorithm.

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
            text=text,
            embedding=embedding,
            metadata=metadata,
            limit=limit,
            search_type=search_type,
            mmr_lambda=mmr_lambda,
        )

        return results

    def search_return_query_vector(
        self,
        text: Optional[str] = None,
        embedding: Optional[List[float]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        limit: Optional[int] = None,
        search_type: Optional[str] = None,
        mmr_lambda: Optional[float] = None,
    ) -> Tuple[List[Document], List[float]]:
        if not self._client:
            raise ValueError(
                "Can only search documents once a collection has been retrieved"
            )

        if text is None and embedding is None and metadata is None:
            raise ValueError("One of text, embedding, or metadata must be provided.")

        if text is not None and not isinstance(text, str):
            raise ValueError("Text must be a string.")

        search_type_value = SearchType(search_type or "similarity")

        payload = DocumentSearchPayload(
            text=text,
            embedding=embedding,
            metadata=metadata,
            search_type=search_type_value,
            mmr_lambda=mmr_lambda,
        )

        url = f"/collection/{self.name}/search"
        params = {"limit": limit} if limit is not None and limit > 0 else {}

        response = self._client.post(
            url,
            params=params,
            json=payload.dict(exclude_none=True),
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
        search_type: Optional[str] = None,
        mmr_lambda: Optional[float] = None,
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
        search_type : Optional[str], optional
            The type of search to perform. Defaults to "similarity".
            Must be one of "similarity" or "mmr".
        mmr_lambda : Optional[float], optional
            The lambda parameter for the MMR Reranking Algorithm.

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
            text=text,
            embedding=embedding,
            metadata=metadata,
            limit=limit,
            search_type=search_type,
            mmr_lambda=mmr_lambda,
        )

        return results
