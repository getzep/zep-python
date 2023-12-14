from typing import TYPE_CHECKING, Any, Dict, Optional
from uuid import UUID

if TYPE_CHECKING:
    from pydantic import BaseModel, Field
else:
    try:
        from pydantic.v1 import BaseModel, Field
    except ImportError:
        from pydantic import BaseModel, Field


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
    metadata: Optional[Dict[str, Any]] = Field(optional=True, default=None)

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the message.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the attributes of the message.
        """
        return self.dict()


class UpdateMessageMetadataRequest(BaseModel):
    """
    Represents a request to update a user.

    Attributes
    ----------
    uuid : UUID
        A unique identifier for the message.
    session_id : str
        A unique identifier for the session.
    metadata : Dict[str, Any]
        The metadata associated with the message.
    """

    uuid: UUID
    session_id: str
    metadata: Dict[str, Any]
