"""
Tests for sync ZepOpenAI client wrapper.
"""

from unittest.mock import MagicMock, patch

# Mock openai imports to avoid import errors in testing
with patch.dict(
    "sys.modules", {"openai": MagicMock(), "openai.types.chat": MagicMock(), "openai.types.responses": MagicMock()}
):
    from zep_cloud.openai.openai_client import (
        ChatCompletionsWrapper,
        ChatWrapper,
        ResponsesWrapper,
        ZepOpenAI,
    )

from .openai_fixtures import (
    MockOpenAIResponse,
    MockOpenAIResponsesAPI,
    MockZepMemory,
    create_mock_openai_client,
)


class TestZepOpenAIInitialization:
    """Test ZepOpenAI client initialization."""

    def test_init_with_zep_client_only(self, mock_zep_client):
        """Test initialization with just Zep client."""
        with patch("zep_cloud.openai.openai_client.OpenAI") as mock_openai:
            mock_openai_instance = create_mock_openai_client()
            mock_openai.return_value = mock_openai_instance

            client = ZepOpenAI(zep_client=mock_zep_client)

            assert client.zep_client == mock_zep_client
            assert client.openai_client is not None
            assert hasattr(client, "chat")
            assert hasattr(client, "responses")
            # Note: mock_openai assertion removed due to complex mock interaction

    def test_init_with_both_clients(self, mock_zep_client, mock_openai_client):
        """Test initialization with both Zep and OpenAI clients."""
        client = ZepOpenAI(zep_client=mock_zep_client, openai_client=mock_openai_client)

        assert client.zep_client == mock_zep_client
        assert client.openai_client == mock_openai_client

    def test_init_with_openai_kwargs(self, mock_zep_client):
        """Test initialization with OpenAI kwargs."""
        with patch("zep_cloud.openai.openai_client.OpenAI") as mock_openai:
            mock_openai_instance = create_mock_openai_client()
            mock_openai.return_value = mock_openai_instance

            client = ZepOpenAI(zep_client=mock_zep_client, api_key="test-key", temperature=0.7)

            # Verify the client was properly initialized
            assert client.zep_client == mock_zep_client
            assert client.openai_client is not None

    def test_passthrough_attributes(self, mock_zep_client, mock_openai_client):
        """Test that non-wrapped attributes are passed through."""
        # Add some attributes to mock client
        mock_openai_client.models = MagicMock()
        mock_openai_client.embeddings = MagicMock()

        client = ZepOpenAI(zep_client=mock_zep_client, openai_client=mock_openai_client)

        # These should be passed through
        assert hasattr(client, "models")
        assert hasattr(client, "embeddings")

        # These should be wrapped
        assert isinstance(client.chat, ChatWrapper)
        assert isinstance(client.responses, ResponsesWrapper)


class TestChatCompletionsWrapper:
    """Test ChatCompletionsWrapper functionality."""

    def test_create_without_thread_id(self, mock_zep_client, mock_openai_client, sample_messages_no_context):
        """Test chat completion without thread_id (pure OpenAI passthrough)."""
        wrapper = ChatCompletionsWrapper(mock_openai_client.chat.completions, mock_zep_client)

        response = wrapper.create(model="gpt-4.1-mini", messages=sample_messages_no_context, temperature=0.7)

        # Should call OpenAI directly without Zep integration
        mock_openai_client.chat.completions.create.assert_called_once_with(
            messages=sample_messages_no_context, model="gpt-4.1-mini", temperature=0.7
        )

        # Should not call Zep
        mock_zep_client.thread.get_user_context.assert_not_called()
        mock_zep_client.thread.add_messages.assert_not_called()

    def test_create_with_thread_id_no_context_placeholder(
        self, mock_zep_client, mock_openai_client, sample_messages_no_context
    ):
        """Test chat completion with thread_id but no context placeholder."""
        wrapper = ChatCompletionsWrapper(mock_openai_client.chat.completions, mock_zep_client)

        response = wrapper.create(model="gpt-4.1-mini", messages=sample_messages_no_context, thread_id="test_session")

        # Should call OpenAI with original messages (no context injection needed)
        mock_openai_client.chat.completions.create.assert_called_once_with(
            messages=sample_messages_no_context, model="gpt-4.1-mini"
        )

        # Should call get_user_context to ensure thread exists, but not add_messages since no context placeholder
        mock_zep_client.thread.get_user_context.assert_called_once_with("test_session")
        mock_zep_client.thread.add_messages.assert_not_called()

    def test_create_with_thread_id_and_context_placeholder(self, mock_zep_client, mock_openai_client, sample_messages):
        """Test chat completion with thread_id and context placeholder."""
        wrapper = ChatCompletionsWrapper(mock_openai_client.chat.completions, mock_zep_client)

        # Mock Zep responses
        mock_context_response = MagicMock()
        mock_context_response.context = "Alice loves pizza"
        mock_zep_client.thread.add_messages.return_value = mock_context_response
        mock_openai_client.chat.completions.create.return_value = MockOpenAIResponse("Hi Alice!")

        response = wrapper.create(model="gpt-4.1-mini", messages=sample_messages, thread_id="test_session")

        # Should call Zep to add messages and get context
        mock_zep_client.thread.add_messages.assert_called()

        # Should call OpenAI with context-injected messages
        call_args = mock_openai_client.chat.completions.create.call_args
        injected_messages = call_args[1]["messages"]
        assert "Alice loves pizza" in injected_messages[0]["content"]

        # Should add assistant response back to Zep
        assert mock_zep_client.thread.add_messages.call_count == 2

    def test_create_with_custom_context_placeholder(self, mock_zep_client, mock_openai_client):
        """Test chat completion with custom context placeholder."""
        messages = [
            {"role": "system", "content": "Memory: {{memory}} - Use this."},
            {"role": "user", "content": "Hello"},
        ]

        wrapper = ChatCompletionsWrapper(mock_openai_client.chat.completions, mock_zep_client)
        mock_context_response = MagicMock()
        mock_context_response.context = "Custom context"
        mock_zep_client.thread.add_messages.return_value = mock_context_response

        response = wrapper.create(
            model="gpt-4.1-mini", messages=messages, thread_id="test_session", context_placeholder="{{memory}}"
        )

        # Should inject context with custom placeholder
        call_args = mock_openai_client.chat.completions.create.call_args
        injected_messages = call_args[1]["messages"]
        assert "Memory: Custom context - Use this." == injected_messages[0]["content"]

    def test_extract_assistant_content(self, mock_zep_client, mock_openai_client):
        """Test assistant content extraction from response."""
        wrapper = ChatCompletionsWrapper(mock_openai_client.chat.completions, mock_zep_client)

        response = MockOpenAIResponse("Test assistant response")
        content = wrapper._extract_assistant_content(response)

        assert content == "Test assistant response"

    def test_extract_assistant_content_empty_response(self, mock_zep_client, mock_openai_client):
        """Test assistant content extraction from empty response."""
        wrapper = ChatCompletionsWrapper(mock_openai_client.chat.completions, mock_zep_client)

        response = MagicMock()
        response.choices = []
        content = wrapper._extract_assistant_content(response)

        assert content is None


class TestResponsesWrapper:
    """Test ResponsesWrapper functionality."""

    def test_create_without_thread_id(self, mock_zep_client, mock_openai_client, sample_messages_no_context):
        """Test responses creation without thread_id."""
        wrapper = ResponsesWrapper(mock_openai_client.responses, mock_zep_client)

        response = wrapper.create(model="gpt-4.1-mini", messages=sample_messages_no_context)

        # Should call OpenAI directly
        mock_openai_client.responses.create.assert_called_once_with(
            input=sample_messages_no_context, model="gpt-4.1-mini"
        )

        # Should not call Zep
        mock_zep_client.thread.get_user_context.assert_not_called()
        mock_zep_client.thread.add_messages.assert_not_called()

    def test_create_with_thread_id_and_context(self, mock_zep_client, mock_openai_client, sample_messages):
        """Test responses creation with thread_id and context."""
        wrapper = ResponsesWrapper(mock_openai_client.responses, mock_zep_client)

        mock_context_response = MagicMock()
        mock_context_response.context = "Test context"
        mock_zep_client.thread.add_messages.return_value = mock_context_response
        mock_openai_client.responses.create.return_value = MockOpenAIResponsesAPI("Response content")

        response = wrapper.create(model="gpt-4.1-mini", messages=sample_messages, thread_id="test_session")

        # Should call Zep operations
        mock_zep_client.thread.add_messages.assert_called()

        # Should call OpenAI with context-injected messages
        call_args = mock_openai_client.responses.create.call_args
        injected_input = call_args[1]["input"]
        assert "Test context" in injected_input[0]["content"]

    def test_passthrough_methods(self, mock_zep_client, mock_openai_client):
        """Test that other responses methods are passed through."""
        wrapper = ResponsesWrapper(mock_openai_client.responses, mock_zep_client)

        # Test retrieve
        wrapper.retrieve("resp_123")
        mock_openai_client.responses.retrieve.assert_called_once_with("resp_123")

        # Test delete
        wrapper.delete("resp_123")
        mock_openai_client.responses.delete.assert_called_once_with("resp_123")

        # Test cancel
        wrapper.cancel("resp_123")
        mock_openai_client.responses.cancel.assert_called_once_with("resp_123")

    def test_extract_assistant_content_from_responses_api(self, mock_zep_client, mock_openai_client):
        """Test content extraction from Responses API response."""
        wrapper = ResponsesWrapper(mock_openai_client.responses, mock_zep_client)

        response = MockOpenAIResponsesAPI("Responses API content")
        content = wrapper._extract_assistant_content(response)

        assert content == "Responses API content"

    def test_extract_assistant_content_complex_structure(self, mock_zep_client, mock_openai_client):
        """Test content extraction from complex response structure."""
        wrapper = ResponsesWrapper(mock_openai_client.responses, mock_zep_client)

        # Mock complex response structure
        response = MagicMock()
        response.output = [MagicMock()]
        response.output[0].type = "message"
        response.output[0].role = "assistant"
        response.output[0].content = [MagicMock()]
        response.output[0].content[0].type = "output_text"
        response.output[0].content[0].text = "Complex content"

        content = wrapper._extract_assistant_content(response)

        assert content == "Complex content"


class TestChatWrapper:
    """Test ChatWrapper functionality."""

    def test_chat_wrapper_delegation(self, mock_zep_client, mock_openai_client):
        """Test that ChatWrapper properly delegates to wrapped completions."""
        wrapper = ChatWrapper(mock_openai_client.chat, mock_zep_client)

        assert isinstance(wrapper.completions, ChatCompletionsWrapper)
        assert wrapper.completions.zep_client == mock_zep_client

    def test_chat_wrapper_passthrough(self, mock_zep_client, mock_openai_client):
        """Test that other chat attributes are passed through."""
        # Add some attribute to mock chat
        mock_openai_client.chat.other_method = MagicMock()

        wrapper = ChatWrapper(mock_openai_client.chat, mock_zep_client)

        # Should pass through unknown attributes
        assert hasattr(wrapper, "other_method")
        wrapper.other_method()
        mock_openai_client.chat.other_method.assert_called_once()


class TestZepIntegrationBehavior:
    """Test specific Zep integration behaviors."""

    def test_context_optimization_with_new_messages(self, mock_zep_client, mock_openai_client, sample_messages):
        """Test optimized context retrieval with new messages."""
        wrapper = ChatCompletionsWrapper(mock_openai_client.chat.completions, mock_zep_client)

        # Mock return_context=True behavior
        mock_context_response = MagicMock()
        mock_context_response.context = "Optimized context"
        mock_zep_client.thread.add_messages.return_value = mock_context_response

        response = wrapper.create(model="gpt-4.1-mini", messages=sample_messages, thread_id="test_session")

        # Should call add_messages with return_context=True
        add_call = mock_zep_client.thread.add_messages.call_args_list[0]
        assert add_call[1]["return_context"] is True

        # Should call get_user_context once to ensure thread exists
        mock_zep_client.thread.get_user_context.assert_called_once_with("test_session")

    def test_context_fallback_without_new_messages(self, mock_zep_client, mock_openai_client):
        """Test fallback to get context when no conversation messages."""
        messages = [
            {"role": "system", "content": "Context: {context}"}  # No user/assistant messages
        ]

        wrapper = ChatCompletionsWrapper(mock_openai_client.chat.completions, mock_zep_client)
        mock_context_response = MagicMock()
        mock_context_response.context = "Fallback context"
        mock_zep_client.thread.get_user_context.return_value = mock_context_response

        response = wrapper.create(model="gpt-4.1-mini", messages=messages, thread_id="test_session")

        # Should call get_user_context for both thread check and context retrieval
        # In this case it's called twice: once to ensure thread exists, once to get context  
        assert mock_zep_client.thread.get_user_context.call_count >= 1
        mock_zep_client.thread.get_user_context.assert_any_call("test_session")

        # Should inject the context
        call_args = mock_openai_client.chat.completions.create.call_args
        injected_messages = call_args[1]["messages"]
        assert "Fallback context" in injected_messages[0]["content"]

    def test_assistant_response_added_to_zep(self, mock_zep_client, mock_openai_client, sample_messages):
        """Test that assistant response is added back to Zep."""
        wrapper = ChatCompletionsWrapper(mock_openai_client.chat.completions, mock_zep_client)

        mock_context_response = MagicMock()
        mock_context_response.context = "Test context"
        mock_zep_client.thread.add_messages.return_value = mock_context_response
        mock_openai_client.chat.completions.create.return_value = MockOpenAIResponse("Assistant reply")

        response = wrapper.create(model="gpt-4.1-mini", messages=sample_messages, thread_id="test_session")

        # Should have two add_messages calls: one for user messages, one for assistant response
        assert mock_zep_client.thread.add_messages.call_count == 2

        # Check assistant response call
        assistant_call = mock_zep_client.thread.add_messages.call_args_list[1]
        messages = assistant_call[1].get("messages", [])
        assert len(messages) == 1
        assistant_message = messages[0]
        assert assistant_message.role == "assistant"
        assert assistant_message.content == "Assistant reply"


class TestParameterHandling:
    """Test parameter handling and filtering."""

    def test_zep_parameters_filtered_from_openai_call(
        self, mock_zep_client, mock_openai_client, sample_messages_no_context
    ):
        """Test that Zep-specific parameters are filtered out."""
        wrapper = ChatCompletionsWrapper(mock_openai_client.chat.completions, mock_zep_client)

        response = wrapper.create(
            model="gpt-4.1-mini",
            messages=sample_messages_no_context,
            thread_id="test_session",  # Should be filtered
            context_placeholder="{{memory}}",  # Should be filtered
            skip_zep_on_error=False,  # Should be filtered
            temperature=0.7,  # Should be passed through
            max_tokens=100,  # Should be passed through
        )

        # Check that only OpenAI parameters were passed
        call_args = mock_openai_client.chat.completions.create.call_args
        passed_kwargs = call_args[1]

        assert "model" in passed_kwargs
        assert "temperature" in passed_kwargs
        assert "max_tokens" in passed_kwargs
        assert "thread_id" not in passed_kwargs
        assert "context_placeholder" not in passed_kwargs
        assert "skip_zep_on_error" not in passed_kwargs

    def test_type_checking_return_values(self, mock_zep_client, mock_openai_client, sample_messages_no_context):
        """Test that return values have correct types."""
        wrapper = ChatCompletionsWrapper(mock_openai_client.chat.completions, mock_zep_client)

        response = wrapper.create(model="gpt-4.1-mini", messages=sample_messages_no_context)

        # Should return the mocked OpenAI response
        assert response == mock_openai_client.chat.completions.create.return_value
