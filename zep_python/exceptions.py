from __future__ import annotations

from typing import Any, Dict, Optional, Union

import httpx


class ZepClientError(Exception):
    """
    Base exception class for ZepClient errors.

    Attributes
    ----------
    message : str
        The error message associated with the ZepClient error.
    response_data : Optional[dict]
        The response data associated with the ZepClient error.

    Parameters
    ----------
    message : str
        The error message to be set for the exception.
    response_data : Optional[dict], optional
        The response data to be set for the exception, by default None.
    """

    def __init__(
        self, message: str, response_data: Optional[Dict[Any, Any]] = None
    ) -> None:
        super().__init__(message)
        self.message = message
        self.response_data = response_data

    def __str__(self):
        return f"{self.message}: {self.response_data}"


class APIError(ZepClientError):
    """
    Raised when the API response format is unexpected.

    Inherits from ZepClientError.
    """

    def __init__(
        self, response: Union[httpx.Response, None] = None, message: str = "API error"
    ) -> None:
        if response:
            response_data = {
                "status_code": response.status_code,
                "message": response.text,
            }
        else:
            response_data = None
        super().__init__(message=message, response_data=response_data)


class AuthError(ZepClientError):
    """
    Raised when API authentication fails.

    Inherits from APIError.
    """

    def __init__(
        self,
        response: Union[httpx.Response, None] = None,
        message: str = "Authentication Failed. Please check your API key is valid",
    ) -> None:
        if response:
            response_data = {
                "status_code": response.status_code,
                "message": response.text,
            }
        else:
            response_data = None
        super().__init__(message=message, response_data=response_data)


class NotFoundError(ZepClientError):
    """
    Raised when the API response contains no results.

    Inherits from ZepClientError.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


def handle_response(
    response: httpx.Response, missing_doc: Optional[str] = None
) -> None:
    missing_doc = missing_doc or "No query results found"
    if response.status_code == 404:
        raise NotFoundError(missing_doc)

    if response.status_code == 401:
        raise AuthError(response)

    if not (200 <= response.status_code <= 299):
        raise APIError(response)
