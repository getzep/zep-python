from zep_cloud.core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zep_cloud.memory.client import MemoryClient as BaseMemoryClient, AsyncMemoryClient as AsyncBaseMemoryClient


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