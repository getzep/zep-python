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
        """
        
        if session_id is None or session_id.strip() == "":
            raise ValueError("Session ID cannot be empty.")

        url = f"/sessions/{session_id}/messages"

        try:
            print(f"url: {url}")
            response = self.client.get(url=url)
        except httpx.NetworkError as e:
            raise ConnectionError("Unable to connect to server.") 

        return [Message.parse_obj(message) for message in response.json()['messages']]
        

    def update_message_metadata(
        self, request: UpdateMessageMetadataRequest
    ) -> Message:
        """
        Updates the metadata of a message.

        Parameters
        ----------
        request : UpdateMessageMetadataRequest
            The request to update the metadata of a message.

        Returns
        -------
        Message
            The updated message.
        """
        response = self.client.patch(
            url="/messages/metadata",
            json=request.dict(),
        )
        return Message(**response.json())
