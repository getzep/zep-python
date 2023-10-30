from __future__ import annotations

import warnings
from types import TracebackType
from typing import Any, Callable, Dict, List, Optional, Type
from urllib.parse import urljoin

import httpx
from packaging.version import InvalidVersion, Version

from zep_python.document.client import DocumentClient
from zep_python.exceptions import APIError
from zep_python.memory.client import MemoryClient
from zep_python.memory.models import (
    Memory,
    MemorySearchPayload,
    MemorySearchResult,
    Session,
)
from zep_python.user.client import UserClient

API_BASE_PATH = "/api/v1"
API_TIMEOUT = 10

MINIMUM_SERVER_VERSION = "0.17.0"


class ZepClient:
    """
    ZepClient class implementation.

    Attributes
    ----------
    base_url : str
        The base URL of the API.
    memory : MemoryClient
        The client used for making Memory API requests.
    document : DocumentClient
        The client used for making Document API requests.

    Methods
    -------
    get_memory(session_id: str, lastn: Optional[int] = None) -> List[Memory]:
        Retrieve memory for the specified session. (Deprecated)
    add_memory(session_id: str, memory_messages: Memory) -> str:
        Add memory to the specified session. (Deprecated)
    delete_memory(session_id: str) -> str:
        Delete memory for the specified session. (Deprecated)
    search_memory(session_id: str, search_payload: SearchPayload,
                  limit: Optional[int] = None) -> List[SearchResult]:
        Search memory for the specified session. (Deprecated)
    close() -> None:
        Close the HTTP client.
    """

    base_url: str
    memory: MemoryClient
    document: DocumentClient
    user: UserClient

    def __init__(self, base_url: str, api_key: Optional[str] = None) -> None:
        """
        Initialize the ZepClient with the specified base URL.

        Parameters
        ----------
        base_url : str
            The base URL of the API.

        api_key : Optional[str]
            The API key to use for authentication. (optional)
        """

        headers: Dict[str, str] = {}
        if api_key is not None:
            headers["Authorization"] = f"Bearer {api_key}"

        self.base_url = concat_url(base_url, API_BASE_PATH)
        self.aclient = httpx.AsyncClient(
            base_url=self.base_url, headers=headers, timeout=API_TIMEOUT
        )
        self.client = httpx.Client(
            base_url=self.base_url, headers=headers, timeout=API_TIMEOUT
        )

        self._healthcheck(base_url)

        self.memory = MemoryClient(self.aclient, self.client)
        self.document = DocumentClient(self.aclient, self.client)
        self.user = UserClient(self.aclient, self.client)

    def _healthcheck(self, base_url: str) -> None:
        """
        Check that the Zep server is running, the API URL is correct,
        and that the server version is compatible with this client.

        Raises
        ------
        ConnectionError
            If the server is not running or the API URL is incorrect.
        """

        url = concat_url(base_url, "/healthz")

        error_msg = """Failed to connect to Zep server. Please check that:
         - the server is running 
         - the API URL is correct
         - No other process is using the same port
         """

        try:
            response = httpx.get(url)
            if response.status_code != 200 or response.text != ".":
                raise APIError(response, error_msg)

            zep_server_version_str = response.headers.get("X-Zep-Version")
            if zep_server_version_str:
                if "dev" in zep_server_version_str:
                    return

                zep_server_version = parse_version_string(zep_server_version_str)
            else:
                zep_server_version = Version("0.0.0")

            if zep_server_version < Version(MINIMUM_SERVER_VERSION):
                warnings.warn(
                    (
                        "You are using an incompatible Zep server version. Please"
                        f" upgrade to {MINIMUM_SERVER_VERSION} or later."
                    ),
                    Warning,
                    stacklevel=2,
                )
        except (httpx.ConnectError, httpx.NetworkError, httpx.TimeoutException) as e:
            raise APIError(None, error_msg) from e

    async def __aenter__(self) -> "ZepClient":
        """Asynchronous context manager entry point"""
        return self

    async def __aexit__(
        self,
        exc_type: Type[Exception],
        exc_val: Exception,
        exc_tb: TracebackType,
    ) -> None:
        """Asynchronous context manager exit point"""
        await self.aclose()

    def __enter__(self) -> "ZepClient":
        """Sync context manager entry point"""
        return self

    def __exit__(
        self,
        exc_type: Type[Exception],
        exc_val: Exception,
        exc_tb: TracebackType,
    ) -> None:
        """Sync context manager exit point"""
        self.close()

    # Facade methods for Memory API
    def get_session(self, session_id: str) -> Session:
        deprecated_warning(self.get_session)
        return self.memory.get_session(session_id)

    async def aget_session(self, session_id: str) -> Session:
        deprecated_warning(self.aget_session)
        return await self.memory.aget_session(session_id)

    def add_session(self, session: Session) -> Session:
        deprecated_warning(self.add_session)
        return self.memory.add_session(session)

    async def aadd_session(self, session: Session) -> Session:
        deprecated_warning(self.aadd_session)
        return await self.memory.aadd_session(session)

    def get_memory(self, session_id: str, lastn: Optional[int] = None) -> Memory:
        deprecated_warning(self.get_memory)
        return self.memory.get_memory(session_id, lastn)

    async def aget_memory(self, session_id: str, lastn: Optional[int] = None) -> Memory:
        deprecated_warning(self.aget_memory)
        return await self.memory.aget_memory(session_id, lastn)

    def add_memory(self, session_id: str, memory_messages: Memory) -> str:
        deprecated_warning(self.add_memory)
        return self.memory.add_memory(session_id, memory_messages)

    async def aadd_memory(self, session_id: str, memory_messages: Memory) -> str:
        deprecated_warning(self.aadd_memory)
        return await self.memory.aadd_memory(session_id, memory_messages)

    def delete_memory(self, session_id: str) -> str:
        deprecated_warning(self.delete_memory)
        return self.memory.delete_memory(session_id)

    async def adelete_memory(self, session_id: str) -> str:
        deprecated_warning(self.adelete_memory)
        return await self.memory.adelete_memory(session_id)

    def search_memory(
        self,
        session_id: str,
        search_payload: MemorySearchPayload,
        limit: Optional[int] = None,
    ) -> List[MemorySearchResult]:
        deprecated_warning(self.search_memory)
        return self.memory.search_memory(session_id, search_payload, limit)

    async def asearch_memory(
        self,
        session_id: str,
        search_payload: MemorySearchPayload,
        limit: Optional[int] = None,
    ) -> List[MemorySearchResult]:
        deprecated_warning(self.asearch_memory)
        return await self.memory.asearch_memory(session_id, search_payload, limit)

    # Close the HTTP client
    async def aclose(self) -> None:
        """
        Asynchronously close the HTTP client.

        [Optional] This method may be called when the ZepClient is no longer needed to
        release resources.
        """
        await self.aclient.aclose()

    def close(self) -> None:
        """
        Close the HTTP client.

        [Optional] This method may be called when the ZepClient is no longer needed to
        release resources.
        """
        self.client.close()


def concat_url(base_url: str, path: str) -> str:
    """
    Join the specified base URL and path.

    Parameters
    ----------
    base_url : str
        The base URL to join.
    path : str
        The path to join.

    Returns
    -------
    str
        The joined URL.
    """
    base_url = base_url.rstrip("/")
    return urljoin(base_url + "/", path.lstrip("/"))


def deprecated_warning(func: Callable[..., Any]) -> Callable[..., Any]:
    warnings.warn(
        (
            f"{func.__name__} method from the base client path is deprecated, "
            "please use the corresponding method from zep_python.memory instead"
        ),
        DeprecationWarning,
        stacklevel=3,
    )
    return func


def parse_version_string(version_string: str) -> Version:
    """
    Parse a string into a Version object.

    Parameters
    ----------
    version_string : str
        The version string to parse.

    Returns
    -------
    Version
        The parsed version.
    """

    try:
        if "-" in version_string:
            version_str = version_string.split("-")[0]
            return Version(version_str if version_str else "0.0.0")
    except InvalidVersion:
        return Version("0.0.0")

    return Version("0.0.0")
