# Apply monkey patch for default retries
from .core.http_client import AsyncHttpClient, HttpClient
from .core.request_options import RequestOptions

# Store the original methods
original_async_request = AsyncHttpClient.request
original_sync_request = HttpClient.request

# Global default retry count
DEFAULT_MAX_RETRIES = 5

async def patched_async_request(self, *args, **kwargs):
    # If no request_options provided, create one with default retries
    if 'request_options' not in kwargs or kwargs['request_options'] is None:
        kwargs['request_options'] = RequestOptions(max_retries=DEFAULT_MAX_RETRIES)
    # If request_options exists but no max_retries set, add default
    elif getattr(kwargs['request_options'], 'max_retries', None) is None:
        # Create new RequestOptions with existing data plus default retries
        existing_options = kwargs['request_options'].__dict__ if hasattr(kwargs['request_options'], '__dict__') else {}
        kwargs['request_options'] = RequestOptions(max_retries=DEFAULT_MAX_RETRIES, **existing_options)
    
    return await original_async_request(self, *args, **kwargs)

def patched_sync_request(self, *args, **kwargs):
    # Same logic for sync version
    if 'request_options' not in kwargs or kwargs['request_options'] is None:
        kwargs['request_options'] = RequestOptions(max_retries=DEFAULT_MAX_RETRIES)
    elif getattr(kwargs['request_options'], 'max_retries', None) is None:
        existing_options = kwargs['request_options'].__dict__ if hasattr(kwargs['request_options'], '__dict__') else {}
        kwargs['request_options'] = RequestOptions(max_retries=DEFAULT_MAX_RETRIES, **existing_options)
    
    return original_sync_request(self, *args, **kwargs)

# Apply the patches
AsyncHttpClient.request = patched_async_request  # type: ignore[method-assign]
HttpClient.request = patched_sync_request  # type: ignore[method-assign]

from .base_client import \
    BaseClient, AsyncBaseClient
import typing
import os
import httpx
from .environment import ZepEnvironment
from .external_clients.memory import MemoryClient, AsyncMemoryClient
from .external_clients.document import DocumentClient, AsyncDocumentClient
from .external_clients.user import UserClient, AsyncUserClient
from .external_clients.graph import GraphClient, AsyncGraphClient

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
        self.graph = GraphClient(client_wrapper=self._client_wrapper)

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
        self.graph = AsyncGraphClient(client_wrapper=self._client_wrapper)
