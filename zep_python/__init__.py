import warnings

from zep_python.exceptions import APIError, NotFoundError
from zep_python.zep_client import ZepClient


def deprecated_import():
    warnings.warn(
        (
            "Importing memory classes from the base client path is deprecated, "
            "please import from zep_python.memory instead."
        ),
        DeprecationWarning,
        stacklevel=2,
    )
    from zep_python.memory.models import (
        Memory,
        MemorySearchPayload,
        MemorySearchResult,
        Message,
        Session,
        Summary,
    )

    return Memory, MemorySearchPayload, MemorySearchResult, Message, Session, Summary


(
    Memory,
    MemorySearchPayload,
    MemorySearchResult,
    Message,
    Session,
    Summary,
) = deprecated_import()

__all__ = [
    "ZepClient",
    "Memory",
    "Message",
    "MemorySearchPayload",
    "APIError",
    "NotFoundError",
    "MemorySearchResult",
    "Summary",
    "Session",
]
