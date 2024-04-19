import urllib.parse
from typing import AsyncGenerator, Generator, List, Optional

import httpx
from httpx import AsyncClient, Client

from zep_python.exceptions import handle_response

from ..memory.models import Session
from .models import CreateUserRequest, UpdateUserRequest, User


class UserClient:
    """
    UserClient class implementation for user APIs.

    Attributes
    ----------
    aclient : httpx.AsyncClient
        The async client used for making API requests.
    client : httpx.Client
        The client used for making API requests.
    """

    def __init__(self, aclient: AsyncClient, client: Client) -> None:
        """
        Initialize the UserClient.

        Parameters
        ----------
        aclient : httpx.AsyncClient
            The async client used for making API requests.
        client : httpx.Client
            The client used for making API requests.
        """

        self.aclient = aclient
        self.client = client

    def add(self, user: CreateUserRequest) -> User:
        """
        Add a user.

        Parameters
        ----------
        user : CreateUserRequest
            The user to add.

        Returns
        -------
        User
            The user that was added.

        Raises
        ------
        ConnectionError
            If the client fails to connect to the server.
        APIError
            If the server returns an error.

        """
        try:
            response = self.client.post(
                "/users", json=user.model_dump(exclude_none=True, exclude_unset=True)
            )
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e

        handle_response(response)
        return User.model_validate(response.json())

    async def aadd(self, user: CreateUserRequest) -> User:
        """
        Async add a user.

        Parameters
        ----------
        user : CreateUserRequest
            The user to add.

        Returns
        -------
        User
            The user that was added.

        Raises
        ------
        ConnectionError
            If the client fails to connect to the server.
        APIError
            If the server returns an error.

        """
        try:
            response = await self.aclient.post(
                "/users", json=user.model_dump(exclude_none=True, exclude_unset=True)
            )
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e

        handle_response(response)
        return User.model_validate(response.json())

    def get(self, user_id: str) -> User:
        """
        Get a user.

        Parameters
        ----------
        user_id : str
            The user_id of the user to get.

        Returns
        -------
        User
            The user that was retrieved.

        Raises
        ------
        ConnectionError
            If the client fails to connect to the server.
        APIError
            If the server returns an error.
        NotFoundError
            If the user does not exist.
        """
        try:
            response = self.client.get(f"/users/{urllib.parse.quote_plus(user_id)}")
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e

        handle_response(response)
        return User.model_validate(response.json())

    async def aget(self, user_id: str) -> User:
        """
        Async get a user.

        Parameters
        ----------
        user_id : str
            The user_id of the user to get.

        Returns
        -------
        User
            The user that was retrieved.

        Raises
        ------
        ConnectionError
            If the client fails to connect to the server.
        APIError
            If the server returns an error.
        NotFoundError
            If the user does not exist.
        """
        if user_id is None:
            raise ValueError("user_id must be provided")
        try:
            response = await self.aclient.get(
                f"/users/{urllib.parse.quote_plus(user_id)}"
            )
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e

        handle_response(response)
        return User.model_validate(response.json())

    def update(self, user: UpdateUserRequest) -> User:
        """
        Update a user.

        Parameters
        ----------
        user : UpdateUserRequest
            The user to update.

        Returns
        -------
        User
            The user that was updated.

        Raises
        ------
        ConnectionError
            If the client fails to connect to the server.
        APIError
            If the server returns an error.
        NotFoundError
            If the user does not exist
        """
        if user.user_id is None:
            raise ValueError("user_id must be provided")

        try:
            response = self.client.patch(
                f"/users/{urllib.parse.quote_plus(user.user_id)}",
                json=user.model_dump(exclude_none=True, exclude_unset=True),
            )
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e
        handle_response(response)

        return User.model_validate(response.json())

    async def aupdate(self, user: UpdateUserRequest) -> User:
        """
        Async update a user.

        Parameters
        ----------
        user : UpdateUserRequest
            The user to update.

        Returns
        -------
        User
            The user that was updated.

        Raises
        ------
        ConnectionError
            If the client fails to connect to the server.
        APIError
            If the server returns an error.
        NotFoundError
            If the user does not exist.
        """
        if user.user_id is None:
            raise ValueError("user_id must be provided")
        try:
            response = await self.aclient.patch(
                f"/users/{urllib.parse.quote_plus(user.user_id)}",
                json=user.model_dump(exclude_none=True, exclude_unset=True),
            )
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e

        handle_response(response)

        return User.model_validate(response.json())

    def delete(self, user_id: str) -> None:
        """
        Delete a user.

        Parameters
        ----------
        user_id : str
            The user_id of the user to delete.

        Returns
        -------
        None

        Raises
        ------
        ConnectionError
            If the client fails to connect to the server.
        APIError
            If the server returns an error.
        NotFoundError
            If the user does not exist.
        """
        try:
            response = self.client.delete(f"/users/{urllib.parse.quote_plus(user_id)}")
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e

        handle_response(response)

    async def adelete(self, user_id: str) -> None:
        """
        Async delete a user.

        Parameters
        ----------
        user_id : str
            The user_id of the user to delete.

        Returns
        -------
        None

        Raises
        ------
        ConnectionError
            If the client fails to connect to the server.
        APIError
            If the server returns an error.
        NotFoundError
            If the user does not exist.
        """
        try:
            response = await self.aclient.delete(
                f"/users/{urllib.parse.quote_plus(user_id)}"
            )
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e

        handle_response(response)

    def list(
        self, limit: Optional[int] = None, cursor: Optional[int] = None
    ) -> List[User]:
        """
        List users.

        Parameters
        ----------
        limit : Optional[int]
            The maximum number of users to return.
        cursor : Optional[int]
            The cursor to use for pagination.

        Returns
        -------
        List[User]
            The list of users. If no users are found, an empty list is returned.

        Raises
        ------
        ConnectionError
            If the client fails to connect to the server.
        APIError
            If the server returns an error.
        """
        try:
            response = self.client.get(
                "/users", params={"limit": limit, "cursor": cursor}
            )
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e
        handle_response(response)
        return [User.model_validate(user) for user in response.json()]

    async def alist(
        self, limit: Optional[int] = None, cursor: Optional[int] = None
    ) -> List[User]:
        """
        Async list users.

        Parameters
        ----------
        limit : Optional[int]
            The maximum number of users to return.
        cursor : Optional[int]
            The cursor to use for pagination.

        Returns
        -------
        List[User]
            The list of users. An empty list is returned if there are no users.

        Raises
        ------
        ConnectionError
            If the client fails to connect to the server.
        APIError
            If the server returns an error.
        """
        try:
            response = await self.aclient.get(
                "/users", params={"limit": limit, "cursor": cursor}
            )
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e
        handle_response(response)
        return [User.model_validate(user) for user in response.json()]

    def list_chunked(self, chunk_size: int = 100) -> Generator[List[User], None, None]:
        """
        List all users in chunks.

        This method uses pagination to retrieve the users in chunks and returns a
        generator that yields each chunk of users as a list.

        Parameters
        ----------
        chunk_size : int, optional
            The number of users to retrieve in each chunk, by default 100

        Returns
        -------
        Generator[List[User], None, None]
            A generator that yields each chunk of users as a list.

        Raises
        ------
        ConnectionError
            If the client fails to connect to the server.
        APIError
            If the server returns an error.
        """
        cursor: Optional[int] = None

        while True:
            response = self.list(limit=chunk_size, cursor=cursor)

            if len(response) == 0:
                # We've reached the last page
                break

            yield response

            if cursor is None:
                cursor = 0
            cursor += chunk_size

    async def alist_chunked(
        self, chunk_size: int = 100
    ) -> AsyncGenerator[List[User], None]:
        """
        Async list all users in chunks.

        This method uses pagination to retrieve the users in chunks and returns a
        generator that yields each chunk of users as a list.

        Parameters
        ----------
        chunk_size : int, optional
            The number of users to retrieve in each chunk, by default 100

        Returns
        -------
        Generator[List[User], None, None]
            A generator that yields each chunk of users as a list.

        Raises
        ------
        ConnectionError
            If the client fails to connect to the server.
        APIError
            If the server returns an error.
        """
        cursor: Optional[int] = None

        while True:
            response = await self.alist(limit=chunk_size, cursor=cursor)
            if len(response) == 0:
                # We've reached the last page
                break

            yield response

            if cursor is None:
                cursor = 0
            cursor += chunk_size

    def get_sessions(self, user_id: str) -> List[Session]:
        """
        List all sessions associated with this user.

        Parameters
        ----------
        user_id : str
            The user_id of the user whose sessions to list.

        Returns
        -------
        List[Session]
            The list of sessions.

        Raises
        ------
        ConnectionError
            If the client fails to connect to the server.
        APIError
            If the server returns an error.
        """
        try:
            response = self.client.get(
                f"/users/{urllib.parse.quote_plus(user_id)}/sessions"
            )
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e

        handle_response(response)
        return [Session.model_validate(session) for session in response.json()]

    async def aget_sessions(self, user_id: str) -> List[Session]:
        """
        Async list all sessions associated with this user.

        Parameters
        ----------
        user_id : str
            The user_id of the user whose sessions to list.

        Returns
        -------
        List[Session]
            The list of sessions.

        Raises
        ------
        ConnectionError
            If the client fails to connect to the server.
        APIError
            If the server returns an error.
        """
        try:
            response = await self.aclient.get(
                f"/users/{urllib.parse.quote_plus(user_id)}/sessions"
            )
        except httpx.NetworkError as e:
            raise ConnectionError("Failed to connect to server") from e

        handle_response(response)
        return [Session.model_validate(session) for session in response.json()]
