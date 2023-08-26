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
    uuid : Optional[UUID]
        A unique identifier for the user. Used internally as a primary key.
    id : Optional[int]
        The ID of the user. Used as a cursor for pagination.
    created_at : Optional[datetime]
        The timestamp when the user was created.
    updated_at : Optional[datetime]
        The timestamp when the user was last updated.
    deleted_at : Optional[datetime]
        The timestamp when the user was deleted.
    user_id : str
        The unique identifier of the user.
    email : Optional[str]
        The email of the user.
    first_name : Optional[str]
        The first name of the user.
    last_name : Optional[str]
        The last name of the user.
    metadata : Optional[Dict[str, Any]]
        The metadata associated with the user.
    """

    uuid: Optional[UUID] = None
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    user_id: str
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class CreateUserRequest(BaseModel):
    """
    Represents a request to create a user.

    Attributes
    ----------
    user_id : str
        The unique identifier of the user.
    email : Optional[str]
        The email of the user.
    first_name : Optional[str]
        The first name of the user.
    last_name : Optional[str]
        The last name of the user.
    metadata : Optional[Dict[str, Any]]
        The metadata associated with the user.
    """

    user_id: str
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class UpdateUserRequest(BaseModel):
    """
    Represents a request to update a user.

    Attributes
    ----------
    uuid : Optional[UUID]
        A unique identifier for the user.
    user_id : str
        The unique identifier of the user.
    email : Optional[str]
        The email of the user.
    first_name : Optional[str]
        The first name of the user.
    last_name : Optional[str]
        The last name of the user.
    metadata : Optional[Dict[str, Any]]
        The metadata associated with the user.
    """

    uuid: Optional[UUID] = None
    user_id: str
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
