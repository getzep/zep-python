from zep.core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zep.base_user.client import BaseUserClient, AsyncBaseUserClient


class UserClient(BaseUserClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )


class AsyncUserClient(AsyncBaseUserClient):
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )
