from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

from zep_python.message.models import Message


class SearchScope(str, Enum):
    messages = "messages"
    summary = "summary"


class Session(BaseModel):
    """
    Represents a session object with a unique identifier, metadata,
    and other attributes.

    Attributes
    ----------
    uuid : Optional[str]
        A unique identifier for the session.
        This is generated server-side and is not expected to be present on creation.
    created_at : str
        The timestamp when the session was created.
        Generated by the server.
    updated_at : str
        The timestamp when the session was last updated.
        Generated by the server.
    deleted_at : Optional[datetime]
        The timestamp when the session was deleted.
        Generated by the server.
    session_id : str
        The unique identifier of the session.
    metadata : Dict[str, Any]
        The metadata associated with the session.
    """

    uuid: Optional[str] = None
    id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    session_id: str
    user_id: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


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
        return self.model_dump(exclude_unset=True, exclude_none=True)


class Memory(BaseModel):
    """
    Represents a memory object with messages, metadata, and other attributes.

    Attributes
    ----------
    messages : Optional[List[Message]]
        A list of message objects, where each message contains a role and content.
    metadata : Optional[Dict[str, Any]]
        A dictionary containing metadata associated with the memory.
    summary : Optional[Summary]
        A Summary object.
    uuid : Optional[str]
        A unique identifier for the memory.
    created_at : Optional[str]
        The timestamp when the memory was created.
    token_count : Optional[int]
        The token count of the memory.

    Methods
    -------
    to_dict() -> Dict[str, Any]:
        Returns a dictionary representation of the message.
    """

    messages: Optional[List[Message]] = Field(
        default=[],
        description="A List of Messages or empty List is required",
    )
    metadata: Optional[Dict[str, Any]] = Field(default=None)
    summary: Optional[Summary] = Field(default=None)
    uuid: Optional[str] = Field(default=None)
    created_at: Optional[str] = Field(default=None)
    token_count: Optional[int] = Field(default=None)

    def to_dict(self) -> Dict[str, Any]:
        return self.model_dump(exclude_unset=True, exclude_none=True)


class MemorySearchPayload(BaseModel):
    """
    Represents a search payload for querying memory.

    Attributes
    ----------
    metadata : Dict[str, Any]
        Metadata associated with the search query.
    text : str
        The text of the search query.
    search_scope : Optional[str]
        Search over messages or summaries. Defaults to "messages".
        Must be one of "messages" or "summary".
    search_type : Optional[str]
        The type of search to perform. Defaults to "similarity".
        Must be one of "similarity" or "mmr".
    mmr_lambda : Optional[float]
        The lambda parameter for the MMR Reranking Algorithm.
    """

    text: Optional[str] = Field(default=None)
    metadata: Optional[Dict[str, Any]] = Field(default=None)
    search_scope: Optional[str] = Field(default="messages")
    search_type: Optional[str] = Field(default="similarity")
    mmr_lambda: Optional[float] = Field(default=None)


class MemorySearchResult(BaseModel):
    """
    Represents a search result from querying memory.

    Attributes
    ----------
    message : Optional[Message]
        The message matched by search.
    summary : Optional[Summary]
        The summary matched by search.
    metadata : Optional[Dict[str, Any]]
        Metadata associated with the search result.
    dist : Optional[float]
        The distance metric of the search result.
    """

    message: Optional[Message] = None
    summary: Optional[Summary] = None
    metadata: Optional[Dict[str, Any]] = None
    dist: Optional[float] = None
