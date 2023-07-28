from __future__ import annotations

from typing import Any, Dict, List, Optional

import httpx

from zep_python.exceptions import APIError, handle_response
from zep_python.memory.models import (
    Memory,
    MemorySearchPayload,
    MemorySearchResult,
    Message,
    Session,
    Summary,
)


class MemoryClient:
    """
    memory_client class implementation for memory APIs.

    Attributes
    ----------
    aclient : httpx.AsyncClient
        The async client used for making API requests.
    client : httpx.Client
        The client used for making API requests.

    Methods
    -------
    ___init___(aclient: httpx.AsyncClient, client: httpx.Client) -> None:
        Initialize the zep_memory_api.

    handle_response(response: httpx.Response,
                    missing_message:
                    Optional[str] = None) -> None:
        Handle the response from the API.

    parse_get_memory_response(response_data: Any) -> Memory:
        Parse the response from the get_memory API call.

    gen_get_params(lastn: Optional[int] = None) -> Dict[str, Any]:
        Generate the parameters for the get_memory API call.

    get_session(session_id: str) -> Session:
        Retrieve the session with the specified ID.

    aget_session(session_id: str) -> Session:
        Asynchronously retrieve the session with the specified ID.

    add_session(session: Session) -> str:
        Add or update the specified session.

    aaadd_session(session: Session) -> str:
        Asynchronously add or update the specified session.

    get_memory(session_id: str, lastn: Optional[int] = None) -> Memory:
        Retrieve memory for the specified session.

    aget_memory(session_id: str, lastn: Optional[int] = None) -> Memory:
        Asynchronously retrieve memory for the specified session.

    add_memory(session_id: str, memory_messages: Memory) -> str:
        Add memory to the specified session.

    aadd_memory(session_id: str, memory_messages: Memory) -> str:
        Asynchronously add memory to the specified session.

    delete_memory(session_id: str) -> str:
        Delete memory for the specified session.

    adelete_memory(session_id: str) -> str:
        Asynchronously delete memory for the specified session.

    search_memory(session_id: str, search_payload: MemorySearchPayload,
                    limit: Optional[int] = None) -> List[MemorySearchResult]:
        Search memory for the specified session.

    asearch_memory(session_id: str, search_payload: MemorySearchPayload,
                    limit: Optional[int] = None) -> List[MemorySearchResult]:
        Asynchronously search memory for the specified session.

    """

    aclient: httpx.AsyncClient
    client: httpx.Client

    def __init__(self, aclient: httpx.AsyncClient, client: httpx.Client) -> None:
        self.aclient = aclient
        self.client = client

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

    # Memory APIs : Get a Session
    def get_session(self, session_id: str) -> Session:
        """
        Retrieve the session with the specified ID.

        Parameters
        ----------
        session_id : str
            The ID of the session to retrieve.

        Returns
        -------
        Session
            The session with the specified ID.

        Raises
        ------
        ValueError
            If the session ID is None or empty.
        APIError
            If the API response format is unexpected.
        """
        if session_id is None or session_id.strip() == "":
            raise ValueError("session_id must be provided")

        url = f"/sessions/{session_id}"

        try:
            response = self.client.get(url)
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e

        handle_response(response, f"No session found for session {session_id}")

        response_data = response.json()

        return Session.parse_obj(response_data)

    # Memory APIs : Get a Session Asynchronously
    async def aget_session(self, session_id: str) -> Session:
        """
        Asynchronously retrieve the session with the specified ID.

        Parameters
        ----------
        session_id : str
            The ID of the session to retrieve.

        Returns
        -------
        Session
            The session with the specified ID.

        Raises
        ------
        ValueError
            If the session ID is None or empty.
        APIError
            If the API response format is unexpected.
        """
        if session_id is None or session_id.strip() == "":
            raise ValueError("session_id must be provided")

        url = f"/sessions/{session_id}"

        try:
            response = await self.aclient.get(url)
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e

        handle_response(response, f"No session found for session {session_id}")

        response_data = response.json()

        return Session.parse_obj(response_data)

    # Memory APIs : Add a Session
    def add_session(self, session: Session) -> str:
        """
        Add or update the specified session.

        Parameters
        ----------
        session : Session
            The session to add.

        Returns
        -------
        Session
            The added session.

        Raises
        ------
        ValueError
            If the session is None or empty.
        APIError
            If the API response format is unexpected.
        """
        if session is None:
            raise ValueError("session must be provided")
        if session.session_id is None or session.session_id.strip() == "":
            raise ValueError("session.session_id must be provided")

        url = f"/sessions/{session.session_id}"

        try:
            response = self.client.post(url, json=session.dict(exclude_none=True))
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e

        handle_response(response, f"Failed to add session {session.session_id}")

        return response.text

    # Memory APIs : Add a Session Asynchronously
    async def aadd_session(self, session: Session) -> str:
        """
        Asynchronously add or update the specified session.

        Parameters
        ----------
        session : Session
            The session to add.

        Returns
        -------
        Session
            The added session.

        Raises
        ------
        ValueError
            If the session is None or empty.
        APIError
            If the API response format is unexpected.
        """
        if session is None:
            raise ValueError("session must be provided")
        if session.session_id is None or session.session_id.strip() == "":
            raise ValueError("session.session_id must be provided")

        url = f"/sessions/{session.session_id}"

        try:
            response = await self.aclient.post(
                url, json=session.dict(exclude_none=True)
            )
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e

        handle_response(response, f"Failed to add session {session.session_id}")

        return response.text

    # Memory APIs : Get Memory
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
        ValueError
            If the session ID is None or empty.
        APIError
            If the API response format is unexpected.
        """

        if session_id is None or session_id.strip() == "":
            raise ValueError("session_id must be provided")

        url = f"/sessions/{session_id}/memory"
        params = self._gen_get_params(lastn)
        response = self.client.get(url, params=params)

        handle_response(response, f"No memory found for session {session_id}")

        response_data = response.json()

        return self._parse_get_memory_response(response_data)

    # Memory APIs : Get Memory Asynchronously
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
        ValueError
            If the session ID is None or empty.
        APIError
            If the API response format is unexpected.
        """
        if session_id is None or session_id.strip() == "":
            raise ValueError("session_id must be provided")

        url = f"/sessions/{session_id}/memory"
        params = self._gen_get_params(lastn)
        response = await self.aclient.get(url, params=params)

        handle_response(response, f"No memory found for session {session_id}")

        response_data = response.json()

        return self._parse_get_memory_response(response_data)

    # Memory APIs : Add Memory
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
        ValueError
            If the session ID is None or empty.
        APIError
            If the API response format is unexpected.
        """
        if session_id is None or session_id.strip() == "":
            raise ValueError("session_id must be provided")

        response = self.client.post(
            f"/sessions/{session_id}/memory",
            json=memory_messages.dict(exclude_none=True),
        )

        handle_response(response)

        return response.text

    # Memory APIs : Add Memory Asynchronously
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
        ValueError
            If the session ID is None or empty.
        APIError
            If the API response format is unexpected.
        """
        if session_id is None or session_id.strip() == "":
            raise ValueError("session_id must be provided")

        response = await self.aclient.post(
            f"/sessions/{session_id}/memory",
            json=memory_messages.dict(exclude_none=True),
        )

        handle_response(response)

        return response.text

    # Memory APIs : Delete Memory
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
        ValueError
            If the session ID is None or empty.
        APIError
            If the API response format is unexpected.
        """
        if session_id is None or session_id.strip() == "":
            raise ValueError("session_id must be provided")

        response = self.client.delete(f"/sessions/{session_id}/memory")
        handle_response(response)
        return response.text

    # Memory APIs : Delete Memory Asynchronously
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
        ValueError
            If the session ID is None or empty.
        APIError
            If the API response format is unexpected.
        """
        if session_id is None or session_id.strip() == "":
            raise ValueError("session_id must be provided")

        response = await self.aclient.delete(f"/sessions/{session_id}/memory")
        handle_response(response)
        return response.text

    # Memory APIs : Search Memory
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
        ValueError
            If the session ID is None or empty.
        APIError
            If the API response format is unexpected.
        """
        if session_id is None or session_id.strip() == "":
            raise ValueError("session_id must be provided")

        if search_payload is None:
            raise ValueError("search_payload must be provided")

        params = {"limit": limit} if limit is not None else {}
        response = self.client.post(
            f"/sessions/{session_id}/search",
            json=search_payload.dict(),
            params=params,
        )
        handle_response(response)
        return [
            MemorySearchResult(**search_result) for search_result in response.json()
        ]

    # Memory APIs : Search Memory Asynchronously
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
        ValueError
            If the session ID is None or empty.
        APIError
            If the API response format is unexpected.
        """
        if session_id is None or session_id.strip() == "":
            raise ValueError("session_id must be provided")

        if search_payload is None:
            raise ValueError("search_payload must be provided")

        params = {"limit": limit} if limit is not None else {}
        response = await self.aclient.post(
            f"/sessions/{session_id}/search",
            json=search_payload.dict(),
            params=params,
        )
        handle_response(response)
        return [
            MemorySearchResult(**search_result) for search_result in response.json()
        ]
