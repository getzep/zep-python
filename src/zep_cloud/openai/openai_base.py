"""
Base wrapper class with unified Zep integration logic.
"""

import logging
from typing import Any, Dict, List, Optional

from .openai_utils import (
    extract_conversation_messages,
    extract_zep_params,
    has_context_placeholder,
    inject_context,
    remove_zep_params,
    safe_zep_operation,
)

from zep_cloud.client import AsyncZep, Zep
from zep_cloud.types import Message

logger = logging.getLogger(__name__)


class BaseZepWrapper:
    """
    Base class for OpenAI API wrappers with unified Zep integration logic.

    This class provides the core Zep integration functionality that is shared
    across different OpenAI API endpoints (Chat Completions, Responses, etc.).
    """

    def __init__(self, zep_client: Zep):
        """
        Initialize the base wrapper.

        Args:
            zep_client: Zep client instance for memory operations
        """
        self.zep_client = zep_client

    def _unified_create(self, messages: List[Dict[str, Any]], thread_id: Optional[str] = None, **kwargs) -> Any:
        """
        Unified logic for both Chat Completions and Responses APIs.

        Args:
            messages: List of messages in the conversation
            thread_id: Optional thread ID to enable Zep integration
            **kwargs: Additional arguments including Zep and OpenAI parameters

        Returns:
            Response from the specific API implementation
        """
        # Extract Zep-specific parameters
        zep_params = extract_zep_params(kwargs)
        openai_params = remove_zep_params(kwargs)

        # Handle streaming
        stream = openai_params.get("stream", False)
        if thread_id and stream:
            return self._create_stream_with_zep(messages, thread_id, zep_params, openai_params)
        elif thread_id:
            return self._create_with_zep(messages, thread_id, zep_params, openai_params)
        else:
            return self._create_openai_direct(messages, openai_params)

    def _create_with_zep(
        self,
        messages: List[Dict[str, Any]],
        thread_id: str,
        zep_params: Dict[str, Any],
        openai_params: Dict[str, Any],
    ) -> Any:
        """
        Create request with Zep integration.

        Args:
            messages: List of messages in the conversation
            thread_id: Thread ID for Zep thread
            zep_params: Zep-specific parameters
            openai_params: Parameters for OpenAI API

        Returns:
            Response from the specific API implementation
        """
        context_placeholder = zep_params.get("context_placeholder", "{context}")
        skip_zep_on_error = zep_params.get("skip_zep_on_error", True)

        # Ensure thread exists before operations
        self._ensure_thread_exists(thread_id, skip_zep_on_error)

        # Check if context injection is needed
        needs_context = has_context_placeholder(messages, context_placeholder)

        if needs_context:
            # Add new messages to Zep and get context in one optimized call
            context = self._get_context_with_optimization(thread_id, messages, skip_zep_on_error)

            if context is not None:
                messages = inject_context(messages, context, context_placeholder)

        # Make OpenAI call (implemented by subclass)
        response = self._create_openai_direct(messages, openai_params)

        # Add assistant response to Zep
        if needs_context:
            self._add_assistant_response_to_zep(thread_id, response, skip_zep_on_error)

        return response

    def _get_context_with_optimization(
        self,
        thread_id: str,
        messages: List[Dict[str, Any]],
        skip_zep_on_error: bool = True,
    ) -> Optional[str]:
        """
        Get context from Zep with optimization using return_context=True.

        Args:
            thread_id: Thread ID for Zep thread
            messages: List of messages in the conversation
            skip_zep_on_error: Whether to skip/log errors or raise them

        Returns:
            Context string from Zep or None if error occurred
        """
        conversation_messages = extract_conversation_messages(messages, user_only=True)

        if conversation_messages:
            filtered_messages = []

            for msg in conversation_messages:
                filtered_messages.append(msg)

            if filtered_messages:
                # Optimized: Add new messages AND get context in one call
                def add_with_context():
                    response = self.zep_client.thread.add_messages(
                        thread_id=thread_id,
                        messages=filtered_messages,
                        return_context=True,
                    )
                    return response.context

                return safe_zep_operation(
                    add_with_context,
                    skip_zep_on_error,
                    "Add messages and get context from Zep thread",
                )
            else:
                # All messages were duplicates, just get context
                def get_context():
                    response = self.zep_client.thread.get_user_context(thread_id)
                    return response.context

                return safe_zep_operation(get_context, skip_zep_on_error, "Get context from Zep thread")
        else:
            # Fallback: Only get context if no new messages
            def get_context():
                response = self.zep_client.thread.get_user_context(thread_id)
                return response.context

            return safe_zep_operation(get_context, skip_zep_on_error, "Get context from Zep thread")

    def _add_assistant_response_to_zep(self, thread_id: str, response: Any, skip_zep_on_error: bool = True) -> None:
        """
        Add assistant response to Zep thread.

        Args:
            thread_id: Thread ID for Zep thread
            response: OpenAI API response
            skip_zep_on_error: Whether to skip/log errors or raise them
        """

        def add_assistant_response():
            assistant_content = self._extract_assistant_content(response)
            if assistant_content:
                zep_message = Message(role="assistant", name="assistant", content=assistant_content)
                self.zep_client.thread.add_messages(thread_id, messages=[zep_message])
                logger.debug(f"Added assistant response to Zep thread {thread_id}")

        safe_zep_operation(add_assistant_response, skip_zep_on_error, "Add assistant response to Zep thread")

    def _create_stream_with_zep(
        self,
        messages: List[Dict[str, Any]],
        thread_id: str,
        zep_params: Dict[str, Any],
        openai_params: Dict[str, Any],
    ) -> Any:
        """
        Create streaming request with Zep integration.

        Args:
            messages: List of messages in the conversation
            thread_id: Thread ID for Zep thread
            zep_params: Zep-specific parameters
            openai_params: Parameters for OpenAI API

        Returns:
            ZepStreamWrapper around the OpenAI stream
        """
        context_placeholder = zep_params.get("context_placeholder", "{context}")
        skip_zep_on_error = zep_params.get("skip_zep_on_error", True)

        # Ensure thread exists before operations
        self._ensure_thread_exists(thread_id, skip_zep_on_error)

        # Pre-process for context injection
        processed_messages = self._preprocess_for_zep(messages, thread_id, context_placeholder, skip_zep_on_error)

        # Create streaming response
        stream = self._create_openai_direct(processed_messages, openai_params)

        # Wrap stream to collect response for Zep
        from .openai_streaming import ZepStreamWrapper

        return ZepStreamWrapper(
            stream=stream,
            thread_id=thread_id,
            zep_client=self.zep_client,
            extract_content_func=self._extract_assistant_content,
            skip_zep_on_error=skip_zep_on_error,
        )

    def _preprocess_for_zep(
        self,
        messages: List[Dict[str, Any]],
        thread_id: str,
        context_placeholder: str = "{context}",
        skip_zep_on_error: bool = True,
    ) -> List[Dict[str, Any]]:
        """
        Pre-process messages for Zep integration (for streaming).

        Args:
            messages: List of messages in the conversation
            thread_id: Thread ID for Zep thread
            context_placeholder: Placeholder string for context injection
            skip_zep_on_error: Whether to skip/log errors or raise them

        Returns:
            Processed messages with context injected
        """
        # Ensure thread exists before operations
        self._ensure_thread_exists(thread_id, skip_zep_on_error)

        # Check if context injection is needed
        needs_context = has_context_placeholder(messages, context_placeholder)

        if needs_context:
            # Add new messages to Zep and get context in one optimized call
            context = self._get_context_with_optimization(thread_id, messages, skip_zep_on_error)

            if context is not None:
                messages = inject_context(messages, context, context_placeholder)

        return messages

    def _ensure_thread_exists(self, thread_id: str, skip_on_error: bool = True) -> None:
        """
        Ensure thread exists, create if it doesn't.

        Args:
            thread_id: Thread ID to check/create
            skip_on_error: Whether to skip/log errors or raise them
        """

        def ensure_thread():
            try:
                # Try a lightweight operation to check if thread exists
                self.zep_client.thread.get_user_context(thread_id)
            except Exception as e:
                # Check if it's a "not found" type error
                error_str = str(e).lower()
                if "not found" in error_str or "404" in error_str:
                   raise Exception("Thread not found, please ensure you have created the thread before using it.")
                else:
                    # Some other error, re-raise
                    raise

        safe_zep_operation(ensure_thread, skip_on_error, f"Ensure thread {thread_id} exists")

    def _create_openai_direct(self, messages: List[Dict], openai_params: Dict) -> Any:
        """
        Make direct OpenAI API call without Zep integration.
        Must be implemented by subclasses.

        Args:
            messages: List of messages for the API call
            openai_params: Parameters for OpenAI API

        Returns:
            Response from OpenAI API
        """
        raise NotImplementedError("Subclasses must implement _create_openai_direct")

    def _extract_assistant_content(self, response: Any) -> Optional[str]:
        """
        Extract assistant content from API response.
        Must be implemented by subclasses.

        Args:
            response: OpenAI API response

        Returns:
            Assistant content string or None
        """
        raise NotImplementedError("Subclasses must implement _extract_assistant_content")


class AsyncBaseZepWrapper:
    """
    Async version of BaseZepWrapper for async Zep client operations.
    """

    def __init__(self, zep_client: AsyncZep):
        """
        Initialize the async base wrapper.

        Args:
            zep_client: Async Zep client instance for memory operations
        """
        self.zep_client = zep_client

    async def _aunified_create(self, messages: List[Dict[str, Any]], thread_id: Optional[str] = None, **kwargs) -> Any:
        """
        Async version of unified create logic.

        Args:
            messages: List of messages in the conversation
            thread_id: Optional thread ID to enable Zep integration
            **kwargs: Additional arguments including Zep and OpenAI parameters

        Returns:
            Response from the specific API implementation
        """
        # Extract Zep-specific parameters
        zep_params = extract_zep_params(kwargs)
        openai_params = remove_zep_params(kwargs)

        # Handle streaming
        stream = openai_params.get("stream", False)
        if thread_id and stream:
            return await self._acreate_stream_with_zep(messages, thread_id, zep_params, openai_params)
        elif thread_id:
            return await self._acreate_with_zep(messages, thread_id, zep_params, openai_params)
        else:
            return await self._acreate_openai_direct(messages, openai_params)

    async def _acreate_with_zep(
        self,
        messages: List[Dict[str, Any]],
        thread_id: str,
        zep_params: Dict[str, Any],
        openai_params: Dict[str, Any],
    ) -> Any:
        """
        Async version of create with Zep integration.

        Args:
            messages: List of messages in the conversation
            thread_id: Thread ID for Zep thread
            zep_params: Zep-specific parameters
            openai_params: Parameters for OpenAI API

        Returns:
            Response from the specific API implementation
        """
        context_placeholder = zep_params.get("context_placeholder", "{context}")
        skip_zep_on_error = zep_params.get("skip_zep_on_error", True)

        # Ensure thread exists before operations
        await self._aensure_thread_exists(thread_id, skip_zep_on_error)

        # Check if context injection is needed
        needs_context = has_context_placeholder(messages, context_placeholder)

        if needs_context:
            # Add new messages to Zep and get context in one optimized call
            context = await self._aget_context_with_optimization(thread_id, messages, skip_zep_on_error)

            if context is not None:
                messages = inject_context(messages, context, context_placeholder)

        # Make OpenAI call (implemented by subclass)
        response = await self._acreate_openai_direct(messages, openai_params)

        # Add assistant response to Zep
        if needs_context:
            await self._aadd_assistant_response_to_zep(thread_id, response, skip_zep_on_error)

        return response

    async def _aget_context_with_optimization(
        self,
        thread_id: str,
        messages: List[Dict[str, Any]],
        skip_zep_on_error: bool = True,
    ) -> Optional[str]:
        """
        Async version of get context with optimization.

        Args:
            thread_id: Thread ID for Zep thread
            messages: List of messages in the conversation
            skip_zep_on_error: Whether to skip/log errors or raise them

        Returns:
            Context string from Zep or None if error occurred
        """
        conversation_messages = extract_conversation_messages(messages, user_only=True)

        if conversation_messages:
            filtered_messages = []

            for msg in conversation_messages:
                filtered_messages.append(msg)

            if filtered_messages:
                # Optimized: Add new messages AND get context in one call
                async def add_with_context():
                    response = await self.zep_client.thread.add_messages(
                        thread_id=thread_id,
                        messages=filtered_messages,
                        return_context=True,
                    )
                    return response.context

                return await self._asafe_zep_operation(
                    add_with_context,
                    skip_zep_on_error,
                    "Add messages and get context from Zep thread",
                )
            else:
                # All messages were duplicates, just get context
                async def get_context():
                    response = await self.zep_client.thread.get_user_context(thread_id)
                    return response.context

                return await self._asafe_zep_operation(get_context, skip_zep_on_error, "Get context from Zep thread")
        else:
            # Fallback: Only get context if no new messages
            async def get_context():
                response = await self.zep_client.thread.get_user_context(thread_id)
                return response.context

            return await self._asafe_zep_operation(get_context, skip_zep_on_error, "Get context from Zep thread")

    async def _aadd_assistant_response_to_zep(
        self, thread_id: str, response: Any, skip_zep_on_error: bool = True
    ) -> None:
        """
        Async version of add assistant response to Zep.

        Args:
            thread_id: Thread ID for Zep thread
            response: OpenAI API response
            skip_zep_on_error: Whether to skip/log errors or raise them
        """

        async def add_assistant_response():
            assistant_content = self._extract_assistant_content(response)
            if assistant_content:
                zep_message = Message(role="assistant", name="assistant", content=assistant_content)
                await self.zep_client.thread.add_messages(thread_id, messages=[zep_message])
                logger.debug(f"Added assistant response to Zep thread {thread_id}")

        await self._asafe_zep_operation(
            add_assistant_response, skip_zep_on_error, "Add assistant response to Zep thread"
        )

    async def _acreate_stream_with_zep(
        self,
        messages: List[Dict[str, Any]],
        thread_id: str,
        zep_params: Dict[str, Any],
        openai_params: Dict[str, Any],
    ) -> Any:
        """
        Async version of create stream with Zep integration.

        Args:
            messages: List of messages in the conversation
            thread_id: Thread ID for Zep thread
            zep_params: Zep-specific parameters
            openai_params: Parameters for OpenAI API

        Returns:
            AsyncZepStreamWrapper around the OpenAI stream
        """
        context_placeholder = zep_params.get("context_placeholder", "{context}")
        skip_zep_on_error = zep_params.get("skip_zep_on_error", True)

        # Pre-process for context injection
        processed_messages = await self._apreprocess_for_zep(
            messages, thread_id, context_placeholder, skip_zep_on_error
        )

        # Create streaming response
        stream = await self._acreate_openai_direct(processed_messages, openai_params)

        # Wrap stream to collect response for Zep
        from .openai_streaming import AsyncZepStreamWrapper

        return AsyncZepStreamWrapper(
            stream=stream,
            thread_id=thread_id,
            zep_client=self.zep_client,
            extract_content_func=self._extract_assistant_content,
            skip_zep_on_error=skip_zep_on_error,
        )

    async def _apreprocess_for_zep(
        self,
        messages: List[Dict[str, Any]],
        thread_id: str,
        context_placeholder: str = "{context}",
        skip_zep_on_error: bool = True,
    ) -> List[Dict[str, Any]]:
        """
        Async version of preprocess for Zep integration.

        Args:
            messages: List of messages in the conversation
            thread_id: Thread ID for Zep thread
            context_placeholder: Placeholder string for context injection
            skip_zep_on_error: Whether to skip/log errors or raise them

        Returns:
            Processed messages with context injected
        """
        # Ensure thread exists before operations
        await self._aensure_thread_exists(thread_id, skip_zep_on_error)

        # Check if context injection is needed
        needs_context = has_context_placeholder(messages, context_placeholder)

        if needs_context:
            # Add new messages to Zep and get context in one optimized call
            context = await self._aget_context_with_optimization(thread_id, messages, skip_zep_on_error)

            if context is not None:
                messages = inject_context(messages, context, context_placeholder)

        return messages

    async def _aensure_thread_exists(self, thread_id: str, skip_on_error: bool = True) -> None:
        """
        Async version of ensure thread exists, create if it doesn't.

        Args:
            thread_id: Thread ID to check/create
            skip_on_error: Whether to skip/log errors or raise them
        """

        async def ensure_thread():
            try:
                # Try a lightweight operation to check if thread exists
                await self.zep_client.thread.get_user_context(thread_id)
            except Exception as e:
                # Check if it's a "not found" type error
                error_str = str(e).lower()
                if "not found" in error_str or "404" in error_str:
                    raise Exception("Thread not found, please ensure you have created the thread before using it.")
                else:
                    # Some other error, re-raise
                    raise

        await self._asafe_zep_operation(ensure_thread, skip_on_error, f"Ensure thread {thread_id} exists")

    async def _acreate_openai_direct(self, messages: List[Dict], openai_params: Dict) -> Any:
        """
        Async version of create OpenAI direct.
        Must be implemented by subclasses.

        Args:
            messages: List of messages for the API call
            openai_params: Parameters for OpenAI API

        Returns:
            Response from OpenAI API
        """
        raise NotImplementedError("Subclasses must implement _acreate_openai_direct")

    def _extract_assistant_content(self, response: Any) -> Optional[str]:
        """
        Extract assistant content from API response.
        Must be implemented by subclasses.

        Args:
            response: OpenAI API response

        Returns:
            Assistant content string or None
        """
        raise NotImplementedError("Subclasses must implement _extract_assistant_content")

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
