from __future__ import annotations

from types import TracebackType
from typing import Any, Dict, List, Optional, Type
from urllib.parse import urljoin

import httpx

from zep_python.exceptions import APIError
from zep_python.document_client import DocumentClient
from zep_python.memory_client import MemoryClient
from zep_python.models import (
    Memory,
    MemorySearchPayload,
    MemorySearchResult,
    Session,
    DocumentCollection,
    Document,
)

API_BASE_PATH = "/api/v1"
API_TIMEOUT = 10


class ZepClient:
    """
    ZepClient class implementation. This is a facade for memory and document APIs.

    Attributes
    ----------
    base_url : str
        The base URL of the API.
    memory_client : zep_memory_api
        The client used for making Memory API requests.
    document_client : zep_documents_api
        The client used for making Document API requests.

    Methods
    -------
    get_memory(session_id: str, lastn: Optional[int] = None) -> List[Memory]:
        Retrieve memory for the specified session.
    add_memory(session_id: str, memory_messages: Memory) -> str:
        Add memory to the specified session.
    delete_memory(session_id: str) -> str:
        Delete memory for the specified session.
    search_memory(session_id: str, search_payload: SearchPayload,
                  limit: Optional[int] = None) -> List[SearchResult]:
        Search memory for the specified session.
    close() -> None:
        Close the HTTP client.
    """

    base_url: str
    memory_client: MemoryClient
    document_client: DocumentClient

    def __init__(self, base_url: str, api_key: Optional[str] = None) -> None:
        """
        Initialize the ZepClient with the specified base URL.

        Parameters
        ----------
        base_url : str
            The base URL of the API.

        api_key : Optional[str]
            The API key to use for authentication. (optional)
        """

        headers: Dict[str, str] = {}
        if api_key is not None:
            headers["Authorization"] = f"Bearer {api_key}"

        self.base_url = concat_url(base_url, API_BASE_PATH)
        self.aclient = httpx.AsyncClient(
            base_url=self.base_url, headers=headers, timeout=API_TIMEOUT
        )
        self.client = httpx.Client(
            base_url=self.base_url, headers=headers, timeout=API_TIMEOUT
        )

        self._healthcheck(base_url)

        self.memory_client = MemoryClient(self.aclient, self.client)
        self.document_client = DocumentClient(self.aclient)

    async def __aenter__(self) -> "ZepClient":
        """Asynchronous context manager entry point"""
        return self

    async def __aexit__(
        self,
        exc_type: Type[Exception],
        exc_val: Exception,
        exc_tb: TracebackType,
    ) -> None:
        """Asynchronous context manager exit point"""
        await self.aclose()

    def __enter__(self) -> "ZepClient":
        """Sync context manager entry point"""
        return self

    def __exit__(
        self,
        exc_type: Type[Exception],
        exc_val: Exception,
        exc_tb: TracebackType,
    ) -> None:
        """Sync context manager exit point"""
        self.close()

    def _healthcheck(self, base_url: str) -> None:
        """
        Check that the Zep server is running and the API URL is correct.

        Raises
        ------
        ConnectionError
            If the server is not running or the API URL is incorrect.
        """

        url = concat_url(base_url, "/healthz")

        error_msg = """Failed to connect to Zep server. Please check that:
         - the server is running 
         - the API URL is correct
         - No other process is using the same port"""

        try:
            response = httpx.get(url)

            self._handle_response(response, error_msg)

            if response.status_code == 200 and response.text != ".":
                raise APIError(response, error_msg)

        except (httpx.ConnectError, httpx.NetworkError, httpx.TimeoutException) as e:
            raise APIError(None, error_msg) from e

    # Facade methods for Memory API
    def get_session(self, session_id: str) -> Session:
        return self.memory_client.get_session(session_id)

    async def aget_session(self, session_id: str) -> Session:
        return await self.memory_client.aget_session(session_id)

    def add_session(self, session: Session) -> str:
        return self.memory_client.add_session(session)

    async def aadd_session(self, session: Session) -> str:
        return await self.memory_client.aadd_session(session)

    def get_memory(self, session_id: str, lastn: Optional[int] = None) -> Memory:
        return self.memory_client.get_memory(session_id, lastn)

    async def aget_memory(self, session_id: str, lastn: Optional[int] = None) -> Memory:
        return await self.memory_client.aget_memory(session_id, lastn)

    def add_memory(self, session_id: str, memory_messages: Memory) -> str:
        return self.memory_client.add_memory(session_id, memory_messages)

    async def aadd_memory(self, session_id: str, memory_messages: Memory) -> str:
        return await self.memory_client.aadd_memory(session_id, memory_messages)

    def delete_memory(self, session_id: str) -> str:
        return self.memory_client.delete_memory(session_id)

    async def adelete_memory(self, session_id: str) -> str:
        return await self.memory_client.adelete_memory(session_id)

    def search_memory(
        self,
        session_id: str,
        search_payload: MemorySearchPayload,
        limit: Optional[int] = None,
    ) -> List[MemorySearchResult]:
        return self.memory_client.search_memory(session_id, search_payload, limit)

    async def asearch_memory(
        self,
        session_id: str,
        search_payload: MemorySearchPayload,
        limit: Optional[int] = None,
    ) -> List[MemorySearchResult]:
        return await self.memory_client.asearch_memory(
            session_id, search_payload, limit
        )

    # Facade methods for Document Collection APIs
    async def get_collection(self, collection_id: str) -> DocumentCollection:
        return await self.document_client.get_documentcollection(collection_id)

    async def add_collection(self, collection: DocumentCollection) -> str:
        return await self.document_client.add_documentcollection(collection)

    async def update_collection(self, collection: DocumentCollection) -> str:
        return await self.document_client.update_documentcollection(collection)

    async def delete_collection(self, collection_id: str) -> str:
        return await self.document_client.delete_documentcollection(collection_id)

    async def list_collections(self) -> List[DocumentCollection]:
        return await self.document_client.list_documentcollections()

    # Facade methods for Document APIs
    async def get_document(self, collection_id: str, document_id: str) -> Document:
        return await self.document_client.get_document(collection_id, document_id)

    async def add_document(
        self, collection_id: str, documents: List[Document]
    ) -> List[str]:
        return await self.document_client.add_document(collection_id, documents)

    async def update_document(self, collection_id: str, document: Document) -> str:
        return await self.document_client.update_document(collection_id, document)

    async def delete_document(self, collection_id: str, document_id: str) -> str:
        return await self.document_client.delete_document(collection_id, document_id)

    # async def list_documents(self, collection_id: str) -> List[Document]:

    # Facade methods for Document Bulk APIs
    async def batchupdate_documents(
        self, collection_id: str, documents: List[Document]
    ) -> str:
        return await self.document_client.batchupdate_documents(
            collection_id, documents
        )

    async def batchdelete_documents(
        self, collection_id: str, document_ids: List[str]
    ) -> str:
        return await self.document_client.batchdelete_documents(
            collection_id, document_ids
        )

    async def batchget_documents_byid(
        self, collection_id: str, document_ids: Dict[str, List[str]]
    ) -> List[Document]:
        return await self.document_client.batchget_documents(
            collection_id, document_ids
        )

    async def batchget_documents_byuuid(
        self,
        collection_id: str,
        document_uuids: Dict[str, List[str]],
    ) -> List[Document]:
        return await self.document_client.batchget_documents(
            collection_id, document_uuids
        )

    # Close the HTTP client
    async def aclose(self) -> None:
        """
        Asynchronously close the HTTP client.

        [Optional] This method may be called when the ZepClient is no longer needed to
        release resources.
        """
        await self.aclient.aclose()

    def close(self) -> None:
        """
        Close the HTTP client.

        [Optional] This method may be called when the ZepClient is no longer needed to
        release resources.
        """
        self.client.close()


def concat_url(base_url: str, path: str) -> str:
    """
    Join the specified base URL and path.

    Parameters
    ----------
    base_url : str
        The base URL to join.
    path : str
        The path to join.

    Returns
    -------
    str
        The joined URL.
    """
    return urljoin(base_url + "/", path.lstrip("/"))
