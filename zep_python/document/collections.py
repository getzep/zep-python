import warnings
from typing import Any, Dict, List, Optional
from uuid import UUID

import httpx
from pydantic import PrivateAttr

from zep_python.exceptions import handle_response

from .models import DocumentCollectionModel, Document

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

    async def aadd_documents(self, documents: List[Document]) -> List[UUID]:
        """
        Asynchronously create documents.


        documents : List[DocumentModel]
            A list of Document objects representing the documents to be create.

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

    async def aupdate_document(self, document: Document) -> None:
        """
        Asynchronously update document by UUID.

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
        if not self._aclient:
            raise ValueError(
                "Can only update documents once a collection has been retrieved or"
                " created"
            )

        if document is None or document.uuid is None:
            raise ValueError("document uuid must be provided")

        response = await self._aclient.patch(
            f"/collection/{self.name}/document/uuid/{document.uuid}",
            json=document.dict(exclude_none=True),
        )

        handle_response(response)

    def update_document(self, document: Document):
        if not self._client:
            raise ValueError(
                "Can only update documents once a collection has been retrieved or"
                " created"
            )

        if document is None or document.uuid is None:
            raise ValueError("document uuid must be provided")

        response = self._client.patch(
            f"/collection/{self.name}/document/uuid/{document.uuid}",
            json=document.dict(exclude_none=True),
        )

        handle_response(response)

    async def adelete_document(self, document_uuid: UUID) -> None:
        """
        Asynchronously delete document.

        Parameters
        ----------
        document_uuid: UUID
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

        if document_uuid is None == "":
            raise ValueError("document uuid must be provided")

        response = await self._aclient.delete(
            f"/collection/{self.name}/document/uuid/{document_uuid}",
        )

        handle_response(response)

    def delete_document(self, document_uuid: UUID) -> None:
        if not self._client:
            raise ValueError(
                "Can only delete a document once a collection has been retrieved"
            )

        if document_uuid is None:
            raise ValueError("document uuid must be provided")

        response = self._client.delete(
            f"/collection/{self.name}/document/uuid/{document_uuid}",
        )

        handle_response(response)

    async def aget_document(self, document_uuid: UUID) -> Document:
        """
        Asynchronously gets a document.

        Parameters
        ----------
        document_uuid: UUID
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

        if document_uuid is None:
            raise ValueError("document uuid must be provided")

        response = await self._aclient.get(
            f"/collection/{self.name}/document/uuid/{document_uuid}",
        )

        handle_response(response)

        return Document(**response.json())

    def get_document(self, document_uuid: UUID) -> Document:
        if not self._client:
            raise ValueError(
                "Can only get a document once a collection has been retrieved"
            )

        if document_uuid is None:
            raise ValueError("document uuid must be provided")

        response = self._client.get(
            f"/collection/{self.name}/document/uuid/{document_uuid}",
        )

        handle_response(response)

        return Document(**response.json())

    async def abatch_update_documents(self, documents: List[Document]) -> None:
        """
        Asynchronously batch update documents.

        Parameters
        ----------
        documents : List[Document]
            A list of Document objects representing the documents to be added
            or updated.

        Returns
        -------
        None

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if not self._aclient:
            raise ValueError(
                "Can only update documents once a collection has been retrieved"
            )

        if documents is None:
            raise ValueError("document list must be provided")

        if len(documents) > LARGE_BATCH_WARNING_LIMIT:
            warnings.warn(LARGE_BATCH_WARNING, stacklevel=2)

        documents_dicts = [document.dict(exclude_none=True) for document in documents]

        response = await self._aclient.patch(
            f"/collection/{self.name}/document/batchUpdate",
            json=documents_dicts,
        )

        handle_response(response)

    def batch_update_documents(self, documents: List[Document]) -> None:
        if not self._client:
            raise ValueError(
                "Can only update documents once a collection has been retrieved"
            )

        if documents is None:
            raise ValueError("document list must be provided")

        if len(documents) > LARGE_BATCH_WARNING_LIMIT:
            warnings.warn(LARGE_BATCH_WARNING, stacklevel=2)

        documents_dicts = [document.dict(exclude_none=True) for document in documents]

        response = self._client.patch(
            f"/collection/{self.name}/document/batchUpdate",
            json=documents_dicts,
        )

        handle_response(response)

    async def abatch_delete_documents(self, document_uuids: List[UUID]) -> None:
        """
        Asynchronously batch delete documents.

        Parameters
        ----------
        document_uuids : List[UUID]
            A list of document uuids to be deleted.

        Returns
        -------
        None

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if not self._aclient:
            raise ValueError(
                "Can only delete documents once a collection has been retrieved"
            )

        if document_uuids is None:
            raise ValueError("document uuid list must be provided")

        if len(document_uuids) > LARGE_BATCH_WARNING_LIMIT:
            warnings.warn(LARGE_BATCH_WARNING, stacklevel=2)

        response = await self._aclient.post(
            f"/collection/{self.name}/document/batchDelete",
            json=document_uuids,
        )

        handle_response(response)

    def batch_delete_documents(self, document_uuids: List[UUID]) -> None:
        if not self._client:
            raise ValueError(
                "Can only delete documents once a collection has been retrieved"
            )

        if document_uuids is None:
            raise ValueError("document uuid list must be provided")

        if len(document_uuids) > LARGE_BATCH_WARNING_LIMIT:
            warnings.warn(LARGE_BATCH_WARNING, stacklevel=2)

        # Limit the number of documents fetched
        document_uuids = document_uuids[:LARGE_BATCH_WARNING_LIMIT]

        response = self._client.post(
            f"/collection/{self.name}/document/batchDelete",
            json=document_uuids,
        )

        handle_response(response)

    async def abatch_get_documents(
        self, document_ids: Dict[str, List[str]]
    ) -> List[Document]:
        """
        Asynchronously batch gets documents.

        Parameters
        ----------
        document_ids : Dict[str, List[str]]
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
        if not self._aclient:
            raise ValueError(
                "Can only get documents once a collection has been retrieved"
            )

        if not document_ids:
            raise ValueError("document identifiers must be provided")

        for key, identifiers in document_ids.items():
            if len(identifiers) > LARGE_BATCH_WARNING_LIMIT:
                warnings.warn(LARGE_BATCH_WARNING, stacklevel=2)

        response = await self._aclient.post(
            f"/collection/{self.name}/document/batchGet",
            json=document_ids,
        )

        handle_response(response)

        return [Document(**document) for document in response.json()]

    def batch_get_documents(self, document_ids: Dict[str, List[str]]) -> List[Document]:
        if not self._client:
            raise ValueError(
                "Can only get documents once a collection has been retrieved"
            )

        if not document_ids:
            raise ValueError("document identifiers must be provided")

        for key, identifiers in document_ids.items():
            if len(identifiers) > LARGE_BATCH_WARNING_LIMIT:
                warnings.warn(LARGE_BATCH_WARNING, stacklevel=2)

        response = self._client.post(
            f"/collection/{self.name}/document/batchGet",
            json=document_ids,
        )

        handle_response(response)

        return [Document(**document) for document in response.json()]

    def create_collection_index(
        self,
    ) -> None:
        """
        Creates an index for a DocumentCollection.


        Returns
        -------
        None

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if not self._client:
            raise ValueError("Can only index a collection it has been retrieved")

        response = self._client.post(
            f"/api/v1/collection/{self.name}/index/create",
        )

        handle_response(response)

    async def asearch_documents(
        self, search_text: str, metadata: Dict[str, Any], limit: int
    ) -> List[Document]:
        """
        Async search over documents in a collection based on provided search criteria.

        Parameters
        ----------
        search_text : str
            The search text.
        metadata : Dict[str, Any]
            Document metadata to filter on.
        limit : int, optional
            Limit the number of returned documents.

        Returns
        -------
        List[Document]
            The response text from the API.

        Raises
        ------
        NotFoundError
            If the collection is not found.
        APIError
            If the API response format is unexpected or there's an error from the API.
        """
        if not self._aclient:
            raise ValueError(
                "Can only search documents once a collection has been retrieved"
            )

        url = f"/api/v1/collection/{self.name}/search"
        params = {"limit": limit} if limit is not None and limit > 0 else {}

        response = await self._aclient.post(
            url,
            params=params,
            json={"text": search_text, "metadata": metadata},
        )

        handle_response(response)

        return [Document(**document) for document in response.json()]

    def search_documents(
        self, search_text: str, metadata: Dict[str, Any], limit: int
    ) -> List[Document]:
        """
        Searches over documents in a collection based on provided search criteria.

        Parameters
        ----------
        search_text : str
            The search text.
        metadata : Dict[str, Any]
            Document metadata to filter on.
        limit : int, optional
            Limit the number of returned documents.

        Returns
        -------
        List[Document]
            The response text from the API.

        Raises
        ------
        NotFoundError
            If the collection is not found.
        APIError
            If the API response format is unexpected or there's an error from the API.
        """
        if not self._client:
            raise ValueError(
                "Can only search documents once a collection has been retrieved"
            )

        url = f"/api/v1/collection/{self.name}/search"
        params = {"limit": limit} if limit is not None and limit > 0 else {}

        response = self._client.post(
            url,
            params=params,
            json={"text": search_text, "metadata": metadata},
        )

        handle_response(response)

        return [Document(**document) for document in response.json()]
