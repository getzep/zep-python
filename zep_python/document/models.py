from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from ..utils import SearchType


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
    score : Optional[float]
        The normed score of the search result. Available only
        when the document is returned as part of a query result.
    """

    uuid: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    document_id: Optional[str] = Field(default=None, max_length=100)
    content: str = Field(..., min_length=1)
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    is_embedded: Optional[bool] = None
    embedding: Optional[List[float]] = None
    score: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the document.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the attributes of the document.
        """
        return self.model_dump()


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

    uuid: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    name: str = Field(
        ...,
        min_length=5,
        max_length=40,
        pattern="^[a-zA-Z0-9_-]*$",
    )
    description: Optional[str] = Field(default=None, max_length=1000)
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
    embedding_dimensions: Optional[int] = Field(ge=8, le=2000, default=None)
    is_auto_embedded: Optional[bool] = True
    is_indexed: Optional[bool] = None
    document_count: Optional[int] = None
    document_embedded_count: Optional[int] = None
    is_normalized: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the document collection.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the attributes of the document collection.
        """
        return self.model_dump()


class DocumentSearchPayload(BaseModel):
    """
    Represents a search payload for querying documents.

    Attributes
    ----------
    text : Optional[str]
        The text of the search query.
    metadata : Optional[Dict[str, Any]]
        Metadata associated with the search query.
    type : SearchType
        The type of search to perform.
    mmr_lambda : Optional[float]
        The lambda parameter for the MMR Reranking Algorithm.
    """

    text: Optional[str] = Field(default=None)
    metadata: Optional[Dict[str, Any]] = Field(default=None)
    search_type: Optional[SearchType] = Field(default="similarity")
    mmr_lambda: Optional[float] = Field(default=None)
