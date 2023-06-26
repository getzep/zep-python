from __future__ import annotations

from types import TracebackType
from typing import Any, Dict, List, Optional, Type

import httpx

from zep_python.exceptions import APIError, AuthError, NotFoundError
from zep_python.models import (
    Memory,
    MemorySearchPayload,
    MemorySearchResult,
    Message,
    Summary,
)

API_BASE_PATH = "/api/v1"


class ZepClient:
    """
    ZepClient class implementation.

    Attributes
    ----------
    base_url : str
        The base URL of the API.
    client : httpx.AsyncClient
        The HTTP client used for making API requests.

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

        self.base_url = f"{base_url}{API_BASE_PATH}"
        self.aclient = httpx.AsyncClient(base_url=self.base_url, headers=headers)
        self.client = httpx.Client(base_url=self.base_url, headers=headers)

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

    def _handle_response(
        self, response: httpx.Response, missing_message: Optional[str] = None
    ) -> None:
        missing_message = missing_message or "No query results found"
        if response.status_code == 404:
            raise NotFoundError(missing_message)

        if response.status_code == 401:
            raise AuthError(response)

        if response.status_code != 200:
            raise APIError(response)

    def _parse_get_memory_response(self, response_data: Any) -> Memory:
        """Parse the response from the get_memory API call."""
        messages: List[Message]
        try:
            messages = [
                Message.parse_obj(m) for m in response_data.get("messages", None)
            ]
            if len(messages) == 0:
                raise ValueError("Messages can't be empty")
        except (TypeError, ValueError) as e:
            raise APIError(message="Unexpected response format from the API") from e

        summary: Optional[Summary] = None
        if response_data.get("summary", None) is not None:
            summary = Summary.parse_obj(response_data["summary"])

        memory = Memory(
            messages=messages,
            # Add the 'summary' field if it is present in the response.
            summary=summary,
            # Add any other fields from the response that are relevant to the
            # Memory class.
        )
        return memory

    def _gen_get_params(self, lastn: Optional[int] = None) -> Dict[str, Any]:
        params = {}
        if lastn is not None:
            params["lastn"] = lastn
        return params

    def get_memory(self, session_id: str, lastn: Optional[int] = None) -> Memory:
        """
        Retrieve memory for the specified session.

        Parameters
        ----------
        session_id : str
            The ID of the session for which to retrieve memory.
        lastn : Optional[int], optional
            The number of most recent memory entries to retrieve. Defaults to None (all
            entries).

        Returns
        -------
        Memory
            A memory object containing a Summary, metadata, and list of Messages.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """

        if session_id is None or session_id == "":
            raise ValueError("session_id must be provided")

        url = f"/sessions/{session_id}/memory"
        params = self._gen_get_params(lastn)
        response = self.client.get(url, params=params)

        self._handle_response(response, f"No memory found for session {session_id}")

        response_data = response.json()

        return self._parse_get_memory_response(response_data)

    async def aget_memory(self, session_id: str, lastn: Optional[int] = None) -> Memory:
        """
        Asynchronously retrieve memory for the specified session.

        Parameters
        ----------
        session_id : str
            The ID of the session for which to retrieve memory.
        lastn : Optional[int], optional
            The number of most recent memory entries to retrieve. Defaults to None (all
            entries).

        Returns
        -------
        Memory
            A memory object containing a Summary, metadata, and list of Messages.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if session_id is None or session_id == "":
            raise ValueError("session_id must be provided")

        url = f"/sessions/{session_id}/memory"
        params = self._gen_get_params(lastn)
        response = await self.aclient.get(url, params=params)

        self._handle_response(response, f"No memory found for session {session_id}")

        response_data = response.json()

        return self._parse_get_memory_response(response_data)

    def add_memory(self, session_id: str, memory_messages: Memory) -> str:
        """
        Add memory to the specified session.

        Parameters
        ----------
        session_id : str
            The ID of the session to which memory should be added.
        memory_messages : Memory
            A Memory object representing the memory messages to be added.

        Returns
        -------
        str
            The response text from the API.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if session_id is None or session_id == "":
            raise ValueError("session_id must be provided")

        response = self.client.post(
            f"/sessions/{session_id}/memory",
            json=memory_messages.dict(exclude_none=True),
        )

        self._handle_response(response)

        return response.text

    async def aadd_memory(self, session_id: str, memory_messages: Memory) -> str:
        """
        Asynchronously add memory to the specified session.

        Parameters
        ----------
        session_id : str
            The ID of the session to which memory should be added.
        memory_messages : Memory
            A Memory object representing the memory messages to be added.

        Returns
        -------
        str
            The response text from the API.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if session_id is None or session_id == "":
            raise ValueError("session_id must be provided")

        response = await self.aclient.post(
            f"/sessions/{session_id}/memory",
            json=memory_messages.dict(exclude_none=True),
        )

        self._handle_response(response)

        return response.text

    def delete_memory(self, session_id: str) -> str:
        """
        Delete memory for the specified session.

        Parameters
        ----------
        session_id : str
            The ID of the session for which memory should be deleted.

        Returns
        -------
        str
            The response text from the API.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if session_id is None or session_id == "":
            raise ValueError("session_id must be provided")

        response = self.client.delete(f"/sessions/{session_id}/memory")
        self._handle_response(response)
        return response.text

    async def adelete_memory(self, session_id: str) -> str:
        """
        Asynchronously delete memory for the specified session.

        Parameters
        ----------
        session_id : str
            The ID of the session for which memory should be deleted.

        Returns
        -------
        str
            The response text from the API.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if session_id is None or session_id == "":
            raise ValueError("session_id must be provided")

        response = await self.aclient.delete(f"/sessions/{session_id}/memory")
        self._handle_response(response)
        return response.text

    def search_memory(
        self,
        session_id: str,
        search_payload: MemorySearchPayload,
        limit: Optional[int] = None,
    ) -> List[MemorySearchResult]:
        """
        Search memory for the specified session.

        Parameters
        ----------
        session_id : str
            The ID of the session for which memory should be searched.
        search_payload : MemorySearchPayload
            A SearchPayload object representing the search query.
        limit : Optional[int], optional
            The maximum number of search results to return. Defaults to None (no limit).

        Returns
        -------
        List[MemorySearchResult]
            A list of SearchResult objects representing the search results.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if session_id is None or session_id == "":
            raise ValueError("session_id must be provided")

        if search_payload is None:
            raise ValueError("search_payload must be provided")

        params = {"limit": limit} if limit is not None else {}
        response = self.client.post(
            f"/sessions/{session_id}/search",
            json=search_payload.dict(),
            params=params,
        )
        self._handle_response(response)
        return [
            MemorySearchResult(**search_result) for search_result in response.json()
        ]

    async def asearch_memory(
        self,
        session_id: str,
        search_payload: MemorySearchPayload,
        limit: Optional[int] = None,
    ) -> List[MemorySearchResult]:
        """
        Asynchronously search memory for the specified session.

        Parameters
        ----------
        session_id : str
            The ID of the session for which memory should be searched.
        search_payload : MemorySearchPayload
            A SearchPayload object representing the search query.
        limit : Optional[int], optional
            The maximum number of search results to return. Defaults to None (no limit).

        Returns
        -------
        List[MemorySearchResult]
            A list of SearchResult objects representing the search results.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if session_id is None or session_id == "":
            raise ValueError("session_id must be provided")

        if search_payload is None:
            raise ValueError("search_payload must be provided")

        params = {"limit": limit} if limit is not None else {}
        response = await self.aclient.post(
            f"/sessions/{session_id}/search",
            json=search_payload.dict(),
            params=params,
        )
        self._handle_response(response)
        return [
            MemorySearchResult(**search_result) for search_result in response.json()
        ]

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
