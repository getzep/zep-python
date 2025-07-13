"""
Base wrapper class with unified Zep integration logic.
"""

import logging
from typing import Any, Dict, List, Optional

from zep_cloud.client import AsyncZep, Zep
from zep_cloud.types import Message

from .openai_utils import (
    extract_conversation_messages,
    extract_zep_params,
    has_context_placeholder,
    inject_context,
    remove_zep_params,
    safe_zep_operation,
)

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

    def _unified_create(
        self, messages: List[Dict[str, Any]], session_id: Optional[str] = None, **kwargs
    ) -> Any:
        """
        Unified logic for both Chat Completions and Responses APIs.

        Args:
            messages: List of messages in the conversation
            session_id: Optional session ID to enable Zep integration
            **kwargs: Additional arguments including Zep and OpenAI parameters

        Returns:
            Response from the specific API implementation
        """
        # Extract Zep-specific parameters
        zep_params = extract_zep_params(kwargs)
        openai_params = remove_zep_params(kwargs)

        # Handle streaming
        stream = openai_params.get("stream", False)
        if session_id and stream:
            return self._create_stream_with_zep(
                messages, session_id, zep_params, openai_params
            )
        elif session_id:
            return self._create_with_zep(
                messages, session_id, zep_params, openai_params
            )
        else:
            return self._create_openai_direct(messages, openai_params)

    def _create_with_zep(
        self,
        messages: List[Dict[str, Any]],
        session_id: str,
        zep_params: Dict[str, Any],
        openai_params: Dict[str, Any],
    ) -> Any:
        """
        Create request with Zep integration.

        Args:
            messages: List of messages in the conversation
            session_id: Session ID for Zep memory
            zep_params: Zep-specific parameters
            openai_params: Parameters for OpenAI API

        Returns:
            Response from the specific API implementation
        """
        context_placeholder = zep_params.get("context_placeholder", "{context}")
        skip_zep_on_error = zep_params.get("skip_zep_on_error", True)

        # Check if context injection is needed
        needs_context = has_context_placeholder(messages, context_placeholder)

        if needs_context:
            # Add new messages to Zep and get context in one optimized call
            context = self._get_context_with_optimization(
                session_id, messages, skip_zep_on_error
            )

            if context is not None:
                messages = inject_context(messages, context, context_placeholder)

        # Make OpenAI call (implemented by subclass)
        response = self._create_openai_direct(messages, openai_params)

        # Add assistant response to Zep
        if needs_context:
            self._add_assistant_response_to_zep(session_id, response, skip_zep_on_error)

        return response

    def _get_context_with_optimization(
        self,
        session_id: str,
        messages: List[Dict[str, Any]],
        skip_zep_on_error: bool = True,
    ) -> Optional[str]:
        """
        Get context from Zep with optimization using return_context=True.

        Args:
            session_id: Session ID for Zep memory
            messages: List of messages in the conversation
            skip_zep_on_error: Whether to skip/log errors or raise them

        Returns:
            Context string from Zep or None if error occurred
        """
        conversation_messages = extract_conversation_messages(messages, user_only=True)

        if conversation_messages:
            # Optimized: Add messages AND get context in one call
            def add_with_context():
                memory_response = self.zep_client.memory.add(
                    session_id=session_id,
                    messages=conversation_messages,
                    return_context=True,
                )
                return memory_response.context

            return safe_zep_operation(
                add_with_context,
                skip_zep_on_error,
                "Add messages and get context from Zep",
            )
        else:
            # Fallback: Only get context if no new messages
            def get_context():
                memory = self.zep_client.memory.get(session_id)
                return memory.context

            return safe_zep_operation(
                get_context, skip_zep_on_error, "Get context from Zep"
            )

    def _add_assistant_response_to_zep(
        self, session_id: str, response: Any, skip_zep_on_error: bool = True
    ) -> None:
        """
        Add assistant response to Zep memory.

        Args:
            session_id: Session ID for Zep memory
            response: OpenAI API response
            skip_zep_on_error: Whether to skip/log errors or raise them
        """

        def add_assistant_response():
            assistant_content = self._extract_assistant_content(response)
            if assistant_content:
                zep_message = Message(
                    role="assistant", role_type="assistant", content=assistant_content
                )
                self.zep_client.memory.add(session_id, messages=[zep_message])
                logger.debug(f"Added assistant response to Zep session {session_id}")

        safe_zep_operation(
            add_assistant_response, skip_zep_on_error, "Add assistant response to Zep"
        )

    def _create_stream_with_zep(
        self,
        messages: List[Dict[str, Any]],
        session_id: str,
        zep_params: Dict[str, Any],
        openai_params: Dict[str, Any],
    ) -> Any:
        """
        Create streaming request with Zep integration.

        Args:
            messages: List of messages in the conversation
            session_id: Session ID for Zep memory
            zep_params: Zep-specific parameters
            openai_params: Parameters for OpenAI API

        Returns:
            ZepStreamWrapper around the OpenAI stream
        """
        context_placeholder = zep_params.get("context_placeholder", "{context}")
        skip_zep_on_error = zep_params.get("skip_zep_on_error", True)

        # Pre-process for context injection
        processed_messages = self._preprocess_for_zep(
            messages, session_id, context_placeholder, skip_zep_on_error
        )

        # Create streaming response
        stream = self._create_openai_direct(processed_messages, openai_params)

        # Wrap stream to collect response for Zep
        from .openai_streaming import ZepStreamWrapper

        return ZepStreamWrapper(
            stream=stream,
            session_id=session_id,
            zep_client=self.zep_client,
            extract_content_func=self._extract_assistant_content,
            skip_zep_on_error=skip_zep_on_error,
        )

    def _preprocess_for_zep(
        self,
        messages: List[Dict[str, Any]],
        session_id: str,
        context_placeholder: str = "{context}",
        skip_zep_on_error: bool = True,
    ) -> List[Dict[str, Any]]:
        """
        Pre-process messages for Zep integration (for streaming).

        Args:
            messages: List of messages in the conversation
            session_id: Session ID for Zep memory
            context_placeholder: Placeholder string for context injection
            skip_zep_on_error: Whether to skip/log errors or raise them

        Returns:
            Processed messages with context injected
        """
        # Check if context injection is needed
        needs_context = has_context_placeholder(messages, context_placeholder)

        if needs_context:
            # Add new messages to Zep and get context in one optimized call
            context = self._get_context_with_optimization(
                session_id, messages, skip_zep_on_error
            )

            if context is not None:
                messages = inject_context(messages, context, context_placeholder)

        return messages

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
        raise NotImplementedError(
            "Subclasses must implement _extract_assistant_content"
        )


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

    async def _aunified_create(
        self, messages: List[Dict[str, Any]], session_id: Optional[str] = None, **kwargs
    ) -> Any:
        """
        Async version of unified create logic.

        Args:
            messages: List of messages in the conversation
            session_id: Optional session ID to enable Zep integration
            **kwargs: Additional arguments including Zep and OpenAI parameters

        Returns:
            Response from the specific API implementation
        """
        # Extract Zep-specific parameters
        zep_params = extract_zep_params(kwargs)
        openai_params = remove_zep_params(kwargs)

        # Handle streaming
        stream = openai_params.get("stream", False)
        if session_id and stream:
            return await self._acreate_stream_with_zep(
                messages, session_id, zep_params, openai_params
            )
        elif session_id:
            return await self._acreate_with_zep(
                messages, session_id, zep_params, openai_params
            )
        else:
            return await self._acreate_openai_direct(messages, openai_params)

    async def _acreate_with_zep(
        self,
        messages: List[Dict[str, Any]],
        session_id: str,
        zep_params: Dict[str, Any],
        openai_params: Dict[str, Any],
    ) -> Any:
        """
        Async version of create with Zep integration.

        Args:
            messages: List of messages in the conversation
            session_id: Session ID for Zep memory
            zep_params: Zep-specific parameters
            openai_params: Parameters for OpenAI API

        Returns:
            Response from the specific API implementation
        """
        context_placeholder = zep_params.get("context_placeholder", "{context}")
        skip_zep_on_error = zep_params.get("skip_zep_on_error", True)

        # Check if context injection is needed
        needs_context = has_context_placeholder(messages, context_placeholder)

        if needs_context:
            # Add new messages to Zep and get context in one optimized call
            context = await self._aget_context_with_optimization(
                session_id, messages, skip_zep_on_error
            )

            if context is not None:
                messages = inject_context(messages, context, context_placeholder)

        # Make OpenAI call (implemented by subclass)
        response = await self._acreate_openai_direct(messages, openai_params)

        # Add assistant response to Zep
        if needs_context:
            await self._aadd_assistant_response_to_zep(
                session_id, response, skip_zep_on_error
            )

        return response

    async def _aget_context_with_optimization(
        self,
        session_id: str,
        messages: List[Dict[str, Any]],
        skip_zep_on_error: bool = True,
    ) -> Optional[str]:
        """
        Async version of get context with optimization.

        Args:
            session_id: Session ID for Zep memory
            messages: List of messages in the conversation
            skip_zep_on_error: Whether to skip/log errors or raise them

        Returns:
            Context string from Zep or None if error occurred
        """
        conversation_messages = extract_conversation_messages(messages, user_only=True)

        if conversation_messages:
            # Optimized: Add messages AND get context in one call
            async def add_with_context():
                memory_response = await self.zep_client.memory.add(
                    session_id=session_id,
                    messages=conversation_messages,
                    return_context=True,
                )
                return memory_response.context

            return await self._asafe_zep_operation(
                add_with_context,
                skip_zep_on_error,
                "Add messages and get context from Zep",
            )
        else:
            # Fallback: Only get context if no new messages
            async def get_context():
                memory = await self.zep_client.memory.get(session_id)
                return memory.context

            return await self._asafe_zep_operation(
                get_context, skip_zep_on_error, "Get context from Zep"
            )

    async def _aadd_assistant_response_to_zep(
        self, session_id: str, response: Any, skip_zep_on_error: bool = True
    ) -> None:
        """
        Async version of add assistant response to Zep.

        Args:
            session_id: Session ID for Zep memory
            response: OpenAI API response
            skip_zep_on_error: Whether to skip/log errors or raise them
        """

        async def add_assistant_response():
            assistant_content = self._extract_assistant_content(response)
            if assistant_content:
                zep_message = Message(
                    role="assistant", role_type="assistant", content=assistant_content
                )
                await self.zep_client.memory.add(session_id, messages=[zep_message])
                logger.debug(f"Added assistant response to Zep session {session_id}")

        await self._asafe_zep_operation(
            add_assistant_response, skip_zep_on_error, "Add assistant response to Zep"
        )

    async def _acreate_stream_with_zep(
        self,
        messages: List[Dict[str, Any]],
        session_id: str,
        zep_params: Dict[str, Any],
        openai_params: Dict[str, Any],
    ) -> Any:
        """
        Async version of create stream with Zep integration.

        Args:
            messages: List of messages in the conversation
            session_id: Session ID for Zep memory
            zep_params: Zep-specific parameters
            openai_params: Parameters for OpenAI API

        Returns:
            AsyncZepStreamWrapper around the OpenAI stream
        """
        context_placeholder = zep_params.get("context_placeholder", "{context}")
        skip_zep_on_error = zep_params.get("skip_zep_on_error", True)

        # Pre-process for context injection
        processed_messages = await self._apreprocess_for_zep(
            messages, session_id, context_placeholder, skip_zep_on_error
        )

        # Create streaming response
        stream = await self._acreate_openai_direct(processed_messages, openai_params)

        # Wrap stream to collect response for Zep
        from .openai_streaming import AsyncZepStreamWrapper

        return AsyncZepStreamWrapper(
            stream=stream,
            session_id=session_id,
            zep_client=self.zep_client,
            extract_content_func=self._extract_assistant_content,
            skip_zep_on_error=skip_zep_on_error,
        )

    async def _apreprocess_for_zep(
        self,
        messages: List[Dict[str, Any]],
        session_id: str,
        context_placeholder: str = "{context}",
        skip_zep_on_error: bool = True,
    ) -> List[Dict[str, Any]]:
        """
        Async version of preprocess for Zep integration.

        Args:
            messages: List of messages in the conversation
            session_id: Session ID for Zep memory
            context_placeholder: Placeholder string for context injection
            skip_zep_on_error: Whether to skip/log errors or raise them

        Returns:
            Processed messages with context injected
        """
        # Check if context injection is needed
        needs_context = has_context_placeholder(messages, context_placeholder)

        if needs_context:
            # Add new messages to Zep and get context in one optimized call
            context = await self._aget_context_with_optimization(
                session_id, messages, skip_zep_on_error
            )

            if context is not None:
                messages = inject_context(messages, context, context_placeholder)

        return messages

    async def _acreate_openai_direct(
        self, messages: List[Dict], openai_params: Dict
    ) -> Any:
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
        raise NotImplementedError(
            "Subclasses must implement _extract_assistant_content"
        )

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
