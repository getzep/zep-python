"""Minimal generated-client shapes produced by the selective v4 contract."""

from typing import Any, Optional

from zep_cloud.core.http_client import AsyncHttpClient, HttpClient
from zep_cloud.core.request_options import RequestOptions


class GeneratedSyncIdempotencyFixture:
    def __init__(self, http_client: HttpClient) -> None:
        self._http_client = http_client

    def mutation(
        self,
        *,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        return self._http_client.request(
            path="mutation",
            method="POST",
            headers={"Idempotency-Key": idempotency_key},
            request_options=request_options,
        )

    def get_read(self) -> Any:
        return self._http_client.request(path="read", method="GET", headers={})

    def post_read(self) -> Any:
        return self._http_client.request(path="read/search", method="POST", headers={})


class GeneratedAsyncIdempotencyFixture:
    def __init__(self, http_client: AsyncHttpClient) -> None:
        self._http_client = http_client

    async def mutation(
        self,
        *,
        idempotency_key: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
    ) -> Any:
        return await self._http_client.request(
            path="mutation",
            method="POST",
            headers={"Idempotency-Key": idempotency_key},
            request_options=request_options,
        )

    async def get_read(self) -> Any:
        return await self._http_client.request(path="read", method="GET", headers={})

    async def post_read(self) -> Any:
        return await self._http_client.request(path="read/search", method="POST", headers={})
