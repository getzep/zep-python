from __future__ import annotations

from typing import Any, AsyncGenerator, Dict, Generator, List, Optional
from .models import Message, UpdateMessageMetadataRequest
from zep_python.exceptions import APIError, handle_response

import httpx

class MessageClient:
    """
    MessageClient class for interacting with the Zep message API.

    Attributes
    ----------
    aclient : httpx.AsyncClient
        The async client used for making API requests.
    client : httpx.Client
        The client used for making API requests.
    """

    def __init__(self, aclient: AsyncClient, client: Client) -> None:
        """
        Initializes a MessageClient object.

        Parameters
        ----------
        aclient : httpx.AsyncClient
            The async client used for making API requests.
        client : httpx.Client
            The client used for making API requests.
        """
        self.aclient = aclient
        self.client = client

    def get_session_messages(self, session_id: str) -> List[Message]:
        """
        Gets all messages for a session.

        Parameters
        ----------
        session_id : str
            The ID of the session.

        Returns
        -------
        List[Message]
            The list of messages for the session.

        Raises
        ------
        ValueError
            If the session ID is empty.
        ConnectionError
            If unable to connect to the server.
        APIError
            If unable to get messages for the session.
        NotFoundError
            If the session is not found.
        """
        
        if session_id is None or session_id.strip() == "":
            raise ValueError("Session ID cannot be empty.")

        url = f"/sessions/{session_id}/messages"

        try:
            print(f"url: {url}")
            response = self.client.get(url=url)
        except httpx.NetworkError as e:
            raise ConnectionError("Unable to connect to server.")

        handle_response(response, f"Unable to get messages for session {session_id}.")

        return [Message.parse_obj(message) for message in response.json()['messages']]

    async def aget_session_messages(self, session_id: str) -> List[Message]:
        """
        Gets all messages for a session.

        Parameters
        ----------
        session_id : str
            The ID of the session.

        Returns
        -------
        List[Message]
            The list of messages for the session.

        Raises
        ------
        ValueError
            If the session ID is empty.
        ConnectionError
            If unable to connect to the server.
        APIError
            If unable to get messages for the session.
        NotFoundError
            If the session is not found.
        """
        
        if session_id is None or session_id.strip() == "":
            raise ValueError("Session ID cannot be empty.")

        url = f"/sessions/{session_id}/messages"

        try:
            print(f"url: {url}")
            response = await self.aclient.get(url=url)
        except httpx.NetworkError as e:
            raise ConnectionError("Unable to connect to server.")

        handle_response(response, f"Unable to get messages for session {session_id}.")

        return [Message.parse_obj(message) for message in response.json()['messages']]
        

    def get_session_message(self, session_id: str, message_id: str) -> List[Message]:
        """
        Gets a specific message from a session

        Parameters
        ----------
        session_id : str
            The ID of the session.
        message_id : str
            The ID of the message.

        Returns
        -------
        Message
            The message.
        """
        
        if session_id is None or session_id.strip() == "":
            raise ValueError("Session ID cannot be empty.")

        if message_id is None or message_id.strip() == "":
            raise ValueError("Message ID cannot be empty.")

        url = f"/sessions/{session_id}/messages/{message_id}"

        try:
            print(f"url: {url}")
            response = self.client.get(url=url)
        except httpx.NetworkError as e:
            raise ConnectionError("Unable to connect to server.")

        handle_response(response, f"Unable to get message {message_id} for session {session_id}.")

        response_data = response.json()
        return Message.parse_obj(response_data)

    async def get_session_message(self, session_id: str, message_id: str) -> List[Message]:
        """
        Gets a specific message from a session

        Parameters
        ----------
        session_id : str
            The ID of the session.
        message_id : str
            The ID of the message.

        Returns
        -------
        Message
            The message.
        """
        
        if session_id is None or session_id.strip() == "":
            raise ValueError("Session ID cannot be empty.")

        if message_id is None or message_id.strip() == "":
            raise ValueError("Message ID cannot be empty.")

        url = f"/sessions/{session_id}/messages/{message_id}"

        try:
            print(f"url: {url}")
            response = await self.aclient.get(url=url)
        except httpx.NetworkError as e:
            raise ConnectionError("Unable to connect to server.")

        handle_response(response, f"Unable to get message {message_id} for session {session_id}.")

        response_data = response.json()
        return Message.parse_obj(response_data)

    def update_message_metadata(
        self, session_id: str, message_id: str, metadata: Dict[str, Any]
    ) -> Message:
        """
        Updates the metadata of a message.

        Parameters
        ----------
        session_id : str
            The ID of the session.
        message_id : str
            The ID of the message.
        metadata : Dict[str, Any]
            The metadata to update.

        Returns
        -------
        Message
            The updated message.
        """
        
        if session_id is None or session_id.strip() == "":
            raise ValueError("Session ID cannot be empty.")

        if message_id is None or message_id.strip() == "":
            raise ValueError("Message ID cannot be empty.")

        url = f"/sessions/{session_id}/messages/{message_id}"

        try:
            response = self.client.patch(url=url, json=metadata)
        except httpx.NetworkError as e:
            raise ConnectionError("Unable to connect to server.")

        handle_response(response, f"Unable to update message metadata {message_id} for session {session_id}.")

        response_data = response.json()
        return Message.parse_obj(response_data) 

    async def update_message_metadata(
        self, session_id: str, message_id: str, metadata: Dict[str, Any]
    ) -> Message:
        """
        Updates the metadata of a message.

        Parameters
        ----------
        session_id : str
            The ID of the session.
        message_id : str
            The ID of the message.
        metadata : Dict[str, Any]
            The metadata to update.

        Returns
        -------
        Message
            The updated message.
        """
        
        if session_id is None or session_id.strip() == "":
            raise ValueError("Session ID cannot be empty.")

        if message_id is None or message_id.strip() == "":
            raise ValueError("Message ID cannot be empty.")

        url = f"/sessions/{session_id}/messages/{message_id}"

        try:
            response = await self.aclient.patch(url=url, json=metadata)
        except httpx.NetworkError as e:
            raise ConnectionError("Unable to connect to server.")

        handle_response(response, f"Unable to update message metadata {message_id} for session {session_id}.")

        response_data = response.json()
        return Message.parse_obj(response_data) 
