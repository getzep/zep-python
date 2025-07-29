"""
Test fixtures for OpenAI wrapper tests.
"""

from datetime import datetime
from typing import List, Optional
from unittest.mock import MagicMock

import pytest
from zep_cloud.types import AddThreadMessagesResponse, Message


class MockOpenAIChoice:
    """Mock OpenAI chat completion choice."""

    def __init__(self, content: str, role: str = "assistant"):
        self.message = MagicMock()
        self.message.content = content
        self.message.role = role
        self.finish_reason = "stop"
        self.index = 0


class MockOpenAIDelta:
    """Mock OpenAI streaming delta."""

    def __init__(self, content: Optional[str] = None):
        self.content = content
        self.role = None


class MockOpenAIStreamChunk:
    """Mock OpenAI streaming chunk."""

    def __init__(self, content: Optional[str] = None):
        self.choices = [MagicMock()]
        self.choices[0].delta = MockOpenAIDelta(content)
        self.choices[0].index = 0
        self.choices[0].finish_reason = None


class MockOpenAIResponse:
    """Mock OpenAI chat completion response."""

    def __init__(self, content: str = "Test response"):
        self.choices = [MockOpenAIChoice(content)]
        self.id = "chatcmpl-test123"
        self.model = "gpt-4.1-mini"
        self.usage = MagicMock()
        self.usage.prompt_tokens = 10
        self.usage.completion_tokens = 5
        self.usage.total_tokens = 15


class MockOpenAIResponsesAPI:
    """Mock OpenAI Responses API response."""

    def __init__(self, content: str = "Test response"):
        self.id = "resp_test123"
        self.model = "gpt-4.1-mini"
        self.output = [MagicMock()]
        self.output[0].type = "message"
        self.output[0].role = "assistant"
        self.output[0].content = [MagicMock()]
        self.output[0].content[0].type = "output_text"
        self.output[0].content[0].text = content


class MockZepMemory:
    """Mock Zep memory response."""

    def __init__(self, context: str = "Test context"):
        self.context = context
        self.messages = [
            Message(name="user", role="user", content="Hello", created_at=datetime.now().isoformat()),
            Message(
                name="assistant", role="assistant", content="Hi there!", created_at=datetime.now().isoformat()
            ),
        ]


class MockStream:
    """Mock streaming iterator."""

    def __init__(self, chunks: List[str]):
        self.chunks = chunks
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self.chunks):
            raise StopIteration
        chunk = MockOpenAIStreamChunk(self.chunks[self._index])
        self._index += 1
        return chunk


class MockAsyncStream:
    """Mock async streaming iterator."""

    def __init__(self, chunks: List[str]):
        self.chunks = chunks
        self._index = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self._index >= len(self.chunks):
            raise StopAsyncIteration
        chunk = MockOpenAIStreamChunk(self.chunks[self._index])
        self._index += 1
        return chunk


@pytest.fixture
def mock_openai_response():
    """Mock OpenAI chat completion response."""
    return MockOpenAIResponse("Hello! How can I help you today?")


@pytest.fixture
def mock_openai_responses_api():
    """Mock OpenAI Responses API response."""
    return MockOpenAIResponsesAPI("Hello! How can I help you today?")


@pytest.fixture
def mock_zep_memory():
    """Mock Zep memory response."""
    return MockZepMemory("Previous conversation context")


@pytest.fixture
def mock_zep_add_response():
    """Mock Zep add memory response."""
    return AddThreadMessagesResponse(context="Updated context with new message")


@pytest.fixture
def mock_stream_chunks():
    """Mock streaming chunks."""
    return ["Hello", " there", "! How", " can I", " help", " you?"]


@pytest.fixture
def sample_messages():
    """Sample message list for testing."""
    return [
        {"role": "system", "content": "You are helpful. Context: {context}"},
        {"role": "user", "content": "What's my name?"},
    ]


@pytest.fixture
def sample_messages_no_context():
    """Sample message list without context placeholder."""
    return [{"role": "system", "content": "You are helpful."}, {"role": "user", "content": "Hello!"}]


@pytest.fixture
def conversation_messages():
    """Sample conversation messages for Zep."""
    return [
        Message(name="user", role="user", content="My name is Alice", created_at=datetime.now().isoformat()),
        Message(
            name="assistant",
            role="assistant",
            content="Nice to meet you, Alice!",
            created_at=datetime.now().isoformat(),
        ),
    ]


def create_mock_openai_client():
    """Create a mock OpenAI client."""
    client = MagicMock()

    # Mock chat completions
    client.chat.completions.create.return_value = MockOpenAIResponse()

    # Mock responses API
    client.responses.create.return_value = MockOpenAIResponsesAPI()
    client.responses.retrieve.return_value = MockOpenAIResponsesAPI()
    client.responses.delete.return_value = {"deleted": True}
    client.responses.cancel.return_value = {"cancelled": True}

    return client


@pytest.fixture
def mock_openai_client():
    """Mock OpenAI client."""
    return create_mock_openai_client()


@pytest.fixture
def mock_async_openai_client():
    """Mock async OpenAI client."""
    client = MagicMock()

    # Mock async chat completions
    async def mock_create(*args, **kwargs):
        return MockOpenAIResponse()

    client.chat.completions.create = mock_create

    # Mock async responses API
    async def mock_responses_create(*args, **kwargs):
        return MockOpenAIResponsesAPI()

    client.responses.create = mock_responses_create

    async def mock_retrieve(*args, **kwargs):
        return MockOpenAIResponsesAPI()

    client.responses.retrieve = mock_retrieve

    async def mock_delete(*args, **kwargs):
        return {"deleted": True}

    client.responses.delete = mock_delete

    async def mock_cancel(*args, **kwargs):
        return {"cancelled": True}

    client.responses.cancel = mock_cancel

    return client


@pytest.fixture
def mock_zep_client():
    """Mock Zep client."""
    client = MagicMock()

    # Mock thread operations
    mock_context_response = MagicMock()
    mock_context_response.context = "Test context"
    
    client.thread.add_messages.return_value = mock_context_response
    client.thread.get_user_context.return_value = mock_context_response

    return client


@pytest.fixture
def mock_async_zep_client():
    """Mock async Zep client."""
    client = MagicMock()

    # Mock async thread operations with MagicMock support
    async def mock_add_messages(*args, **kwargs):
        mock_response = MagicMock()
        mock_response.context = "Test context"
        return mock_response

    async def mock_get_context(*args, **kwargs):
        mock_response = MagicMock()
        mock_response.context = "Test context"
        return mock_response

    # Create MagicMock objects that support both async calls and assert methods
    client.thread.add_messages = MagicMock(side_effect=mock_add_messages)
    client.thread.get_user_context = MagicMock(side_effect=mock_get_context)

    return client


@pytest.fixture
def error_responses():
    """Error responses for testing."""
    return {
        "openai_error": Exception("OpenAI API error"),
        "zep_error": Exception("Zep API error"),
        "network_error": ConnectionError("Network connection failed"),
    }
