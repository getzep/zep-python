from enum import Enum
from typing import Any, Dict, Optional
from uuid import UUID

from pydantic import BaseModel, Field, validator


class RoleType(str, Enum):
    USER_ROLE = "user"
    ASSISTANT_ROLE = "assistant"
    SYSTEM_ROLE = "system"
    FUNCTION_ROLE = "function"
    TOOL_ROLE = "tool"
    NO_ROLE = "norole"


def get_zep_message_role_type(role):
    if role == "human":
        return RoleType.USER_ROLE
    elif role == "ai":
        return RoleType.ASSISTANT_ROLE
    elif role == "system":
        return RoleType.SYSTEM_ROLE
    elif role == "function":
        return RoleType.FUNCTION_ROLE
    elif role == "tool":
        return RoleType.TOOL_ROLE
    elif role == "norole":
        return RoleType.NO_ROLE
    else:
        return RoleType.NO_ROLE


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
    role_type: RoleType
        The type of the role (e.g., "user", "system").
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
    role_type: RoleType = Field("A role type is required")
    content: str = Field("Content is required")
    uuid: Optional[str] = Field(default=None)
    created_at: Optional[str] = Field(default=None)
    token_count: Optional[int] = Field(default=None)
    metadata: Optional[Dict[str, Any]] = Field(default=None)

    @validator("role_type")
    def validate_role_type(cls, v):
        if isinstance(v, RoleType):
            return v
        if v not in RoleType._value2member_map_:
            raise ValueError(f"Invalid role type: {v}")
        return v

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the message.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the attributes of the message.
        """
        return self.model_dump(exclude_unset=True, exclude_none=True)


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
