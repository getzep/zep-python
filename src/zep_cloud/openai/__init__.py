"""
External client implementations for Zep Cloud SDK.

This module provides wrapper clients for external services that integrate with Zep.
"""

from typing import TYPE_CHECKING, Any

# Import OpenAI wrapper classes (with graceful fallback if OpenAI is not installed)
try:
    from .openai_async import AsyncZepOpenAI
    from .openai_client import ZepOpenAI
    from .openai_streaming import AsyncZepStreamWrapper, ZepStreamWrapper
    from .openai_utils import ZepOpenAIError

    __all__ = [
        "ZepOpenAI",
        "AsyncZepOpenAI",
        "ZepOpenAIError",
        "ZepStreamWrapper",
        "AsyncZepStreamWrapper",
    ]
except ImportError:
    # OpenAI is not installed, provide helpful error message
    def _openai_not_installed(*args: Any, **kwargs: Any) -> Any:
        raise ImportError(
            "OpenAI is required for ZepOpenAI. Install it with: pip install openai"
        )

    if TYPE_CHECKING:
        from .openai_async import AsyncZepOpenAI
        from .openai_client import ZepOpenAI
        from .openai_streaming import AsyncZepStreamWrapper, ZepStreamWrapper
        from .openai_utils import ZepOpenAIError
    else:
        # Assign fallback functions at runtime
        ZepOpenAI = _openai_not_installed  # type: ignore
        AsyncZepOpenAI = _openai_not_installed  # type: ignore
        ZepOpenAIError = ImportError  # type: ignore
        ZepStreamWrapper = _openai_not_installed  # type: ignore
        AsyncZepStreamWrapper = _openai_not_installed  # type: ignore

    __all__ = [
        "ZepOpenAI",
        "AsyncZepOpenAI",
        "ZepOpenAIError",
        "ZepStreamWrapper",
        "AsyncZepStreamWrapper",
    ]
