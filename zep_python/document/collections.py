import warnings
from typing import Any, Dict, List, Optional
from uuid import UUID

import httpx
from pydantic import PrivateAttr

from zep_python.utils import filter_dict

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
        description: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        if not self._client:
            raise ValueError(
                "Can only update documents once a collection has been retrieved or"
                " created"
            )

        if uuid is None:
            raise ValueError("document uuid must be provided")

        if description is None and metadata is None:
            raise ValueError("description or metadata must be provided")

        payload = filter_dict({"description": description, "metadata": metadata})

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
        if not self._aclient:
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
        self,
        search_text: str,
        metadata: Optional[Dict[str, Any]] = None,
        limit: Optional[int] = None,
    ) -> List[Document]:
        """
        Async search over documents in a collection based on provided search criteria.

        Parameters
        ----------
        search_text : str
            The search text.
        metadata : Optional[Dict[str, Any]], optional
            Document metadata to filter on.
        limit : Optional[int], optional
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
        self,
        search_text: str,
        metadata: Optional[Dict[str, Any]] = None,
        limit: Optional[int] = None,
    ) -> List[Document]:
        """
        Searches over documents in a collection based on provided search criteria.

        Parameters
        ----------
        search_text : str
            The search text.
        metadata : Optional[Dict[str, Any]], optional
            Document metadata to filter on.
        limit : Optional[int], optional
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
