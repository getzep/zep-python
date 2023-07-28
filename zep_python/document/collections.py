import warnings
from typing import Any, Dict, List
from uuid import UUID

import httpx

from zep_python.exceptions import handle_response

from .models import CollectionModel, Document

LARGE_BATCH_WARNING_LIMIT = 1000
LARGE_BATCH_WARNING = (
    f"Batch size is greater than {LARGE_BATCH_WARNING_LIMIT}. "
    "This may result in slow performance or out-of-memory failures."
)


class Collection(CollectionModel):
    __doc__ = CollectionModel.__doc__

    aclient: httpx.AsyncClient
    client: httpx.Client

    # TODO: What should updates return?
    async def aupdate(self) -> str:
        """
        Asynchronously update collection.

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

        response = await self.aclient.patch(
            f"/collection/{self.name}",
            json=self.dict(exclude_none=True),
        )

        handle_response(response)

        return response.text

    def update(self) -> str:
        response = self.client.patch(
            f"/collection/{self.name}",
            json=self.dict(exclude_none=True),
        )

        handle_response(response)

        return response.text

    async def aadd_documents(self, documents: List[Document]) -> List[UUID]:
        """
        Asynchronously create documents.


        documents : List[DocumentModel]
            A list of Document objects representing the documents to be create.

        Returns
        -------
        UUID
            The UUIDs of the created documents.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """

        if documents is None:
            raise ValueError("document list must be provided")

        documents_dicts = [document.dict(exclude_none=True) for document in documents]

        response = await self.aclient.post(
            f"/collection/{self.name}/document",
            json=documents_dicts,
        )

        handle_response(response)

        uuids = [UUID(uuid) for uuid in response.json()]

        return uuids

    def add_document(self, documents: List[Document]) -> List[UUID]:
        if documents is None:
            raise ValueError("document list must be provided")

        documents_dicts = [document.dict(exclude_none=True) for document in documents]

        response = self.client.post(
            f"/collection/{self.name}/document",
            json=documents_dicts,
        )

        handle_response(response)

        uuids = [UUID(uuid) for uuid in response.json()]

        return uuids

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
        if document is None or document.uuid is None:
            raise ValueError("document uuid must be provided")

        response = await self.aclient.patch(
            f"/collection/{self.name}/document/uuid/{document.uuid}",
            json=document.dict(exclude_none=True),
        )

        handle_response(response)

    def update_document(self, document: Document):
        if document is None or document.uuid is None:
            raise ValueError("document uuid must be provided")

        response = self.client.patch(
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

        if document_uuid is None == "":
            raise ValueError("document uuid must be provided")

        response = await self.aclient.delete(
            f"/collection/{self.name}/document/uuid/{document_uuid}",
        )

        handle_response(response)

    def delete_document(self, document_uuid: UUID) -> None:
        if document_uuid is None:
            raise ValueError("document uuid must be provided")

        response = self.client.delete(
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

        if document_uuid is None:
            raise ValueError("document uuid must be provided")

        response = await self.aclient.get(
            f"/collection/{self.name}/document/uuid/{document_uuid}",
        )

        handle_response(response)

        return Document(**response.json())

    def get_document(self, document_uuid: UUID) -> Document:
        if document_uuid is None:
            raise ValueError("document uuid must be provided")

        response = self.client.get(
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

        if documents is None:
            raise ValueError("document list must be provided")

        if len(documents) > LARGE_BATCH_WARNING_LIMIT:
            warnings.warn(LARGE_BATCH_WARNING, stacklevel=2)

        documents_dicts = [document.dict(exclude_none=True) for document in documents]

        response = await self.aclient.patch(
            f"/collection/{self.name}/document/batchUpdate",
            json=documents_dicts,
        )

        handle_response(response)

    def batch_update_documents(self, documents: List[Document]) -> None:
        if documents is None:
            raise ValueError("document list must be provided")

        if len(documents) > LARGE_BATCH_WARNING_LIMIT:
            warnings.warn(LARGE_BATCH_WARNING, stacklevel=2)

        documents_dicts = [document.dict(exclude_none=True) for document in documents]

        response = self.client.patch(
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
        if document_uuids is None:
            raise ValueError("document uuid list must be provided")

        if len(document_uuids) > LARGE_BATCH_WARNING_LIMIT:
            warnings.warn(LARGE_BATCH_WARNING, stacklevel=2)

        response = await self.aclient.post(
            f"/collection/{self.name}/document/batchDelete",
            json=document_uuids,
        )

        handle_response(response)

    def batch_delete_documents(self, document_uuids: List[UUID]) -> None:
        if document_uuids is None:
            raise ValueError("document uuid list must be provided")

        if len(document_uuids) > LARGE_BATCH_WARNING_LIMIT:
            warnings.warn(LARGE_BATCH_WARNING, stacklevel=2)

        # Limit the number of documents fetched
        document_uuids = document_uuids[:LARGE_BATCH_WARNING_LIMIT]

        response = self.client.post(
            f"/collection/{self.name}/document/batchDelete",
            json=document_uuids,
        )

        handle_response(response)

    # TODO: Fix this
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

        if not document_ids:
            raise ValueError("document identifiers must be provided")

        for key, identifiers in document_ids.items():
            if len(identifiers) > LARGE_BATCH_WARNING_LIMIT:
                warnings.warn(LARGE_BATCH_WARNING, stacklevel=2)

        response = await self.aclient.post(
            f"/collection/{self.name}/document/batchGet",
            json=document_ids,
        )

        handle_response(response)

        return [Document(**document) for document in response.json()]

    def batch_get_documents(self, document_ids: Dict[str, List[str]]) -> List[Document]:
        if not document_ids:
            raise ValueError("document identifiers must be provided")

        for key, identifiers in document_ids.items():
            if len(identifiers) > LARGE_BATCH_WARNING_LIMIT:
                warnings.warn(LARGE_BATCH_WARNING, stacklevel=2)

        response = self.client.post(
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

        response = self.client.post(
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

        url = f"/api/v1/collection/{self.name}/search"
        params = {"limit": limit} if limit is not None and limit > 0 else {}

        response = await self.aclient.post(
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

        url = f"/api/v1/collection/{self.name}/search"
        params = {"limit": limit} if limit is not None and limit > 0 else {}

        response = self.client.post(
            url,
            params=params,
            json={"text": search_text, "metadata": metadata},
        )

        handle_response(response)

        return [Document(**document) for document in response.json()]
