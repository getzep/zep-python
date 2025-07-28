"""
Tests for OpenAI wrapper utility functions.
"""

import pytest
from zep_cloud.external_clients.openai_utils import (
    ZepOpenAIError,
    extract_conversation_messages,
    extract_zep_params,
    has_context_placeholder,
    inject_context,
    normalize_messages_for_zep,
    remove_zep_params,
    safe_zep_operation,
)
from zep_cloud.types import Message


class TestParameterHandling:
    """Test parameter extraction and filtering functions."""

    def test_extract_zep_params(self):
        """Test extraction of Zep-specific parameters."""
        kwargs = {
            "model": "gpt-4.1-mini",
            "session_id": "test_session",
            "context_placeholder": "{{memory}}",
            "skip_zep_on_error": False,
            "temperature": 0.7,
            "max_tokens": 100,
        }

        zep_params = extract_zep_params(kwargs)

        assert zep_params == {
            "session_id": "test_session",
            "context_placeholder": "{{memory}}",
            "skip_zep_on_error": False,
        }

        # Original kwargs should be modified
        assert kwargs == {"model": "gpt-4.1-mini", "temperature": 0.7, "max_tokens": 100}

    def test_extract_zep_params_empty(self):
        """Test extraction when no Zep params are present."""
        kwargs = {"model": "gpt-4.1-mini", "temperature": 0.7}
        zep_params = extract_zep_params(kwargs)

        assert zep_params == {}
        assert kwargs == {"model": "gpt-4.1-mini", "temperature": 0.7}

    def test_remove_zep_params(self):
        """Test removal of Zep-specific parameters."""
        kwargs = {
            "model": "gpt-4.1-mini",
            "session_id": "test_session",
            "context_placeholder": "{{memory}}",
            "temperature": 0.7,
        }

        clean_params = remove_zep_params(kwargs)

        assert clean_params == {"model": "gpt-4.1-mini", "temperature": 0.7}
        # Original kwargs should not be modified
        assert "session_id" in kwargs


class TestContextHandling:
    """Test context placeholder detection and injection."""

    def test_has_context_placeholder_default(self):
        """Test context placeholder detection with default placeholder."""
        messages = [
            {"role": "system", "content": "You are helpful. Context: {context}"},
            {"role": "user", "content": "Hello"},
        ]

        assert has_context_placeholder(messages) is True

    def test_has_context_placeholder_custom(self):
        """Test context placeholder detection with custom placeholder."""
        messages = [
            {"role": "system", "content": "You are helpful. Memory: {{memory}}"},
            {"role": "user", "content": "Hello"},
        ]

        assert has_context_placeholder(messages, "{{memory}}") is True
        assert has_context_placeholder(messages, "{context}") is False

    def test_has_context_placeholder_none(self):
        """Test when no context placeholder is present."""
        messages = [{"role": "system", "content": "You are helpful."}, {"role": "user", "content": "Hello"}]

        assert has_context_placeholder(messages) is False

    def test_has_context_placeholder_non_string_content(self):
        """Test with non-string content."""
        messages = [{"role": "system", "content": ["You are helpful"]}, {"role": "user", "content": None}]

        assert has_context_placeholder(messages) is False

    def test_inject_context_default_placeholder(self):
        """Test context injection with default placeholder."""
        messages = [
            {"role": "system", "content": "You are helpful. Context: {context}"},
            {"role": "user", "content": "What's my name?"},
        ]

        result = inject_context(messages, "Alice loves pizza")

        assert result[0]["content"] == "You are helpful. Context: Alice loves pizza"
        assert result[1]["content"] == "What's my name?"
        # Original messages should not be modified
        assert messages[0]["content"] == "You are helpful. Context: {context}"

    def test_inject_context_custom_placeholder(self):
        """Test context injection with custom placeholder."""
        messages = [{"role": "system", "content": "Memory: {{memory}} - Use this."}]

        result = inject_context(messages, "Previous chat", "{{memory}}")

        assert result[0]["content"] == "Memory: Previous chat - Use this."

    def test_inject_context_none(self):
        """Test context injection with None context."""
        messages = [{"role": "system", "content": "Context: {context}"}]

        result = inject_context(messages, None)

        assert result[0]["content"] == "Context: "

    def test_inject_context_empty_string(self):
        """Test context injection with empty context."""
        messages = [{"role": "system", "content": "Context: {context}"}]

        result = inject_context(messages, "")

        assert result[0]["content"] == "Context: "

    def test_inject_context_multiple_occurrences(self):
        """Test context injection with multiple placeholder occurrences."""
        messages = [{"role": "system", "content": "Start: {context} End: {context}"}]

        result = inject_context(messages, "CONTEXT")

        assert result[0]["content"] == "Start: CONTEXT End: CONTEXT"


class TestMessageConversion:
    """Test message conversion functions."""

    def test_extract_conversation_messages(self):
        """Test extraction of conversation messages."""
        openai_messages = [
            {"role": "system", "content": "You are helpful"},
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there!"},
            {"role": "function", "content": "Function result"},
        ]

        result = extract_conversation_messages(openai_messages)

        assert len(result) == 2
        assert result[0].role == "user"
        assert result[0].role_type == "user"
        assert result[0].content == "Hello"
        assert result[1].role == "assistant"
        assert result[1].role_type == "assistant"
        assert result[1].content == "Hi there!"

    def test_extract_conversation_messages_empty_content(self):
        """Test extraction with empty content."""
        openai_messages = [
            {"role": "user", "content": ""},
            {"role": "assistant", "content": None},
            {"role": "user", "content": "Valid message"},
        ]

        result = extract_conversation_messages(openai_messages)

        assert len(result) == 1
        assert result[0].content == "Valid message"

    def test_extract_conversation_messages_user_only(self):
        """Test extraction with user_only=True to prevent assistant message duplication."""
        messages = [
            {"role": "system", "content": "System message"},
            {"role": "user", "content": "User message 1"},
            {"role": "assistant", "content": "Assistant response 1"},
            {"role": "user", "content": "User message 2"},
        ]

        # With user_only=True, should only extract user messages
        result = extract_conversation_messages(messages, user_only=True)

        assert len(result) == 2
        assert all(msg.role == "user" for msg in result)
        assert all(msg.role_type == "user" for msg in result)
        assert result[0].content == "User message 1"
        assert result[1].content == "User message 2"

        # With user_only=False (default), should extract both user and assistant
        result_all = extract_conversation_messages(messages, user_only=False)

        assert len(result_all) == 3
        assert result_all[0].role == "user"
        assert result_all[1].role == "assistant"
        assert result_all[2].role == "user"

    def test_normalize_messages_for_zep_chat(self):
        """Test message normalization for chat API."""
        messages = [{"role": "user", "content": "Hello"}, {"role": "assistant", "content": "Hi!"}]

        result = normalize_messages_for_zep(messages, "chat")

        assert len(result) == 2
        assert isinstance(result[0], Message)
        assert result[0].role == "user"

    def test_normalize_messages_for_zep_responses(self):
        """Test message normalization for responses API."""
        messages = [{"role": "user", "content": "Hello"}, {"role": "assistant", "content": "Hi!"}]

        result = normalize_messages_for_zep(messages, "responses")

        assert len(result) == 2
        assert isinstance(result[0], Message)
        assert result[0].role == "user"


class TestSafeOperation:
    """Test safe operation execution with error handling."""

    def test_safe_zep_operation_success(self):
        """Test successful operation execution."""

        def successful_operation():
            return "success"

        result = safe_zep_operation(successful_operation, skip_on_error=True)
        assert result == "success"

    def test_safe_zep_operation_skip_error(self):
        """Test operation with skip_on_error=True."""

        def failing_operation():
            raise ValueError("Test error")

        result = safe_zep_operation(failing_operation, skip_on_error=True)
        assert result is None

    def test_safe_zep_operation_raise_error(self):
        """Test operation with skip_on_error=False."""

        def failing_operation():
            raise ValueError("Test error")

        with pytest.raises(ZepOpenAIError) as exc_info:
            safe_zep_operation(failing_operation, skip_on_error=False)

        assert "Test error" in str(exc_info.value)
        assert exc_info.value.__cause__.__class__ == ValueError

    def test_safe_zep_operation_custom_name(self):
        """Test operation with custom operation name."""

        def failing_operation():
            raise RuntimeError("Custom error")

        with pytest.raises(ZepOpenAIError) as exc_info:
            safe_zep_operation(failing_operation, skip_on_error=False, operation_name="Custom operation")

        assert "Custom operation failed" in str(exc_info.value)


class TestZepOpenAIError:
    """Test custom exception class."""

    def test_zep_openai_error_creation(self):
        """Test ZepOpenAIError creation."""
        error = ZepOpenAIError("Test error message")
        assert str(error) == "Test error message"
        assert isinstance(error, Exception)

    def test_zep_openai_error_with_cause(self):
        """Test ZepOpenAIError with cause."""
        original_error = ValueError("Original error")

        try:
            raise ZepOpenAIError("Wrapper error") from original_error
        except ZepOpenAIError as error:
            assert str(error) == "Wrapper error"
            assert error.__cause__ == original_error


class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_empty_messages_list(self):
        """Test with empty messages list."""
        messages = []

        assert has_context_placeholder(messages) is False
        assert inject_context(messages, "context") == []
        assert extract_conversation_messages(messages) == []

    def test_malformed_messages(self):
        """Test with malformed message structures."""
        messages = [
            {"content": "Missing role"},
            {"role": "user"},  # Missing content
            {},  # Empty message
        ]

        # Should not crash, but should handle gracefully
        result = extract_conversation_messages(messages)
        assert result == []

    def test_context_placeholder_edge_cases(self):
        """Test context placeholder with edge cases."""
        # Empty placeholder
        messages = [{"role": "system", "content": "Test"}]
        assert has_context_placeholder(messages, "") is False

        # Very long placeholder
        long_placeholder = "{" + "x" * 1000 + "}"
        messages = [{"role": "system", "content": f"Test {long_placeholder}"}]
        assert has_context_placeholder(messages, long_placeholder) is True

    def test_context_placeholder_optimization_large_list(self):
        """Test context placeholder optimization with large message lists."""
        # Create a large message list
        messages = []

        # Add system message with placeholder (should be found quickly)
        messages.append({"role": "system", "content": "You are helpful. Context: {context}"})

        # Add many user/assistant messages without placeholders
        for i in range(100):
            messages.append({"role": "user", "content": f"User message {i}"})
            messages.append({"role": "assistant", "content": f"Assistant response {i}"})

        # Should find the placeholder in system message efficiently
        assert has_context_placeholder(messages, "{context}")

        # Test with placeholder in early non-system message
        messages_early = []
        messages_early.append({"role": "user", "content": "Hello with {context}"})
        for i in range(100):
            messages_early.append({"role": "user", "content": f"User message {i}"})

        assert has_context_placeholder(messages_early, "{context}")

        # Test with placeholder in later message (should still be found)
        messages_late = []
        for i in range(10):
            messages_late.append({"role": "user", "content": f"User message {i}"})
        messages_late.append({"role": "user", "content": "Message with {context}"})

        assert has_context_placeholder(messages_late, "{context}")

        # Test with no placeholder in large list
        messages_no_placeholder = []
        for i in range(100):
            messages_no_placeholder.append({"role": "user", "content": f"User message {i}"})

        assert not has_context_placeholder(messages_no_placeholder, "{context}")
