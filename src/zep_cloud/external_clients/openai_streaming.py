"""
Streaming support for Zep OpenAI integration.
"""

import io
import logging
from typing import Any, AsyncIterator, Callable, Iterator, Optional

from .message_cache import get_message_cache
from .openai_utils import safe_zep_operation

from zep_cloud.client import AsyncZep, Zep
from zep_cloud.types import Message

logger = logging.getLogger(__name__)


class ZepStreamWrapper:
    """
    Wrapper around OpenAI streaming responses that collects content for Zep.

    This class wraps the OpenAI streaming response and collects the complete
    assistant response as it streams, then adds it to Zep when the stream completes.
    """

    def __init__(
        self,
        stream: Iterator[Any],
        thread_id: str,
        zep_client: Zep,
        extract_content_func: Callable[[Any], Optional[str]],
        skip_zep_on_error: bool = True,
    ):
        """
        Initialize the stream wrapper.

        Args:
            stream: The original OpenAI stream iterator
            thread_id: Thread ID for Zep thread
            zep_client: Zep client instance
            extract_content_func: Function to extract content from stream chunks
            skip_zep_on_error: Whether to skip/log errors or raise them
        """
        self.stream = stream
        self.thread_id = thread_id
        self.zep_client = zep_client
        self.extract_content_func = extract_content_func
        self.skip_zep_on_error = skip_zep_on_error
        self._content_buffer = io.StringIO()

    def __iter__(self) -> Iterator[Any]:
        """Make the wrapper iterable."""
        return self

    def __next__(self) -> Any:
        """Get the next chunk from the stream and collect content."""
        try:
            chunk = next(self.stream)

            # Extract and collect content from this chunk
            content = self._extract_chunk_content(chunk)
            if content and isinstance(content, str):
                self._content_buffer.write(content)

            return chunk

        except StopIteration:
            # Stream is complete, add collected content to Zep
            self._finalize_stream()
            raise

    def _extract_chunk_content(self, chunk: Any) -> Optional[str]:
        """
        Extract content from a streaming chunk.

        Args:
            chunk: A streaming response chunk

        Returns:
            Content string from the chunk or None
        """
        try:
            # Use the custom extraction function if provided
            if self.extract_content_func is not None:
                return self.extract_content_func(chunk)

            # Default extraction logic
            # For Chat Completions streaming
            if hasattr(chunk, "choices") and chunk.choices:
                choice = chunk.choices[0]
                if hasattr(choice, "delta") and hasattr(choice.delta, "content"):
                    return choice.delta.content

            # For Responses API streaming - this may need adjustment based on actual API
            elif hasattr(chunk, "delta") and hasattr(chunk.delta, "content"):
                return chunk.delta.content

            return None

        except Exception as e:
            logger.debug(f"Failed to extract content from chunk: {e}")
            return None

    def _finalize_stream(self) -> None:
        """
        Finalize the stream by adding collected content to Zep.
        """
        # Get the collected content from the buffer
        full_content = self._content_buffer.getvalue()

        if full_content.strip():
            # Check if this streamed assistant response is a duplicate
            cache = get_message_cache()
            from datetime import datetime
            response_created_at = datetime.utcnow()  # Streamed response being created now
            
            if not cache.is_message_seen(self.thread_id, "assistant", full_content, response_created_at):

                def add_to_zep():
                    zep_message = Message(role="assistant", role_type="assistant", content=full_content)
                    self.zep_client.thread.add_messages(self.thread_id, messages=[zep_message])
                    logger.debug(f"Added streamed assistant response to Zep thread {self.thread_id}")

                safe_zep_operation(
                    add_to_zep,
                    self.skip_zep_on_error,
                    "Add streamed assistant response to Zep thread",
                )
            else:
                logger.debug(f"Skipped duplicate streamed assistant response for thread {self.thread_id}")

    def __enter__(self):
        """Support for context manager protocol."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support for context manager protocol."""
        # Ensure content is added to Zep even if stream is not fully consumed
        self._finalize_stream()


class AsyncZepStreamWrapper:
    """
    Async wrapper around OpenAI streaming responses that collects content for Zep.

    This class wraps the OpenAI async streaming response and collects the complete
    assistant response as it streams, then adds it to Zep when the stream completes.
    """

    def __init__(
        self,
        stream: AsyncIterator[Any],
        thread_id: str,
        zep_client: AsyncZep,
        extract_content_func: Callable[[Any], Optional[str]],
        skip_zep_on_error: bool = True,
    ):
        """
        Initialize the async stream wrapper.

        Args:
            stream: The original OpenAI async stream iterator
            thread_id: Thread ID for Zep thread
            zep_client: Async Zep client instance
            extract_content_func: Function to extract content from stream chunks
            skip_zep_on_error: Whether to skip/log errors or raise them
        """
        self.stream = stream
        self.thread_id = thread_id
        self.zep_client = zep_client
        self.extract_content_func = extract_content_func
        self.skip_zep_on_error = skip_zep_on_error
        self._content_buffer = io.StringIO()

    def __aiter__(self) -> AsyncIterator[Any]:
        """Make the wrapper async iterable."""
        return self

    async def __anext__(self) -> Any:
        """Get the next chunk from the stream and collect content."""
        try:
            chunk = await self.stream.__anext__()

            # Extract and collect content from this chunk
            content = self._extract_chunk_content(chunk)
            if content and isinstance(content, str):
                self._content_buffer.write(content)

            return chunk

        except StopAsyncIteration:
            # Stream is complete, add collected content to Zep
            await self._finalize_stream()
            raise

    def _extract_chunk_content(self, chunk: Any) -> Optional[str]:
        """
        Extract content from a streaming chunk.

        Args:
            chunk: A streaming response chunk

        Returns:
            Content string from the chunk or None
        """
        try:
            # Use the custom extraction function if provided
            if self.extract_content_func is not None:
                return self.extract_content_func(chunk)

            # Default extraction logic
            # For Chat Completions streaming
            if hasattr(chunk, "choices") and chunk.choices:
                choice = chunk.choices[0]
                if hasattr(choice, "delta") and hasattr(choice.delta, "content"):
                    return choice.delta.content

            # For Responses API streaming - this may need adjustment based on actual API
            elif hasattr(chunk, "delta") and hasattr(chunk.delta, "content"):
                return chunk.delta.content

            return None

        except Exception as e:
            logger.debug(f"Failed to extract content from chunk: {e}")
            return None

    async def _finalize_stream(self) -> None:
        """
        Finalize the stream by adding collected content to Zep.
        """
        # Get the collected content from the buffer
        full_content = self._content_buffer.getvalue()

        if full_content.strip():
            # Check if this streamed assistant response is a duplicate
            cache = get_message_cache()
            from datetime import datetime
            response_created_at = datetime.utcnow()  # Streamed response being created now
            
            if not cache.is_message_seen(self.thread_id, "assistant", full_content, response_created_at):

                async def add_to_zep():
                    zep_message = Message(role="assistant", role_type="assistant", content=full_content)
                    await self.zep_client.thread.add_messages(self.thread_id, messages=[zep_message])
                    logger.debug(f"Added streamed assistant response to Zep thread {self.thread_id}")

                await self._asafe_zep_operation(
                    add_to_zep,
                    self.skip_zep_on_error,
                    "Add streamed assistant response to Zep thread",
                )
            else:
                logger.debug(f"Skipped duplicate streamed assistant response for thread {self.thread_id}")

    async def _asafe_zep_operation(
        self,
        operation_func,
        skip_on_error: bool = True,
        operation_name: str = "Zep operation",
    ) -> Any:
        """
        Async version of safe Zep operation.

        Args:
            operation_func: Async function to execute
            skip_on_error: Whether to skip/log errors or raise them
            operation_name: Name of the operation for logging

        Returns:
            Result of operation_func or None if error occurred
        """
        try:
            return await operation_func()
        except Exception as e:
            if skip_on_error:
                logger.warning(f"{operation_name} failed: {e}")
                return None
            else:
                from .openai_utils import ZepOpenAIError

                raise ZepOpenAIError(f"{operation_name} failed: {e}") from e

    async def __aenter__(self):
        """Support for async context manager protocol."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Support for async context manager protocol."""
        # Ensure content is added to Zep even if stream is not fully consumed
        await self._finalize_stream()
