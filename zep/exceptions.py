from __future__ import annotations

from typing import Any, Dict, Optional


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
        self.response_data = response_data


class APIError(ZepClientError):
    """
    Raised when the API response format is unexpected.

    Inherits from ZepClientError.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


class NotFoundError(ZepClientError):
    """
    Raised when the API response contains no results.

    Inherits from ZepClientError.
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)
