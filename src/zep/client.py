from typing import Iterator, Optional, Union, \
    Optional, AsyncIterator
from .base_client import \
    BaseClient, AsyncBaseClient
import typing
import json
import re
import os
import httpx
from .environment import BaseClientEnvironment
from .memory import MemoryClient


class Zep(BaseClient):
    def __init__(
            self,
            *,
            base_url: typing.Optional[str] = None,
            environment: BaseClientEnvironment = BaseClientEnvironment.DEFAULT,
            api_key: typing.Optional[str] = os.getenv("ZEP_API_KEY"),
            timeout: typing.Optional[float] = None,
            follow_redirects: typing.Optional[bool] = None,
            httpx_client: typing.Optional[httpx.Client] = None
    ):
        super().__init__(
            base_url=base_url,
            environment=environment,
            api_key=api_key,
            timeout=timeout,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client
        )
        self.memory = MemoryClient(client_wrapper=self._client_wrapper)
