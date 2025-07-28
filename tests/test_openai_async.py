"""
Tests for async ZepOpenAI client wrapper.
"""

from unittest.mock import MagicMock, patch

import pytest

# Mock openai imports to avoid import errors in testing
with patch.dict(
    "sys.modules", {"openai": MagicMock(), "openai.types.chat": MagicMock(), "openai.types.responses": MagicMock()}
):
    from zep_cloud.openai.openai_async import (
        AsyncChatCompletionsWrapper,
        AsyncChatWrapper,
        AsyncResponsesWrapper,
        AsyncZepOpenAI,
    )

from .openai_fixtures import (
    MockOpenAIResponse,
    MockOpenAIResponsesAPI,
    MockZepMemory,
    mock_async_openai_client,
)


class TestAsyncZepOpenAIInitialization:
    """Test AsyncZepOpenAI client initialization."""

    def test_init_with_zep_client_only(self, mock_async_zep_client):
        """Test initialization with just async Zep client."""
        with patch("zep_cloud.openai.openai_async.AsyncOpenAI") as mock_async_openai:
            mock_async_openai_instance = mock_async_openai_client()
            mock_async_openai.return_value = mock_async_openai_instance

            client = AsyncZepOpenAI(zep_client=mock_async_zep_client)

            assert client.zep_client == mock_async_zep_client
            assert client.openai_client == mock_async_openai_instance
            assert hasattr(client, "chat")
            assert hasattr(client, "responses")
            mock_async_openai.assert_called_once_with()

    def test_init_with_both_clients(self, mock_async_zep_client, mock_async_openai_client):
        """Test initialization with both async clients."""
        client = AsyncZepOpenAI(zep_client=mock_async_zep_client, openai_client=mock_async_openai_client)

        assert client.zep_client == mock_async_zep_client
        assert client.openai_client == mock_async_openai_client

    def test_init_with_openai_kwargs(self, mock_async_zep_client):
        """Test initialization with OpenAI kwargs."""
        with patch("zep_cloud.openai.openai_async.AsyncOpenAI") as mock_async_openai:
            mock_async_openai_instance = mock_async_openai_client()
            mock_async_openai.return_value = mock_async_openai_instance

            client = AsyncZepOpenAI(zep_client=mock_async_zep_client, api_key="test-key", timeout=30.0)

            mock_async_openai.assert_called_once_with(api_key="test-key", timeout=30.0)

    def test_passthrough_attributes(self, mock_async_zep_client, mock_async_openai_client):
        """Test that non-wrapped attributes are passed through."""
        # Add some attributes to mock client
        mock_async_openai_client.models = MagicMock()
        mock_async_openai_client.embeddings = MagicMock()

        client = AsyncZepOpenAI(zep_client=mock_async_zep_client, openai_client=mock_async_openai_client)

        # These should be passed through
        assert hasattr(client, "models")
        assert hasattr(client, "embeddings")

        # These should be wrapped
        assert isinstance(client.chat, AsyncChatWrapper)
        assert isinstance(client.responses, AsyncResponsesWrapper)


class TestAsyncChatCompletionsWrapper:
    """Test AsyncChatCompletionsWrapper functionality."""

    @pytest.mark.asyncio
    async def test_create_without_session_id(
        self, mock_async_zep_client, mock_async_openai_client, sample_messages_no_context
    ):
        """Test async chat completion without session_id."""
        wrapper = AsyncChatCompletionsWrapper(mock_async_openai_client.chat.completions, mock_async_zep_client)

        response = await wrapper.create(model="gpt-4.1-mini", messages=sample_messages_no_context, temperature=0.7)

        # Should call OpenAI directly without Zep integration
        assert response == await mock_async_openai_client.chat.completions.create(
            messages=sample_messages_no_context, model="gpt-4.1-mini", temperature=0.7
        )

        # Should not call Zep
        mock_async_zep_client.memory.get.assert_not_called()
        mock_async_zep_client.memory.add.assert_not_called()

    @pytest.mark.asyncio
    async def test_create_with_session_id_no_context_placeholder(
        self, mock_async_zep_client, mock_async_openai_client, sample_messages_no_context
    ):
        """Test async chat completion with session_id but no context placeholder."""
        wrapper = AsyncChatCompletionsWrapper(mock_async_openai_client.chat.completions, mock_async_zep_client)

        response = await wrapper.create(
            model="gpt-4.1-mini", messages=sample_messages_no_context, session_id="test_session"
        )

        # Should call OpenAI with original messages
        assert response is not None

        # Should not call Zep memory operations since no context placeholder
        mock_async_zep_client.memory.get.assert_not_called()
        mock_async_zep_client.memory.add.assert_not_called()

    @pytest.mark.asyncio
    async def test_create_with_session_id_and_context_placeholder(
        self, mock_async_zep_client, mock_async_openai_client, sample_messages
    ):
        """Test async chat completion with session_id and context placeholder."""
        wrapper = AsyncChatCompletionsWrapper(mock_async_openai_client.chat.completions, mock_async_zep_client)

        # Mock Zep responses
        async def mock_add(*args, **kwargs):
            mock_response = MagicMock()
            mock_response.context = "Alice loves pizza"
            return mock_response

        mock_async_zep_client.memory.add = mock_add

        async def mock_create(*args, **kwargs):
            # Verify context was injected
            messages = kwargs.get("messages", args[0] if args else [])
            if messages and "Alice loves pizza" in str(messages[0].get("content", "")):
                return MockOpenAIResponse("Hi Alice!")
            return MockOpenAIResponse("Default response")

        mock_async_openai_client.chat.completions.create = mock_create

        response = await wrapper.create(model="gpt-4.1-mini", messages=sample_messages, session_id="test_session")

        assert response is not None

    @pytest.mark.asyncio
    async def test_create_with_custom_context_placeholder(self, mock_async_zep_client, mock_async_openai_client):
        """Test async chat completion with custom context placeholder."""
        messages = [
            {"role": "system", "content": "Memory: {{memory}} - Use this."},
            {"role": "user", "content": "Hello"},
        ]

        wrapper = AsyncChatCompletionsWrapper(mock_async_openai_client.chat.completions, mock_async_zep_client)

        async def mock_add(*args, **kwargs):
            mock_response = MagicMock()
            mock_response.context = "Custom context"
            return mock_response

        mock_async_zep_client.memory.add = mock_add

        async def mock_create(*args, **kwargs):
            # Verify custom context was injected
            messages = kwargs.get("messages", args[0] if args else [])
            if messages and "Memory: Custom context - Use this." in str(messages[0].get("content", "")):
                return MockOpenAIResponse("Success")
            return MockOpenAIResponse("Failed")

        mock_async_openai_client.chat.completions.create = mock_create

        response = await wrapper.create(
            model="gpt-4.1-mini", messages=messages, session_id="test_session", context_placeholder="{{memory}}"
        )

        assert response is not None

    def test_extract_assistant_content(self, mock_async_zep_client, mock_async_openai_client):
        """Test assistant content extraction from response."""
        wrapper = AsyncChatCompletionsWrapper(mock_async_openai_client.chat.completions, mock_async_zep_client)

        response = MockOpenAIResponse("Test assistant response")
        content = wrapper._extract_assistant_content(response)

        assert content == "Test assistant response"

    def test_extract_assistant_content_empty_response(self, mock_async_zep_client, mock_async_openai_client):
        """Test assistant content extraction from empty response."""
        wrapper = AsyncChatCompletionsWrapper(mock_async_openai_client.chat.completions, mock_async_zep_client)

        response = MagicMock()
        response.choices = []
        content = wrapper._extract_assistant_content(response)

        assert content is None


class TestAsyncResponsesWrapper:
    """Test AsyncResponsesWrapper functionality."""

    @pytest.mark.asyncio
    async def test_create_without_session_id(
        self, mock_async_zep_client, mock_async_openai_client, sample_messages_no_context
    ):
        """Test async responses creation without session_id."""
        wrapper = AsyncResponsesWrapper(mock_async_openai_client.responses, mock_async_zep_client)

        response = await wrapper.create(model="gpt-4.1-mini", messages=sample_messages_no_context)

        assert response is not None

        # Should not call Zep
        mock_async_zep_client.memory.get.assert_not_called()
        mock_async_zep_client.memory.add.assert_not_called()

    @pytest.mark.asyncio
    async def test_create_with_session_id_and_context(
        self, mock_async_zep_client, mock_async_openai_client, sample_messages
    ):
        """Test async responses creation with session_id and context."""
        wrapper = AsyncResponsesWrapper(mock_async_openai_client.responses, mock_async_zep_client)

        async def mock_add(*args, **kwargs):
            mock_response = MagicMock()
            mock_response.context = "Test context"
            return mock_response

        mock_async_zep_client.memory.add = mock_add

        async def mock_create(*args, **kwargs):
            # Verify context was injected
            messages = kwargs.get("messages", args[0] if args else [])
            if messages and "Test context" in str(messages[0].get("content", "")):
                return MockOpenAIResponsesAPI("Response with context")
            return MockOpenAIResponsesAPI("Response without context")

        mock_async_openai_client.responses.create = mock_create

        response = await wrapper.create(model="gpt-4.1-mini", messages=sample_messages, session_id="test_session")

        assert response is not None

    @pytest.mark.asyncio
    async def test_passthrough_methods(self, mock_async_zep_client, mock_async_openai_client):
        """Test that other async responses methods are passed through."""
        wrapper = AsyncResponsesWrapper(mock_async_openai_client.responses, mock_async_zep_client)

        # Test retrieve
        result = await wrapper.retrieve("resp_123")
        assert result is not None

        # Test delete
        result = await wrapper.delete("resp_123")
        assert result is not None

        # Test cancel
        result = await wrapper.cancel("resp_123")
        assert result is not None

    def test_extract_assistant_content_from_responses_api(self, mock_async_zep_client, mock_async_openai_client):
        """Test content extraction from Responses API response."""
        wrapper = AsyncResponsesWrapper(mock_async_openai_client.responses, mock_async_zep_client)

        response = MockOpenAIResponsesAPI("Responses API content")
        content = wrapper._extract_assistant_content(response)

        assert content == "Responses API content"


class TestAsyncChatWrapper:
    """Test AsyncChatWrapper functionality."""

    def test_async_chat_wrapper_delegation(self, mock_async_zep_client, mock_async_openai_client):
        """Test that AsyncChatWrapper properly delegates to wrapped completions."""
        wrapper = AsyncChatWrapper(mock_async_openai_client.chat, mock_async_zep_client)

        assert isinstance(wrapper.completions, AsyncChatCompletionsWrapper)
        assert wrapper.completions.zep_client == mock_async_zep_client

    def test_async_chat_wrapper_passthrough(self, mock_async_zep_client, mock_async_openai_client):
        """Test that other chat attributes are passed through."""
        # Add some attribute to mock chat
        mock_async_openai_client.chat.other_method = MagicMock()

        wrapper = AsyncChatWrapper(mock_async_openai_client.chat, mock_async_zep_client)

        # Should pass through unknown attributes
        assert hasattr(wrapper, "other_method")


class TestAsyncZepIntegrationBehavior:
    """Test specific async Zep integration behaviors."""

    @pytest.mark.asyncio
    async def test_context_optimization_with_new_messages(
        self, mock_async_zep_client, mock_async_openai_client, sample_messages
    ):
        """Test optimized context retrieval with new messages in async."""
        wrapper = AsyncChatCompletionsWrapper(mock_async_openai_client.chat.completions, mock_async_zep_client)

        # Mock return_context=True behavior
        async def mock_add(*args, **kwargs):
            # Verify return_context=True is passed
            if kwargs.get("return_context") is True:
                mock_response = MagicMock()
                mock_response.context = "Optimized context"
                return mock_response
            return MagicMock()

        mock_async_zep_client.memory.add = mock_add

        response = await wrapper.create(model="gpt-4.1-mini", messages=sample_messages, session_id="test_session")

        # Should not call get separately
        mock_async_zep_client.memory.get.assert_not_called()

    @pytest.mark.asyncio
    async def test_context_fallback_without_new_messages(self, mock_async_zep_client, mock_async_openai_client):
        """Test fallback to get context when no conversation messages in async."""
        messages = [
            {"role": "system", "content": "Context: {context}"}  # No user/assistant messages
        ]

        wrapper = AsyncChatCompletionsWrapper(mock_async_openai_client.chat.completions, mock_async_zep_client)

        async def mock_get(*args, **kwargs):
            return MockZepMemory("Fallback context")

        mock_async_zep_client.memory.get = mock_get

        response = await wrapper.create(model="gpt-4.1-mini", messages=messages, session_id="test_session")

        assert response is not None

    @pytest.mark.asyncio
    async def test_assistant_response_added_to_zep(
        self, mock_async_zep_client, mock_async_openai_client, sample_messages
    ):
        """Test that assistant response is added back to Zep in async."""
        wrapper = AsyncChatCompletionsWrapper(mock_async_openai_client.chat.completions, mock_async_zep_client)

        add_call_count = 0

        async def mock_add(*args, **kwargs):
            nonlocal add_call_count
            add_call_count += 1

            if add_call_count == 1:
                # First call for user messages
                mock_response = MagicMock()
                mock_response.context = "Test context"
                return mock_response
            else:
                # Second call for assistant response
                messages = kwargs.get("messages", [])
                if messages and messages[0].role == "assistant":
                    assert messages[0].content == "Assistant reply"
                return MagicMock()

        mock_async_zep_client.memory.add = mock_add

        async def mock_create(*args, **kwargs):
            return MockOpenAIResponse("Assistant reply")

        mock_async_openai_client.chat.completions.create = mock_create

        response = await wrapper.create(model="gpt-4.1-mini", messages=sample_messages, session_id="test_session")

        # Should have two add calls: one for user messages, one for assistant response
        assert add_call_count == 2


class TestAsyncParameterHandling:
    """Test async parameter handling and filtering."""

    @pytest.mark.asyncio
    async def test_zep_parameters_filtered_from_openai_call(
        self, mock_async_zep_client, mock_async_openai_client, sample_messages_no_context
    ):
        """Test that Zep-specific parameters are filtered out in async."""
        wrapper = AsyncChatCompletionsWrapper(mock_async_openai_client.chat.completions, mock_async_zep_client)

        passed_params = {}

        async def mock_create(*args, **kwargs):
            nonlocal passed_params
            passed_params = kwargs
            return MockOpenAIResponse("Test")

        mock_async_openai_client.chat.completions.create = mock_create

        response = await wrapper.create(
            model="gpt-4.1-mini",
            messages=sample_messages_no_context,
            session_id="test_session",  # Should be filtered
            context_placeholder="{{memory}}",  # Should be filtered
            skip_zep_on_error=False,  # Should be filtered
            temperature=0.7,  # Should be passed through
            max_tokens=100,  # Should be passed through
        )

        # Check that only OpenAI parameters were passed
        assert "model" in passed_params
        assert "temperature" in passed_params
        assert "max_tokens" in passed_params
        assert "session_id" not in passed_params
        assert "context_placeholder" not in passed_params
        assert "skip_zep_on_error" not in passed_params


class TestAsyncErrorHandling:
    """Test async error handling scenarios."""

    @pytest.mark.asyncio
    async def test_skip_zep_on_error_true(self, mock_async_zep_client, mock_async_openai_client, sample_messages):
        """Test skip_zep_on_error=True behavior in async."""
        wrapper = AsyncChatCompletionsWrapper(mock_async_openai_client.chat.completions, mock_async_zep_client)

        # Make Zep operation fail
        async def mock_add_fail(*args, **kwargs):
            raise Exception("Zep is down")

        mock_async_zep_client.memory.add = mock_add_fail

        # Should not raise error and continue with OpenAI call
        response = await wrapper.create(
            model="gpt-4.1-mini", messages=sample_messages, session_id="test_session", skip_zep_on_error=True
        )

        assert response is not None

    @pytest.mark.asyncio
    async def test_skip_zep_on_error_false(self, mock_async_zep_client, mock_async_openai_client, sample_messages):
        """Test skip_zep_on_error=False behavior in async."""
        wrapper = AsyncChatCompletionsWrapper(mock_async_openai_client.chat.completions, mock_async_zep_client)

        # Make Zep operation fail
        async def mock_add_fail(*args, **kwargs):
            raise Exception("Zep is down")

        mock_async_zep_client.memory.add = mock_add_fail

        # Should raise ZepOpenAIError
        from zep_cloud.openai.openai_utils import ZepOpenAIError

        with pytest.raises(ZepOpenAIError):
            await wrapper.create(
                model="gpt-4.1-mini", messages=sample_messages, session_id="test_session", skip_zep_on_error=False
            )
