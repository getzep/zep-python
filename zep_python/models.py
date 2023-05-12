from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Summary(BaseModel):
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

    uuid: str = Field("A uuid is required")
    created_at: str = Field("A created_at is required")
    content: str = Field("Content is required")
    recent_message_uuid: str = Field("A recent_message_uuid is required")
    token_count: int = Field("A token_count is required")

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the summary.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the attributes of the summary.
        """
        return self.dict()


class Message(BaseModel):
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

    role: str = Field("A role is required")
    content: str = Field("Content is required")
    uuid: Optional[str] = Field(optional=True, default=None)
    created_at: Optional[str] = Field(optional=True, default=None)
    token_count: Optional[int] = Field(optional=True, default=None)

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the message.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the attributes of the message.
        """
        return self.dict()


class Memory(BaseModel):
    """
    Represents a memory object with messages, metadata, and other attributes.

    :param messages: A list of message objects, where each message contains a role and
                     content.
    :type messages: Optional[List[Dict[str, Any]]]
    :param metadata: A dictionary containing metadata associated with the memory.
    :type metadata: Optional[Dict[str, Any]]
    :param summary: A Summary object.
    :type summary: Optional[Summary]
    :param uuid: A unique identifier for the memory.
    :type uuid: Optional[str]
    :param created_at: The timestamp when the memory was created.
    :type created_at: Optional[str]
    :param token_count: The token count of the memory.
    :type token_count: Optional[int]
    """

    messages: List[Message] = Field(
        default=[], description="A List of Messages or empty List is required"
    )
    metadata: Optional[Dict[str, Any]] = Field(optional=True, default=None)
    summary: Optional[Summary] = Field(optional=True, default=None)
    uuid: Optional[str] = Field(optional=True, default=None)
    created_at: Optional[str] = Field(optional=True, default=None)
    token_count: Optional[int] = Field(optional=True, default=None)

    def to_dict(self) -> Dict[str, Any]:
        return self.dict()


class SearchPayload(BaseModel):
    """
    Represents a search payload for querying memory.

    Attributes
    ----------
    meta : Dict[str, Any]
        Metadata associated with the search query.
    text : str
        The text of the search query.
    """

    text: str = Field("A text is required")
    meta: Optional[Dict[str, Any]] = Field(optional=True, default=None)


class SearchResult(BaseModel):
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

    message: Optional[Dict[str, Any]] = None
    meta: Optional[Dict[str, Any]] = None
    score: Optional[float] = None
    summary: Optional[str] = None
    dist: Optional[float] = None
