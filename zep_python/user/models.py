from datetime import datetime
from typing import Any, Dict, Optional
from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    """
    Represents a user object with a unique identifier, metadata,
    and other attributes.

    Attributes
    ----------
    uuid : UUID
        A unique identifier for the user.
    id : int
        The ID of the user. Used as a cursor for pagination.
    created_at : datetime
        The timestamp when the user was created.
    updated_at : datetime
        The timestamp when the user was last updated.
    deleted_at : Optional[datetime]
        The timestamp when the user was deleted.
    user_id : str
        The unique identifier of the user.
    email : str
        The email of the user.
    first_name : str
        The first name of the user.
    last_name : str
        The last name of the user.
    metadata : Dict[str, Any]
        The metadata associated with the user.
    """

    uuid: UUID
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    user_id: str
    email: str
    first_name: str
    last_name: str
    metadata: Dict[str, Any]


class CreateUserRequest(BaseModel):
    """
    Represents a request to create a user.

    Attributes
    ----------
    user_id : str
        The unique identifier of the user.
    email : str
        The email of the user.
    first_name : str
        The first name of the user.
    last_name : str
        The last name of the user.
    metadata : Dict[str, Any]
        The metadata associated with the user.
    """

    user_id: str
    email: str
    first_name: str
    last_name: str
    metadata: Dict[str, Any]


class UpdateUserRequest(BaseModel):
    """
    Represents a request to update a user.

    Attributes
    ----------
    uuid : UUID
        A unique identifier for the user.
    user_id : str
        The unique identifier of the user.
    email : str
        The email of the user.
    first_name : str
        The first name of the user.
    last_name : str
        The last name of the user.
    metadata : Dict[str, Any]
        The metadata associated with the user.
    """

    uuid: UUID
    user_id: str
    email: str
    first_name: str
    last_name: str
    metadata: Dict[str, Any]
