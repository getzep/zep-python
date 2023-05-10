from __future__ import annotations

from types import TracebackType
from typing import List, Optional, Type

import httpx

from zep_python.exceptions import APIError, NotFoundError
from zep_python.models import Memory, SearchPayload, SearchResult
from zep_python.utils import sync

API_BASEURL = "/api/v1"


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

    def __init__(self, base_url: str) -> None:
        """
        Initialize the ZepClient with the specified base URL.

        Parameters
        ----------
        base_url : str
            The base URL of the API.
        """
        self.base_url = base_url
        self.client = httpx.AsyncClient()

    # Asynchronous context manager entry point
    async def __aenter__(self) -> "ZepClient":
        return self

    # Asynchronous context manager exit point
    async def __aexit__(
        self,
        exc_type: Type[Exception],
        exc_val: Exception,
        exc_tb: TracebackType,
    ) -> None:
        await self.close()

    @sync
    def get_memory(
        self, session_id: str, lastn: Optional[int] = None
    ) -> List[Memory]:
        """
        Retrieve memory for the specified session. This method is a synchronous wrapper
        for the asynchronous method `aget_memory`.

        Parameters
        ----------
        session_id : str
            The ID of the session for which to retrieve memory.
        lastn : Optional[int], optional
            The number of most recent memory entries to retrieve. Defaults to None (all
            entries).

        Returns
        -------
        List[Memory]
            A list of Memory objects representing the retrieved memory entries.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        # we've wrapped the function in a decorator that will run it synchronously.
        # ignore the type error.
        return self.aget_memory(session_id, lastn)  # type: ignore

    async def aget_memory(
        self, session_id: str, lastn: Optional[int] = None
    ) -> List[Memory]:
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
        List[Memory]
            A list of Memory objects representing the retrieved memory entries.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        url = f"{self.base_url}{API_BASEURL}/sessions/{session_id}/memory"
        params = (
            {"lastn": lastn} if lastn is not None else {}
        )  # Include 'lastn' as a query parameter if provided
        response = await self.client.get(url, params=params)

        if response.status_code == 404:
            raise NotFoundError(f"No memory found for session {session_id}")

        if response.status_code != 200:
            raise APIError(f"Unexpected status code: {response.status_code}")

        response_data = response.json()

        # Check if the response contains the expected field 'messages'.
        if "messages" in response_data:
            # If 'messages' is None, return an empty list.
            if response_data["messages"] is None:
                return []
            # Create a Memory instance using the 'messages' field from the response.
            memory = Memory(
                messages=response_data["messages"],
                # Add the 'summary' field if it is present in the response.
                summary=response_data.get("summary", None),
                # Add any other fields from the response that are relevant to the
                # Memory class.
            )
            return [memory]
        else:
            raise APIError("Unexpected response format from the API")

    @sync
    def add_memory(self, session_id: str, memory_messages: Memory) -> str:
        """
        Add memory to the specified session. This method is a synchronous wrapper for
        the asynchronous method `aadd_memory`.

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
        # we've wrapped the function in a decorator that will run it synchronously.
        # ignore the type error.
        return self.aadd_memory(session_id, memory_messages)  # type: ignore

    async def aadd_memory(
        self, session_id: str, memory_messages: Memory
    ) -> str:
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
        response = await self.client.post(
            f"{self.base_url}{API_BASEURL}/sessions/{session_id}/memory",
            json=memory_messages.to_dict(),
        )
        if response.status_code != 200:
            raise APIError(f"Unexpected status code: {response.status_code}")

        return response.text

    @sync
    def delete_memory(self, session_id: str) -> str:
        """
        Delete memory for the specified session. This method is a synchronous wrapper
        for the asynchronous method `adelete_memory`.

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
        # we've wrapped the function in a decorator that will run it synchronously.
        # ignore the type error.
        return self.adelete_memory(session_id)  # type: ignore

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
        response = await self.client.delete(
            f"{self.base_url}{API_BASEURL}/sessions/{session_id}/memory"
        )
        if response.status_code == 404:
            raise NotFoundError(f"No session found for session {session_id}")

        if response.status_code != 200:
            raise APIError(f"Unexpected status code: {response.status_code}")
        return response.text

    @sync
    def search_memory(
        self,
        session_id: str,
        search_payload: SearchPayload,
        limit: Optional[int] = None,
    ) -> List[SearchResult]:
        """
        Search memory for the specified session. This method is a synchronous wrapper
        for the asynchronous method `asearch_memory`.

        Parameters
        ----------
        session_id : str
            The ID of the session for which memory should be searched.
        search_payload : SearchPayload
            A SearchPayload object representing the search query.
        limit : Optional[int], optional
            The maximum number of search results to return. Defaults to None (no limit).

        Returns
        -------
        List[SearchResult]
            A list of SearchResult objects representing the search results.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        # we've wrapped the function in a decorator that will run it synchronously.
        # ignore the type error.
        return self.asearch_memory(session_id, search_payload, limit)  # type: ignore

    async def asearch_memory(
        self,
        session_id: str,
        search_payload: SearchPayload,
        limit: Optional[int] = None,
    ) -> List[SearchResult]:
        """
        Asynchronously search memory for the specified session.

        Parameters
        ----------
        session_id : str
            The ID of the session for which memory should be searched.
        search_payload : SearchPayload
            A SearchPayload object representing the search query.
        limit : Optional[int], optional
            The maximum number of search results to return. Defaults to None (no limit).

        Returns
        -------
        List[SearchResult]
            A list of SearchResult objects representing the search results.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        params = {"limit": limit} if limit is not None else {}
        response = await self.client.post(
            f"{self.base_url}{API_BASEURL}/sessions/{session_id}/search",
            json=search_payload.__dict__,
            params=params,
        )
        if response.status_code != 200:
            raise APIError(f"Unexpected status code: {response.status_code}")
        return [
            SearchResult(**search_result) for search_result in response.json()
        ]

    async def close(self) -> None:
        """
        Asynchronously close the HTTP client.

        [Optional] This method may be called when the ZepClient is no longer needed to
        release resources.
        """
        await self.client.aclose()
