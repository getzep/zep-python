"""
Main ZepOpenAI client implementation.
"""

import logging
from typing import Any, Dict, List, Optional, Union

try:
    from openai import OpenAI, Stream
    from openai.types.chat import ChatCompletion, ChatCompletionChunk
    from openai.types.responses import Response

    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

from .openai_base import BaseZepWrapper
from .openai_streaming import ZepStreamWrapper

from zep_cloud.client import Zep

logger = logging.getLogger(__name__)


if not HAS_OPENAI:
    raise ImportError("OpenAI is required for ZepOpenAI. Install it with: pip install openai")


class ChatCompletionsWrapper(BaseZepWrapper):
    """Wrapper for OpenAI Chat Completions API with Zep integration."""

    def __init__(self, openai_completions, zep_client: Zep):
        super().__init__(zep_client)
        self.openai_completions = openai_completions

    def create(
        self,
        model: str,
        messages: List[Dict[str, Any]],
        thread_id: Optional[str] = None,
        context_placeholder: str = "{context}",
        skip_zep_on_error: bool = True,
        **kwargs,
    ) -> Union[ChatCompletion, Stream[ChatCompletionChunk], ZepStreamWrapper]:
        """
        Create a chat completion with optional Zep integration.

        Args:
            model: The model to use for completion
            messages: List of messages in the conversation
            thread_id: Optional thread ID to enable Zep integration
            context_placeholder: Placeholder string for context injection
            skip_zep_on_error: Whether to continue if Zep operations fail
            **kwargs: Additional arguments to pass to OpenAI API

        Returns:
            ChatCompletion response from OpenAI
        """
        result = self._unified_create(
            model=model,
            messages=messages,
            thread_id=thread_id,
            context_placeholder=context_placeholder,
            skip_zep_on_error=skip_zep_on_error,
            **kwargs,
        )

        # Return the result directly from the unified create method
        # Type checking is only done when OpenAI is available and we're not using mocks
        if HAS_OPENAI and not self._is_test_environment(result):
            from zep_cloud.external_clients.openai_streaming import ZepStreamWrapper

            if isinstance(result, (ChatCompletion, Stream, ZepStreamWrapper)):
                return result
            else:
                # This should not happen for chat completions with real OpenAI
                raise TypeError(f"Unexpected return type from unified create: {type(result)}")
        else:
            # In test environments or when OpenAI is not available, return directly
            return result

    def _is_test_environment(self, result: Any) -> bool:
        """
        Check if we're in a test environment by examining the result type.

        Args:
            result: The result object to check

        Returns:
            True if we're likely in a test environment
        """
        # Check if it's a mock object (common test pattern)
        if hasattr(result, "_mock_name") or hasattr(result, "_spec_class"):
            return True

        # Check if the type name suggests it's from tests
        type_name = str(type(result))
        return "tests." in type_name or "mock" in type_name.lower()

    # Pass through other completions methods

    def _create_openai_direct(
        self, messages: List[Dict], openai_params: Dict
    ) -> Union[ChatCompletion, Stream[ChatCompletionChunk]]:
        """Make direct OpenAI API call for chat completions."""
        return self.openai_completions.create(messages=messages, **openai_params)

    def _extract_assistant_content(self, response: ChatCompletion) -> Optional[str]:
        """Extract assistant content from ChatCompletion response."""
        if response.choices and response.choices[0].message:
            return response.choices[0].message.content
        return None

    # Pass through other completions methods
    def __getattr__(self, name: str) -> Any:
        """Delegate unknown attributes to the underlying completions object."""
        return getattr(self.openai_completions, name)


class ResponsesWrapper(BaseZepWrapper):
    """Wrapper for OpenAI Responses API with Zep integration."""

    def __init__(self, openai_responses, zep_client: Zep):
        super().__init__(zep_client)
        self.openai_responses = openai_responses

    def create(
        self,
        model: str,
        messages: List[Dict[str, Any]],
        thread_id: Optional[str] = None,
        context_placeholder: str = "{context}",
        skip_zep_on_error: bool = True,
        **kwargs,
    ) -> Union[Response, Any]:  # Response API may support streaming in future
        """
        Create a response with optional Zep integration.

        Args:
            model: The model to use for the response
            messages: List of messages in the conversation
            thread_id: Optional thread ID to enable Zep integration
            context_placeholder: Placeholder string for context injection
            skip_zep_on_error: Whether to continue if Zep operations fail
            **kwargs: Additional arguments to pass to OpenAI API

        Returns:
            Response from OpenAI
        """
        return self._unified_create(
            model=model,
            messages=messages,
            thread_id=thread_id,
            context_placeholder=context_placeholder,
            skip_zep_on_error=skip_zep_on_error,
            **kwargs,
        )

    def _create_openai_direct(self, messages: List[Dict], openai_params: Dict) -> Response:
        """Make direct OpenAI API call for responses."""
        processed_input = self._convert_to_responses_format(messages)
        return self.openai_responses.create(input=processed_input, **openai_params)

    def _extract_assistant_content(self, response: Response) -> Optional[str]:
        """
        Extract assistant content from Response.

        Response structure:
        {
          "output": [
            {
              "content": [
                {
                  "text": "response text",
                  "type": "output_text"
                }
              ],
              "role": "assistant",
              "type": "message"
            }
          ]
        }
        """
        if not (hasattr(response, "output") and response.output):
            return None

        # Find first message-type output item from assistant
        for output_item in response.output:
            if (
                hasattr(output_item, "type")
                and output_item.type == "message"
                and hasattr(output_item, "role")
                and output_item.role == "assistant"
            ):
                # Extract text from content array
                if hasattr(output_item, "content") and output_item.content:
                    for content_item in output_item.content:
                        if (
                            hasattr(content_item, "type")
                            and content_item.type == "output_text"
                            and hasattr(content_item, "text")
                            and content_item.text
                        ):
                            return content_item.text

        return None

    def _convert_to_responses_format(self, messages: List[Dict]) -> Union[str, List[Dict]]:
        """
        Convert chat messages to Responses API format.

        The Responses API accepts either:
        - A string for simple single-turn conversations
        - An array of message objects for multi-turn conversations

        Args:
            messages: List of message dictionaries in Chat Completions format

        Returns:
            Either a string (for simple cases) or list of messages
        """
        if not messages:
            return []

        # For single user message without system context, return as string
        if len(messages) == 1 and messages[0].get("role") == "user" and isinstance(messages[0].get("content"), str):
            return messages[0]["content"]

        # For multi-turn conversations or complex content, return as message array
        # The Responses API uses the same message format as Chat Completions
        return messages

    # Pass through other responses methods
    def retrieve(self, response_id: str, **kwargs):
        """Retrieve a response by ID."""
        return self.openai_responses.retrieve(response_id, **kwargs)

    def delete(self, response_id: str):
        """Delete a response by ID."""
        return self.openai_responses.delete(response_id)

    def cancel(self, response_id: str):
        """Cancel a response by ID."""
        return self.openai_responses.cancel(response_id)

    def __getattr__(self, name: str) -> Any:
        """Delegate unknown attributes to the underlying responses object."""
        return getattr(self.openai_responses, name)


class ChatWrapper:
    """Wrapper for the entire chat namespace to maintain OpenAI client structure."""

    def __init__(self, openai_chat, zep_client: Zep):
        self.openai_chat = openai_chat
        self.zep_client = zep_client
        self.completions = ChatCompletionsWrapper(openai_chat.completions, zep_client)

    def __getattr__(self, name: str) -> Any:
        """Delegate unknown attributes to the underlying chat object."""
        return getattr(self.openai_chat, name)


class ZepOpenAI:
    """
    ZepOpenAI client that wraps the OpenAI client with Zep memory integration.

    This class provides a drop-in replacement for the OpenAI client. When thread_id
    is provided to API calls, Zep memory features are automatically enabled. Otherwise,
    it functions as a pure OpenAI passthrough.
    """

    def __init__(self, zep_client: Zep, openai_client: Optional[OpenAI] = None, **openai_kwargs):
        """
        Initialize ZepOpenAI client.

        Args:
            zep_client: Zep client instance for thread operations
            openai_client: Optional OpenAI client instance. If not provided,
                          will be created with openai_kwargs
            **openai_kwargs: Additional arguments to pass to OpenAI client constructor
        """
        self.zep_client = zep_client
        self.openai_client = openai_client or OpenAI(**openai_kwargs)

        # Wrap both chat completions and responses
        self.chat = ChatWrapper(self.openai_client.chat, self.zep_client)
        self.responses = ResponsesWrapper(self.openai_client.responses, self.zep_client)

        # Pass through all other OpenAI attributes
        self._setup_passthrough_attributes()

    def _setup_passthrough_attributes(self):
        """Set up passthrough attributes for all non-wrapped OpenAI client methods."""
        excluded_attrs = {"chat", "responses", "_setup_passthrough_attributes"}

        for attr in dir(self.openai_client):
            if not attr.startswith("_") and attr not in excluded_attrs:
                setattr(self, attr, getattr(self.openai_client, attr))

    def __getattr__(self, name: str) -> Any:
        """
        Fallback attribute access to delegate to the underlying OpenAI client.
        This ensures compatibility with future OpenAI client updates.
        """
        return getattr(self.openai_client, name)
