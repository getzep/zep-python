from zep_python.core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zep_python.user.client import UserClient as BaseUserClient, AsyncUserClient as AsyncBaseUserClient


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