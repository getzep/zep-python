from zep.core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zep.base_memory.client import BaseMemoryClient, AsyncBaseMemoryClient


class MemoryClient(BaseMemoryClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )


class AsyncMemoryClient(AsyncBaseMemoryClient):
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )
