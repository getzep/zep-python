from __future__ import annotations

import asyncio
from functools import wraps
from typing import Any, Callable, Protocol, TypeVar

T = TypeVar("T", bound=Callable[..., Any], covariant=True)


class WrappedProtocol(
    Protocol[T],
):
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        ...


# Decorator that allows us to call async functions synchronously.
# TODO: Fix this type issue. Can't be covariant.
def sync(coro: T) -> WrappedProtocol[T]:  # type: ignore
    @wraps(coro)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(coro(*args, **kwargs))

    return wrapper
