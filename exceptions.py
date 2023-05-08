from typing import Optional  

class ZepClientError(Exception):
    """Base exception class for ZepClient errors."""
    def __init__(self, message: str, response_data: Optional[dict] = None):
        super().__init__(message)
        self.response_data = response_data

class UnexpectedResponseError(ZepClientError):
    """Raised when the API response format is unexpected."""

    def __init__(self, message: str):
        super().__init__(message)