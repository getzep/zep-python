from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, Extra


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

    uuid: Optional[str] = Field(default=None)
    created_at: Optional[datetime] = Field(const=True)
    updated_at: Optional[datetime] = Field(const=True)
    document_id: Optional[str] = None
    content: str = Field(..., min_length=1)
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    is_embedded: Optional[bool] = Field(default=None)
    embedding: Optional[List[float]] = Field(default=None)
    dist: Optional[float] = Field(const=True)

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
    uuid : str
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

    uuid: Optional[str] = Field(default=None)
    created_at: Optional[datetime] = Field(const=True)
    updated_at: Optional[datetime] = Field(const=True)
    name: str = Field(
        ...,
        min_length=5,
        max_length=45,
        regex="^[a-zA-Z0-9_-]*$",
    )
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    embedding_dimensions: Optional[int] = Field(ge=1, le=2000)  # not required on update
    is_auto_embedded: Optional[bool] = Field(const=True, default=True)
    is_indexed: Optional[bool] = Field(const=True)
    document_count: Optional[int] = Field(const=True)
    document_embedded_count: Optional[int] = Field(const=True)

    class Config:
        extra = Extra.forbid

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the document collection.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the attributes of the document collection.
        """
        return self.dict()