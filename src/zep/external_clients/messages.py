from zep.core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zep.messages.client import MessagesClient as BaseMessagesClient, AsyncMessagesClient as AsyncBaseMessagesClient


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