from .base_client import BaseClient, AsyncBaseClient
import typing
import os
import httpx
from .external_clients.memory import MemoryClient, AsyncMemoryClient
from .external_clients.user import UserClient, AsyncUserClient

api_suffix = "api/v2"


class Zep(BaseClient):
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        api_key: typing.Optional[str] = os.getenv("ZEP_API_KEY"),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = None,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        api_url = ""
        env_api_url = os.getenv("ZEP_API_URL")
        if env_api_url:
            api_url = f"{env_api_url}/{api_suffix}"
        else:
            api_url = f"{base_url}/{api_suffix}"
        super().__init__(
            base_url=api_url,
            api_key=api_key,
            timeout=timeout,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
        )
        self.memory = MemoryClient(client_wrapper=self._client_wrapper)
        self.user = UserClient(client_wrapper=self._client_wrapper)


class AsyncZep(AsyncBaseClient):
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        api_key: typing.Optional[str] = os.getenv("ZEP_API_KEY"),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = None,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        api_url = ""
        env_api_url = os.getenv("ZEP_API_URL")
        if env_api_url:
            api_url = f"{env_api_url}/{api_suffix}"
        else:
            api_url = f"{base_url}/{api_suffix}"
        super().__init__(
            base_url=api_url,
            api_key=api_key,
            timeout=timeout,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
        )
        self.memory = AsyncMemoryClient(client_wrapper=self._client_wrapper)
        self.user = AsyncUserClient(client_wrapper=self._client_wrapper)
