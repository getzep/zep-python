from __future__ import annotations

from typing import Any, Dict, Optional, Sequence


class Memory:
    """
    Represents a memory object with messages, metadata, and other attributes.

    :param messages: A list of message objects, where each message contains a role and
                     content.
    :type messages: Optional[List[Dict[str, Any]]]
    :param metadata: A dictionary containing metadata associated with the memory.
    :type metadata: Optional[Dict[str, Any]]
    :param summary: A dictionary containing a summary of the memory.
    :type summary: Optional[Dict[str, Any]]
    :param uuid: A unique identifier for the memory.
    :type uuid: Optional[str]
    :param created_at: The timestamp when the memory was created.
    :type created_at: Optional[str]
    :param token_count: The token count of the memory.
    :type token_count: Optional[int]
    """

    def __init__(
        self,
        messages: Optional[Sequence[Dict[str, Any] | Message]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        summary: Optional[Dict[str, Any]] = None,
        uuid: Optional[str] = None,
        created_at: Optional[str] = None,
        token_count: Optional[int] = None,
    ) -> None:
        if messages is not None:
            self.messages = [
                (
                    Message(**message_data)
                    if isinstance(message_data, dict)
                    else message_data
                )
                for message_data in messages
            ]
        else:
            self.messages = []
        self.metadata = metadata if metadata is not None else {}
        self.summary = Summary(**summary) if summary else None
        self.uuid = uuid
        self.created_at = created_at
        self.token_count = token_count

    def to_dict(self) -> Dict[str, Any]:
        return {
            "messages": [message.to_dict() for message in self.messages],
            "metadata": self.metadata,
            "summary": self.summary.to_dict() if self.summary else None,
            "uuid": self.uuid,
            "created_at": self.created_at,
            "token_count": self.token_count,
        }


class Message:
    """
    Represents a message in a conversation.

    Attributes
    ----------
    uuid : str, optional
        The unique identifier of the message.
    created_at : str, optional
        The timestamp of when the message was created.
    role : str
        The role of the sender of the message (e.g., "user", "assistant").
    content : str
        The content of the message.
    token_count : int, optional
        The number of tokens in the message.

    Methods
    -------
    to_dict() -> Dict[str, Any]:
        Returns a dictionary representation of the message.
    """

    def __init__(
        self,
        role: str,
        content: str,
        uuid: Optional[str] = None,
        created_at: Optional[str] = None,
        token_count: Optional[int] = None,
    ):
        self.uuid = uuid
        self.created_at = created_at
        self.role = role
        self.content = content
        self.token_count = token_count

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the message.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the attributes of the message.
        """
        return {
            "uuid": self.uuid,
            "created_at": self.created_at,
            "role": self.role,
            "content": self.content,
            "token_count": self.token_count,
        }


class Summary:
    """
    Represents a summary of a conversation.

    Attributes
    ----------
    uuid : str
        The unique identifier of the summary.
    created_at : str
        The timestamp of when the summary was created.
    content : str
        The content of the summary.
    recent_message_uuid : str
        The unique identifier of the most recent message in the conversation.
    token_count : int
        The number of tokens in the summary.

    Methods
    -------
    to_dict() -> Dict[str, Any]:
        Returns a dictionary representation of the summary.
    """

    def __init__(
        self,
        uuid: str,
        created_at: str,
        content: str,
        recent_message_uuid: str,
        token_count: int,
    ):
        self.uuid = uuid
        self.created_at = created_at
        self.content = content
        self.recent_message_uuid = recent_message_uuid
        self.token_count = token_count

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the summary.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the attributes of the summary.
        """
        return {
            "uuid": self.uuid,
            "created_at": self.created_at,
            "content": self.content,
            "recent_message_uuid": self.recent_message_uuid,
            "token_count": self.token_count,
        }


class SearchPayload:
    """
    Represents a search payload for querying memory.

    Attributes
    ----------
    meta : Dict[str, Any]
        Metadata associated with the search query.
    text : str
        The text of the search query.
    """

    def __init__(self, meta: Dict[str, Any], text: str):
        self.meta = meta
        self.text = text


class SearchResult:
    """
    Represents a search result from querying memory.

    Attributes
    ----------
    message : Optional[Dict[str, Any]]
        The message associated with the search result.
    meta : Optional[Dict[str, Any]]
        Metadata associated with the search result.
    score : Optional[float]
        The score of the search result.
    summary : Optional[str]
        The summary of the search result.
    dist : Optional[float]
        The distance metric of the search result.
    """

    def __init__(
        self,
        message: Optional[Dict[str, Any]] = None,
        meta: Optional[
            Dict[str, Any]
        ] = None,  # Add the 'meta' argument with a default value
        score: Optional[float] = None,
        summary: Optional[str] = None,
        dist: Optional[float] = None,
    ) -> None:
        self.message = message
        self.meta = (
            meta if meta is not None else {}
        )  # Use the provided value or an empty dictionary
        self.score = score
        self.summary = summary
        self.dist = dist


class APIError:
    """
    Represents an API error.

    Attributes
    ----------
    code : int
        The error code associated with the API error.
    message : str
        The error message associated with the API error.
    """

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
