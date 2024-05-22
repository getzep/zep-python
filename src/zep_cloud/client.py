from .base_client import \
    BaseClient, AsyncBaseClient
import typing
import os
import httpx
from .environment import ZepEnvironment
from .external_clients.memory import MemoryClient, AsyncMemoryClient
from .external_clients.document import DocumentClient, AsyncDocumentClient
from .external_clients.user import UserClient, AsyncUserClient


class Zep(BaseClient):
    def __init__(
            self,
            *,
            base_url: typing.Optional[str] = None,
            environment: ZepEnvironment = ZepEnvironment.DEFAULT,
            api_key: typing.Optional[str] = os.getenv("ZEP_API_KEY"),
            timeout: typing.Optional[float] = None,
            follow_redirects: typing.Optional[bool] = None,
            httpx_client: typing.Optional[httpx.Client] = None
    ):
        env_api_url = os.getenv("ZEP_API_URL")
        if env_api_url:
            base_url = f"{env_api_url}/api/v2"
        super().__init__(
            base_url=base_url,
            environment=environment,
            api_key=api_key,
            timeout=timeout,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client
        )
        self.memory = MemoryClient(client_wrapper=self._client_wrapper)
        self.document = DocumentClient(client_wrapper=self._client_wrapper)
        self.user = UserClient(client_wrapper=self._client_wrapper)


class AsyncZep(AsyncBaseClient):
    def __init__(
            self,
            *,
            base_url: typing.Optional[str] = None,
            environment: ZepEnvironment = ZepEnvironment.DEFAULT,
            api_key: typing.Optional[str] = os.getenv("ZEP_API_KEY"),
            timeout: typing.Optional[float] = None,
            follow_redirects: typing.Optional[bool] = None,
            httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        env_api_url = os.getenv("ZEP_API_URL")
        if env_api_url:
            base_url = f"{env_api_url}/api/v2"
        super().__init__(
            base_url=base_url,
            environment=environment,
            api_key=api_key,
            timeout=timeout,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client
        )
        self.memory = AsyncMemoryClient(client_wrapper=self._client_wrapper)
        self.document = AsyncDocumentClient(client_wrapper=self._client_wrapper)
        self.user = AsyncUserClient(client_wrapper=self._client_wrapper)