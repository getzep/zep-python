from __future__ import annotations

import urllib.parse
from typing import Any, AsyncGenerator, Dict, Generator, List, Optional

import httpx

from zep_python.exceptions import handle_response
from zep_python.memory.models import (
    ClassifySessionRequest,
    ClassifySessionResponse,
    Memory,
    MemorySearchPayload,
    MemorySearchResult,
    MemoryType,
    Question,
    SearchScope,
    Session,
)
from zep_python.utils import SearchType


class MemoryClient:
    """
    memory_client class implementation for memory APIs.

    Attributes
    ----------
    aclient : httpx.AsyncClient
        The async client used for making API requests.
    client : httpx.Client
        The client used for making API requests.

    """

    aclient: httpx.AsyncClient
    client: httpx.Client

    def __init__(self, aclient: httpx.AsyncClient, client: httpx.Client) -> None:
        self.aclient = aclient
        self.client = client

    def _gen_get_params(
        self, lastn: Optional[int] = None, memory_type: Optional[str] = None
    ) -> Dict[str, Any]:
        params: dict[str, Any] = {}
        if lastn is not None:
            params["lastn"] = lastn
        if memory_type is not None:
            if memory_type not in MemoryType.__members__:
                raise ValueError(
                    f"memory_type must be one of {list(MemoryType.__members__)}"
                )
            params["memoryType"] = memory_type
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
        NotFoundError
            If the session with the specified ID is not found.
        ValueError
            If the session ID is None or empty.
        APIError
            If the API response format is unexpected.
        ConnectionError
            If the connection to the server fails.
        """
        if session_id is None or session_id.strip() == "":
            raise ValueError("session_id must be provided")

        url = f"/sessions/{urllib.parse.quote_plus(session_id)}"

        try:
            response = self.client.get(url)
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e

        handle_response(response, f"No session found for session {session_id}")

        response_data = response.json()

        return Session.model_validate(response_data)

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
        NotFoundError
            If the session with the specified ID is not found.
        ValueError
            If the session ID is None or empty.
        APIError
            If the API response format is unexpected.
        ConnectionError
            If the connection to the server fails.
        """
        if session_id is None or session_id.strip() == "":
            raise ValueError("session_id must be provided")

        url = f"/sessions/{urllib.parse.quote_plus(session_id)}"

        try:
            response = await self.aclient.get(url)
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e

        handle_response(response, f"No session found for session {session_id}")

        response_data = response.json()

        return Session.model_validate(response_data)

    # Memory APIs : Add a Session
    def add_session(self, session: Session) -> Session:
        """
        Add a session.

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
        ConnectionError
            If the connection to the server fails.
        """
        if session is None:
            raise ValueError("session must be provided")
        if session.session_id is None or session.session_id.strip() == "":
            raise ValueError("session.session_id must be provided")

        url = "sessions"

        try:
            response = self.client.post(
                url, json=session.model_dump(exclude_none=True, exclude_unset=True)
            )
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e

        handle_response(response, f"Failed to add session {session.session_id}")

        return Session.model_validate(response.json())

    # Memory APIs : Add a Session Asynchronously
    async def aadd_session(self, session: Session) -> Session:
        """
        Asynchronously add a session.

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
        ConnectionError
            If the connection to the server fails.
        """
        if session is None:
            raise ValueError("session must be provided")
        if session.session_id is None or session.session_id.strip() == "":
            raise ValueError("session.session_id must be provided")

        url = "sessions"

        try:
            response = await self.aclient.post(
                url, json=session.model_dump(exclude_none=True, exclude_unset=True)
            )
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e

        handle_response(response, f"Failed to add session {session.session_id}")

        return Session.model_validate(response.json())

    # Memory APIs : Update a Session
    def update_session(self, session: Session) -> Session:
        """
        Update the specified session.

        Parameters
        ----------
        session : Session
            The session data to update.

        Returns
        -------
        Session
            The updated session.

        Raises
        ------
        NotFoundError
            If the session with the specified ID is not found.
        ValueError
            If the session ID or session is None.
        APIError
            If the API response format is unexpected.
        """
        if session is None:
            raise ValueError("session must be provided")
        if session.session_id is None or session.session_id.strip() == "":
            raise ValueError("session_id must be provided")

        response = self.client.patch(
            f"/sessions/{urllib.parse.quote(session.session_id)}",
            json=session.model_dump(exclude_none=True, exclude_unset=True),
        )

        handle_response(response, f"Failed to update session {session.session_id}")

        return Session.model_validate(response.json())

    # Memory APIs : Update a Session Asynchronously
    async def aupdate_session(self, session: Session) -> Session:
        """
        Asynchronously update the specified session.

        Parameters
        ----------
        session : Session
            The session data to update.

        Returns
        -------
        Session
            The updated session.

        Raises
        ------
        NotFoundError
            If the session with the specified ID is not found.
        ValueError
            If the session ID or session is None.
        APIError
            If the API response format is unexpected.
        """
        if session is None:
            raise ValueError("session must be provided")
        if session.session_id is None or session.session_id.strip() == "":
            raise ValueError("session_id must be provided")

        response = await self.aclient.patch(
            f"/sessions/{urllib.parse.quote(session.session_id)}",
            json=session.model_dump(exclude_none=True, exclude_unset=True),
        )

        handle_response(response, f"Failed to update session {session.session_id}")

        return Session.model_validate(response.json())

    async def aclassify_session(
        self,
        session_id: str,
        name: str,
        classes: List[str],
        last_n: Optional[int] = None,
        persist: Optional[bool] = True,
        instruction: Optional[str] = None,
    ) -> ClassifySessionResponse:
        """
        Classify the session with the specified ID. Asynchronous version.

        Parameters
        ----------
        session_id : str
            The ID of the session to classify.
        name : str
            The name of the classifier. Will be used to store the classification in
            session metadata if persist is True.
        classes : List[str]
            The classes to use for classification.
        last_n : Optional[int], optional
            The number of session messages to consider for classification.
            Defaults to 4.
        persist : Optional[bool], optional
            Whether to persist the classification to session metadata.
            Defaults to True.
        instruction : Optional[str], optional
            Custom instruction to use for classification. Defaults to None.

        Returns
        -------
        ClassifySessionResponse
            A response object containing the name of the classifier.

        Raises
        ------
        NotFoundError
            If the session with the specified ID is not found.
        ValueError
            If required values are not provided or are invalid.
        APIError
            If the API response format is unexpected.
        """
        if session_id is None or session_id.strip() == "":
            raise ValueError("session_id must be provided")

        if name is None or name.strip() == "":
            raise ValueError("name must be provided")

        if classes is None or len(classes) == 0:
            raise ValueError("classes must be provided")

        request = ClassifySessionRequest(
            session_id=session_id,
            name=name,
            classes=classes,
            last_n=last_n,
            persist=persist,
            instruction=instruction,
        )

        response = await self.aclient.post(
            f"/sessions/{urllib.parse.quote_plus(session_id)}/classify",
            json=request.model_dump(exclude_none=True, exclude_unset=True),
        )
        handle_response(response)

        return ClassifySessionResponse(**response.json())

    def classify_session(
        self,
        session_id: str,
        name: str,
        classes: List[str],
        last_n: Optional[int] = None,
        persist: Optional[bool] = True,
        instruction: Optional[str] = None,
    ) -> ClassifySessionResponse:
        """
        Classify the session with the specified ID.

        Parameters
        ----------
        session_id : str
            The ID of the session to classify.
        name : str
            The name of the classifier. Will be used to store the classification in
            session metadata if persist is True.
        classes : List[str]
            The classes to use for classification.
        last_n : Optional[int], optional
            The number of session messages to consider for classification.
            Defaults to 4.
        persist : Optional[bool], optional
            Whether to persist the classification to session metadata.
            Defaults to True.
        instruction : Optional[str], optional
            Custom instruction to use for classification. Defaults to None.

        Returns
        -------
        ClassifySessionResponse
            A response object containing the name of the classifier.

        Raises
        ------
        NotFoundError
            If the session with the specified ID is not found.
        ValueError
            If required values are not provided or are invalid.
        APIError
            If the API response format is unexpected.
        """
        if session_id is None or session_id.strip() == "":
            raise ValueError("session_id must be provided")

        if name is None or name.strip() == "":
            raise ValueError("name must be provided")

        if classes is None or len(classes) == 0:
            raise ValueError("classes must be provided")

        request = ClassifySessionRequest(
            session_id=session_id,
            name=name,
            classes=classes,
            last_n=last_n,
            persist=persist,
            instruction=instruction,
        )

        response = self.client.post(
            f"/sessions/{urllib.parse.quote_plus(session_id)}/classify",
            json=request.model_dump(exclude_none=True, exclude_unset=True),
        )
        handle_response(response)

        return ClassifySessionResponse(**response.json())

    # Memory APIs : Get a List of Sessions
    def list_sessions(
        self, limit: Optional[int] = None, cursor: Optional[int] = None
    ) -> List[Session]:
        """
        Retrieve a list of paginated sessions.

        Parameters
        ----------
        limit : Optional[int]
            Limit the number of results returned.
        cursor : Optional[int]
            Cursor for pagination.

        Returns
        -------
        List[Session]
            A list of all sessions paginated.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        ConnectionError
            If the connection to the server fails.
        """
        url = "sessions"
        params = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor

        try:
            response = self.client.get(url, params=params)
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e

        handle_response(response, "Failed to get sessions")

        response_data = response.json()

        return [Session.model_validate(session) for session in response_data]

    # Memory APIs : Get a List of Sessions Asynchronously
    async def alist_sessions(
        self, limit: Optional[int] = None, cursor: Optional[int] = None
    ) -> List[Session]:
        """
        Asynchronously retrieve a list of paginated sessions.

        Parameters
        ----------
        limit : Optional[int]
            Limit the number of results returned.
        cursor : Optional[int]
            Cursor for pagination.

        Returns
        -------
        List[Session]
            A list of all sessions paginated.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        url = "sessions"
        params = {}
        if limit is not None:
            params["limit"] = limit
        if cursor is not None:
            params["cursor"] = cursor

        try:
            response = await self.aclient.get(url, params=params)
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e

        handle_response(response, "Failed to get sessions")

        response_data = response.json()

        return [Session.model_validate(session) for session in response_data]

    def list_all_sessions(
        self, chunk_size: int = 100
    ) -> Generator[List[Session], None, None]:
        """
        Retrieve all sessions, handling pagination automatically.
        Yields a generator of lists of sessions.

        Parameters
        ----------
        chunk_size : int
            The number of sessions to retrieve at a time.

        Yields
        ------
        List[Session]
            The next chunk of sessions from the server.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        ConnectionError
            If the connection to the server fails.
        """
        cursor: Optional[int] = None

        while True:
            response = self.list_sessions(limit=chunk_size, cursor=cursor)

            if len(response) == 0:
                # We've reached the last page
                break

            yield response

            if cursor is None:
                cursor = 0

            cursor += chunk_size

    async def alist_all_sessions(
        self, chunk_size: int = 100
    ) -> AsyncGenerator[List[Session], None]:
        """
        Asynchronously retrieve all sessions, handling pagination automatically.
        Yields a generator of lists of sessions.

        Parameters
        ----------
        chunk_size : int
            The number of sessions to retrieve at a time.

        Yields
        ------
        List[Session]
            The next chunk of sessions from the server.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        cursor: Optional[int] = None

        while True:
            response = await self.alist_sessions(limit=chunk_size, cursor=cursor)

            if len(response) == 0:
                # We've reached the last page
                break

            yield response

            if cursor is None:
                cursor = 0
            cursor += chunk_size

    # Memory APIs : Get Memory
    def get_memory(
        self,
        session_id: str,
        memory_type: Optional[str] = None,
        lastn: Optional[int] = None,
    ) -> Memory:
        """
        Retrieve memory for the specified session.

        Parameters
        ----------
        session_id : str
            The ID of the session for which to retrieve memory.
        memory_type : Optional[str]
            The type of memory to retrieve: perpetual, summary_retriever, or
                message_window. Defaults to perpetual.
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

        url = f"/sessions/{urllib.parse.quote_plus(session_id)}/memory"
        params = self._gen_get_params(lastn, memory_type or MemoryType.perpetual.value)
        response = self.client.get(url, params=params)

        handle_response(response, f"No memory found for session {session_id}")

        response_data = response.json()

        return Memory.model_validate(response_data)

    # Memory APIs : Get Memory Asynchronously
    async def aget_memory(
        self,
        session_id: str,
        memory_type: Optional[str] = None,
        lastn: Optional[int] = None,
    ) -> Memory:
        """
        Asynchronously retrieve memory for the specified session.

        Parameters
        ----------
        session_id : str
            The ID of the session for which to retrieve memory.
        memory_type : Optional[str]
            The type of memory to retrieve: perpetual, summary_retriever, or
                message_window. Defaults to perpetual.
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

        url = f"/sessions/{urllib.parse.quote_plus(session_id)}/memory"
        params = self._gen_get_params(lastn, memory_type or MemoryType.perpetual.value)
        response = await self.aclient.get(url, params=params)

        handle_response(response, f"No memory found for session {session_id}")

        response_data = response.json()

        return Memory.model_validate(response_data)

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
            f"/sessions/{urllib.parse.quote_plus(session_id)}/memory",
            json=memory_messages.model_dump(exclude_none=True, exclude_unset=True),
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
            f"/sessions/{urllib.parse.quote_plus(session_id)}/memory",
            json=memory_messages.model_dump(exclude_none=True, exclude_unset=True),
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

        response = self.client.delete(
            f"/sessions/{urllib.parse.quote_plus(session_id)}/memory"
        )
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

        response = await self.aclient.delete(
            f"/sessions/{urllib.parse.quote_plus(session_id)}/memory"
        )
        handle_response(response)
        return response.text

    def _validate_search_payload(self, search_payload: MemorySearchPayload) -> None:
        if search_payload is None:
            raise ValueError("search_payload must be provided")

        if search_payload.search_type not in SearchType.__members__:
            raise ValueError("search_type must be one of 'similarity' or 'mmr'")

        if search_payload.search_scope not in SearchScope.__members__:
            raise ValueError("search_scope must be one of 'messages' or 'summary'")

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

        self._validate_search_payload(search_payload)

        params = {"limit": limit} if limit is not None else {}
        response = self.client.post(
            f"/sessions/{urllib.parse.quote_plus(session_id)}/search",
            json=search_payload.model_dump(exclude_unset=True, exclude_none=True),
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

        self._validate_search_payload(search_payload)

        params = {"limit": limit} if limit is not None else {}
        response = await self.aclient.post(
            f"/sessions/{urllib.parse.quote_plus(session_id)}/search",
            json=search_payload.model_dump(exclude_unset=True, exclude_none=True),
            params=params,
        )
        handle_response(response)
        return [
            MemorySearchResult(**search_result) for search_result in response.json()
        ]

    def synthesize_question(self, session_id: str, last_n: int = 3) -> str:
        """
        Synthesize a question from the last N messages in the chat history.

        Parameters
        ----------
        session_id : str
            The ID of the session.
        last_n : int
            The number of messages to use for question synthesis.

        Returns
        -------
        str
            The synthesized question.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if session_id is None or session_id.strip() == "":
            raise ValueError("session_id must be provided")

        params = {"lastNMessages": last_n}
        print(f"/sessions/{urllib.parse.quote_plus(session_id)}/synthesize_question")
        response = self.client.get(
            f"/sessions/{urllib.parse.quote_plus(session_id)}/synthesize_question",
            params=params,
        )

        handle_response(response)

        question = Question(**response.json())

        return question.question

    async def asynthesize_question(self, session_id: str, last_n: int = 3) -> str:
        """
        Synthesize a question from the last N messages in the chat history.

        Parameters
        ----------
        session_id : str
            The ID of the session.
        last_n : int
            The number of messages to use for question synthesis.

        Returns
        -------
        str
            The synthesized question.

        Raises
        ------
        APIError
            If the API response format is unexpected.
        """
        if session_id is None or session_id.strip() == "":
            raise ValueError("session_id must be provided")

        params = {"lastNMessages": last_n}
        response = await self.aclient.get(
            f"/sessions/{urllib.parse.quote_plus(session_id)}/synthesize_question",
            params=params,
        )

        handle_response(response)

        question = Question(**response.json())

        return question.question
