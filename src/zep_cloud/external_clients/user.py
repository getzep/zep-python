from zep_cloud.core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zep_cloud.user.client import AsyncUserClient as AsyncBaseUserClient
from zep_cloud.user.client import UserClient as BaseUserClient


class UserClient(BaseUserClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)


class AsyncUserClient(AsyncBaseUserClient):
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)
