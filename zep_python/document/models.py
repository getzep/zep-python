from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field, root_validator


def create_root_validator(allowed_on_create, allowed_on_update):
    @root_validator(pre=True, allow_reuse=True)
    def check_fields(cls, values):
        operation = values.get("operation")

        if operation is None:
            operation = "create"
        else:
            del values["operation"]

        if operation == "create":
            for field in values:
                if field not in allowed_on_create:
                    raise ValueError(f"{field} is not allowed for create operation")

        elif operation == "update":
            for field in values:
                if field not in allowed_on_update:
                    raise ValueError(f"{field} is not allowed for update operation")

        return values

    return check_fields


class Document(BaseModel):
    """
    Represents a document base.

    Attributes
    ----------
    uuid : Optional[str]
        The unique identifier of the document.
    created_at : Optional[datetime]
        The timestamp of when the document was created.
    updated_at : Optional[datetime]
        The timestamp of when the document was last updated.
    document_id : Optional[str]
        The unique identifier of the document (name or some id).
    content : str
        The content of the document.
    metadata : Optional[Dict[str, Any]]
        Any additional metadata associated with the document.
    is_embedded : Optional[bool]
        Whether the document has an embedding.
    embedding : Optional[List[float]]
        The embedding of the document.
    dist : Optional[float]
        The distance of the document from the query document. Available only
        when the document is returned as part of a query result.
    """

    uuid: UUID = Field(const=True)
    created_at: Optional[datetime] = Field(const=True)
    updated_at: Optional[datetime] = Field(const=True)
    document_id: Optional[str] = None
    content: str = Field(..., min_length=1)
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    is_embedded: bool = Field(const=True)
    embedding: Optional[List[float]] = Field(const=True)
    dist: Optional[float] = Field(const=True)

    _ = create_root_validator(
        allowed_on_create=["document_id", "content", "metadata", "embedding"],
        allowed_on_update=["uuid", "document_id", "metadata"],
    )

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the document.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the attributes of the document.
        """
        return self.dict()


class DocumentCollectionModel(BaseModel):
    """
    Represents a collection of documents.

    Attributes
    ----------
    uuid : UUID
        The unique identifier of the collection.
    created_at : Optional[datetime]
        The timestamp of when the collection was created.
    updated_at : Optional[datetime]
        The timestamp of when the collection was last updated.
    name : str
        The unique name of the collection.
    description : Optional[str]
        The description of the collection.
    metadata : Optional[Dict[str, Any]]
        Any additional metadata associated with the collection.
    embedding_dimensions : int
        The dimensions of the embedding model.
    is_auto_embedded : bool
        Flag to indicate whether the documents in the collection should be
        automatically embedded by Zep. (Default: True)
    is_indexed : bool
        Flag indicating whether an index has been created for this collection.
    """

    uuid: Optional[UUID] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    name: str = Field(..., min_length=5, max_length=45, regex="^[a-zA-Z0-9_-]*$")
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    embedding_dimensions: int
    is_auto_embedded: Optional[bool] = True
    is_indexed: Optional[bool] = None
    document_count: Optional[int] = None
    document_embedded_count: Optional[int] = None

    _ = create_root_validator(
        allowed_on_create=[
            "name",
            "description",
            "metadata",
            "embedding_dimensions",
            "is_auto_embedded",
        ],
        allowed_on_update=["uuid", "description", "metadata"],
    )

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the document collection.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the attributes of the document collection.
        """
        return self.dict()
