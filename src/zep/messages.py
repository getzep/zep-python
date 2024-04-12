from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .base_messages.client import BaseMessagesClient, AsyncBaseMessagesClient


class MessagesClient(BaseMessagesClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )


class AsyncMessagesClient(AsyncBaseMessagesClient):
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )
