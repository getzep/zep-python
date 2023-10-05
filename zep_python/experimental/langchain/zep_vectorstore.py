from __future__ import annotations

from typing import (
    Any,
    Dict,
    List,
    Optional,
)


class DeprecationError(Exception):
    pass


class ZepVectorStore:
    def __init__(
        self,
        collection: Any,
        texts: Optional[List[str]] = None,
        metadata: Optional[List[Dict[str, Any]]] = None,
        embedding: Optional[Any] = None,
        **kwargs: Any,
    ) -> None:
        raise DeprecationError(
            "This experimental class has been deprecated. Please use the "
            "official ZepVectorStore class in the Langchain package."
        )
