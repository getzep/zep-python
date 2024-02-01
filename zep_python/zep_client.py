from __future__ import annotations

import warnings
from types import TracebackType
from typing import Dict, Optional, Type
from urllib.parse import urljoin

import httpx
from packaging.version import InvalidVersion, Version

from zep_python.document.client import DocumentClient
from zep_python.exceptions import APIError
from zep_python.memory.client import MemoryClient
from zep_python.message.client import MessageClient
from zep_python.user.client import UserClient

API_URL = "https://api.getzep.com"
API_BASE_PATH = "/api/v2"
API_TIMEOUT = 10

MINIMUM_SERVER_VERSION = "0.22.0"


class ZepClient:
    """
    ZepClient class implementation.

    Attributes
    ----------
    api_url : str
        The Zep API service URL.
    memory : MemoryClient
        The client used for making Memory API requests.
    document : DocumentClient
        The client used for making Document API requests.
    user : UserClient
        The client used for making User API requests.

    Methods
    -------
    close() -> None:
        Close the HTTP client.
    """

    api_url: str
    memory: MemoryClient
    document: DocumentClient
    user: UserClient

    def __init__(
        self,
        api_url: Optional[str] = None,
        api_key: Optional[str] = None,
    ) -> None:
        """
        Initialize the ZepClient with the specified base URL.

        Parameters
        ----------

        api_url : Optional[str]
            The base URL of the API. (optional)

        api_key : Optional[str]
            The API key to use for authentication. (optional)
        """

        # Zep Cloud API keys start with "z_". A url is not required for Zep Cloud.
        # Zep Open Source API keys do not start with "z_". A url is required for
        # Zep On-Premise. Check if both zep_url and api_key are None
        if api_url is None and api_key is None:
            raise ValueError("Please provide an api_key to access the Zep service.")
        # Check if api_key is not None and doesn't start with "z_" and zep_url is None
        elif api_key and not api_key.startswith("z_") and api_url is None:
            raise ValueError(
                "Please provide the zep_url which is the address of your Zep service."
            )

        self.api_key = api_key
        headers: Dict[str, str] = {}
        if api_key and api_key.startswith("z_"):
            headers["Authorization"] = f"Api-Key {api_key}"
        elif api_key is not None:
            headers["Authorization"] = f"Bearer {api_key}"

        if api_url is None:
            self._healthcheck(API_URL)
            self.api_url = concat_url(API_URL, API_BASE_PATH)
        else:
            self._healthcheck(api_url)
            self.api_url = concat_url(api_url, API_BASE_PATH)

        self.aclient = httpx.AsyncClient(
            base_url=self.api_url, headers=headers, timeout=API_TIMEOUT
        )
        self.client = httpx.Client(
            base_url=self.api_url, headers=headers, timeout=API_TIMEOUT
        )

        self.memory = MemoryClient(self.aclient, self.client)
        self.message = MessageClient(self.aclient, self.client)
        self.document = DocumentClient(self.aclient, self.client)
        self.user = UserClient(self.aclient, self.client)

    def _healthcheck(self, base_url: str) -> None:
        """
        Check that the Zep service is running, the API URL is correct,
        and that the server version is compatible with this client.

        Raises
        ------
        ConnectionError
            If the server is not running or the API URL is incorrect.
        """

        url = concat_url(base_url, "/healthz")

        error_msg = """Failed to connect to Zep server. Please check that:
         - the status of the service 
         - your internet connection is working
         - the API URL is correct (not required for Zep Cloud)
         - No other process is using the same port (not required for Zep Cloud)
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

            if (
                zep_server_version < Version(MINIMUM_SERVER_VERSION)
                and self.api_key is None
            ):
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
