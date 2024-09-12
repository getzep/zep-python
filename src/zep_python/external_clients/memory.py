import datetime
import json
import typing
from packaging import version

import pydantic

from zep_python.core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zep_python.memory.client import (
    AsyncMemoryClient as AsyncBaseMemoryClient,
)
from zep_python.memory.client import (
    MemoryClient as BaseMemoryClient,
)

MIN_PYDANTIC_VERSION = "2.0"


class MemoryClient(BaseMemoryClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)


class AsyncMemoryClient(AsyncBaseMemoryClient):
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)
