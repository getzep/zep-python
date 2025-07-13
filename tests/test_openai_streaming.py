"""
Tests for OpenAI wrapper streaming functionality.
"""

import pytest
from unittest.mock import MagicMock, patch

from zep_cloud.external_clients.openai_streaming import (
    AsyncZepStreamWrapper,
    ZepStreamWrapper,
)
from zep_cloud.types import Message

from .openai_fixtures import (
    MockAsyncStream,
    MockStream,
    mock_async_zep_client,
    mock_stream_chunks,
    mock_zep_client,
)


class TestZepStreamWrapper:
    """Test sync ZepStreamWrapper functionality."""
    
    def test_stream_wrapper_initialization(self, mock_zep_client, mock_stream_chunks):
        """Test ZepStreamWrapper initialization."""
        stream = MockStream(mock_stream_chunks)
        extract_func = lambda x: "test content"
        
        wrapper = ZepStreamWrapper(
            stream=stream,
            session_id="test_session",
            zep_client=mock_zep_client,
            extract_content_func=extract_func,
            skip_zep_on_error=True
        )
        
        assert wrapper.stream == stream
        assert wrapper.session_id == "test_session"
        assert wrapper.zep_client == mock_zep_client
        assert wrapper.extract_content_func == extract_func
        assert wrapper.skip_zep_on_error is True
        assert wrapper._collected_content == []
    
    def test_stream_iteration(self, mock_zep_client, mock_stream_chunks):
        """Test streaming through wrapper with content collection."""
        stream = MockStream(mock_stream_chunks)
        
        wrapper = ZepStreamWrapper(
            stream=stream,
            session_id="test_session",
            zep_client=mock_zep_client,
            extract_content_func=lambda x: x.choices[0].delta.content,
            skip_zep_on_error=True
        )
        
        collected_chunks = []
        collected_content = []
        
        for chunk in wrapper:
            collected_chunks.append(chunk)
            if hasattr(chunk, 'choices') and chunk.choices[0].delta.content:
                collected_content.append(chunk.choices[0].delta.content)
        
        # Should have iterated through all chunks
        assert len(collected_chunks) == len(mock_stream_chunks)
        assert collected_content == mock_stream_chunks
        
        # Should have added content to Zep when stream finished
        mock_zep_client.memory.add.assert_called_once()
        
        # Check the message that was added
        call_args = mock_zep_client.memory.add.call_args
        messages = call_args[1].get('messages', [])  # From kwargs
        assert len(messages) == 1
        assert messages[0].role == "assistant"
        assert messages[0].content == "".join(mock_stream_chunks)
    
    def test_stream_content_extraction(self, mock_zep_client):
        """Test content extraction from different chunk types."""
        chunks = ["Hello", " ", "world", "!"]
        stream = MockStream(chunks)
        
        wrapper = ZepStreamWrapper(
            stream=stream,
            session_id="test_session",
            zep_client=mock_zep_client,
            extract_content_func=lambda x: x.choices[0].delta.content,
            skip_zep_on_error=True
        )
        
        # Consume the stream
        list(wrapper)
        
        # Should have collected all content
        assert wrapper._collected_content == chunks
    
    def test_stream_content_extraction_with_none_values(self, mock_zep_client):
        """Test content extraction handling None values."""
        chunks = ["Hello", None, "world", "", "!"]
        stream = MockStream(chunks)
        
        wrapper = ZepStreamWrapper(
            stream=stream,
            session_id="test_session",
            zep_client=mock_zep_client,
            extract_content_func=lambda x: x.choices[0].delta.content,
            skip_zep_on_error=True
        )
        
        # Consume the stream
        list(wrapper)
        
        # Should have collected non-None content
        assert wrapper._collected_content == ["Hello", "world", "!"]
        
        # Final content should exclude None and empty values
        mock_zep_client.memory.add.assert_called_once()
        call_args = mock_zep_client.memory.add.call_args
        messages = call_args[1].get('messages', [])
        assert messages[0].content == "Helloworld!"
    
    def test_stream_finalization_empty_content(self, mock_zep_client):
        """Test stream finalization with empty content."""
        stream = MockStream([])
        
        wrapper = ZepStreamWrapper(
            stream=stream,
            session_id="test_session",
            zep_client=mock_zep_client,
            extract_content_func=lambda x: x.choices[0].delta.content,
            skip_zep_on_error=True
        )
        
        # Consume the stream
        list(wrapper)
        
        # Should not add empty content to Zep
        mock_zep_client.memory.add.assert_not_called()
    
    def test_stream_finalization_whitespace_only(self, mock_zep_client):
        """Test stream finalization with whitespace-only content."""
        chunks = [" ", "\t", "\n", ""]
        stream = MockStream(chunks)
        
        wrapper = ZepStreamWrapper(
            stream=stream,
            session_id="test_session",
            zep_client=mock_zep_client,
            extract_content_func=lambda x: x.choices[0].delta.content,
            skip_zep_on_error=True
        )
        
        # Consume the stream
        list(wrapper)
        
        # Should not add whitespace-only content to Zep
        mock_zep_client.memory.add.assert_not_called()
    
    def test_stream_context_manager(self, mock_zep_client, mock_stream_chunks):
        """Test ZepStreamWrapper as context manager."""
        stream = MockStream(mock_stream_chunks)
        
        with ZepStreamWrapper(
            stream=stream,
            session_id="test_session",
            zep_client=mock_zep_client,
            extract_content_func=lambda x: x.choices[0].delta.content,
            skip_zep_on_error=True
        ) as wrapper:
            # Partially consume the stream
            next(wrapper)
            next(wrapper)
        
        # Should still finalize and add content to Zep on exit
        mock_zep_client.memory.add.assert_called_once()
    
    def test_stream_error_handling_skip_true(self, mock_zep_client, mock_stream_chunks):
        """Test error handling with skip_zep_on_error=True."""
        stream = MockStream(mock_stream_chunks)
        
        # Make Zep operation fail
        mock_zep_client.memory.add.side_effect = Exception("Zep error")
        
        wrapper = ZepStreamWrapper(
            stream=stream,
            session_id="test_session",
            zep_client=mock_zep_client,
            extract_content_func=lambda x: x.choices[0].delta.content,
            skip_zep_on_error=True
        )
        
        # Should not raise error
        list(wrapper)
        
        # Should have attempted to add to Zep
        mock_zep_client.memory.add.assert_called_once()
    
    def test_stream_error_handling_skip_false(self, mock_zep_client, mock_stream_chunks):
        """Test error handling with skip_zep_on_error=False."""
        stream = MockStream(mock_stream_chunks)
        
        # Make Zep operation fail
        mock_zep_client.memory.add.side_effect = Exception("Zep error")
        
        wrapper = ZepStreamWrapper(
            stream=stream,
            session_id="test_session",
            zep_client=mock_zep_client,
            extract_content_func=lambda x: x.choices[0].delta.content,
            skip_zep_on_error=False
        )
        
        # Should raise ZepOpenAIError when stream finishes
        from zep_cloud.external_clients.openai_utils import ZepOpenAIError
        
        with pytest.raises(ZepOpenAIError):
            list(wrapper)
    
    def test_stream_content_extraction_error_handling(self, mock_zep_client):
        """Test handling of content extraction errors."""
        chunks = ["Hello", "world"]
        stream = MockStream(chunks)
        
        def failing_extract_func(chunk):
            if chunk.choices[0].delta.content == "world":
                raise AttributeError("Extraction failed")
            return chunk.choices[0].delta.content
        
        wrapper = ZepStreamWrapper(
            stream=stream,
            session_id="test_session",
            zep_client=mock_zep_client,
            extract_content_func=failing_extract_func,
            skip_zep_on_error=True
        )
        
        # Should handle extraction errors gracefully
        list(wrapper)
        
        # Should only collect content that was successfully extracted
        assert wrapper._collected_content == ["Hello"]


class TestAsyncZepStreamWrapper:
    """Test async ZepStreamWrapper functionality."""
    
    @pytest.mark.asyncio
    async def test_async_stream_wrapper_initialization(self, mock_async_zep_client, mock_stream_chunks):
        """Test AsyncZepStreamWrapper initialization."""
        stream = MockAsyncStream(mock_stream_chunks)
        extract_func = lambda x: "test content"
        
        wrapper = AsyncZepStreamWrapper(
            stream=stream,
            session_id="test_session",
            zep_client=mock_async_zep_client,
            extract_content_func=extract_func,
            skip_zep_on_error=True
        )
        
        assert wrapper.stream == stream
        assert wrapper.session_id == "test_session"
        assert wrapper.zep_client == mock_async_zep_client
        assert wrapper.extract_content_func == extract_func
        assert wrapper.skip_zep_on_error is True
        assert wrapper._collected_content == []
    
    @pytest.mark.asyncio
    async def test_async_stream_iteration(self, mock_async_zep_client, mock_stream_chunks):
        """Test async streaming through wrapper with content collection."""
        stream = MockAsyncStream(mock_stream_chunks)
        
        wrapper = AsyncZepStreamWrapper(
            stream=stream,
            session_id="test_session",
            zep_client=mock_async_zep_client,
            extract_content_func=lambda x: x.choices[0].delta.content,
            skip_zep_on_error=True
        )
        
        collected_chunks = []
        collected_content = []
        
        async for chunk in wrapper:
            collected_chunks.append(chunk)
            if hasattr(chunk, 'choices') and chunk.choices[0].delta.content:
                collected_content.append(chunk.choices[0].delta.content)
        
        # Should have iterated through all chunks
        assert len(collected_chunks) == len(mock_stream_chunks)
        assert collected_content == mock_stream_chunks
        
        # Should have added content to Zep when stream finished
        mock_async_zep_client.memory.add.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_async_stream_content_extraction(self, mock_async_zep_client):
        """Test async content extraction from different chunk types."""
        chunks = ["Hello", " ", "world", "!"]
        stream = MockAsyncStream(chunks)
        
        wrapper = AsyncZepStreamWrapper(
            stream=stream,
            session_id="test_session",
            zep_client=mock_async_zep_client,
            extract_content_func=lambda x: x.choices[0].delta.content,
            skip_zep_on_error=True
        )
        
        # Consume the stream
        async for _ in wrapper:
            pass
        
        # Should have collected all content
        assert wrapper._collected_content == chunks
    
    @pytest.mark.asyncio
    async def test_async_stream_finalization_empty_content(self, mock_async_zep_client):
        """Test async stream finalization with empty content."""
        stream = MockAsyncStream([])
        
        wrapper = AsyncZepStreamWrapper(
            stream=stream,
            session_id="test_session",
            zep_client=mock_async_zep_client,
            extract_content_func=lambda x: x.choices[0].delta.content,
            skip_zep_on_error=True
        )
        
        # Consume the stream
        async for _ in wrapper:
            pass
        
        # Should not add empty content to Zep
        mock_async_zep_client.memory.add.assert_not_called()
    
    @pytest.mark.asyncio
    async def test_async_stream_context_manager(self, mock_async_zep_client, mock_stream_chunks):
        """Test AsyncZepStreamWrapper as async context manager."""
        stream = MockAsyncStream(mock_stream_chunks)
        
        async with AsyncZepStreamWrapper(
            stream=stream,
            session_id="test_session",
            zep_client=mock_async_zep_client,
            extract_content_func=lambda x: x.choices[0].delta.content,
            skip_zep_on_error=True
        ) as wrapper:
            # Partially consume the stream
            await wrapper.__anext__()
            await wrapper.__anext__()
        
        # Should still finalize and add content to Zep on exit
        mock_async_zep_client.memory.add.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_async_stream_error_handling_skip_true(self, mock_async_zep_client, mock_stream_chunks):
        """Test async error handling with skip_zep_on_error=True."""
        stream = MockAsyncStream(mock_stream_chunks)
        
        # Make Zep operation fail
        async def mock_add_fail(*args, **kwargs):
            raise Exception("Zep error")
        
        mock_async_zep_client.memory.add = mock_add_fail
        
        wrapper = AsyncZepStreamWrapper(
            stream=stream,
            session_id="test_session",
            zep_client=mock_async_zep_client,
            extract_content_func=lambda x: x.choices[0].delta.content,
            skip_zep_on_error=True
        )
        
        # Should not raise error
        async for _ in wrapper:
            pass
    
    @pytest.mark.asyncio
    async def test_async_stream_error_handling_skip_false(self, mock_async_zep_client, mock_stream_chunks):
        """Test async error handling with skip_zep_on_error=False."""
        stream = MockAsyncStream(mock_stream_chunks)
        
        # Make Zep operation fail
        async def mock_add_fail(*args, **kwargs):
            raise Exception("Zep error")
        
        mock_async_zep_client.memory.add = mock_add_fail
        
        wrapper = AsyncZepStreamWrapper(
            stream=stream,
            session_id="test_session",
            zep_client=mock_async_zep_client,
            extract_content_func=lambda x: x.choices[0].delta.content,
            skip_zep_on_error=False
        )
        
        # Should raise ZepOpenAIError when stream finishes
        from zep_cloud.external_clients.openai_utils import ZepOpenAIError
        
        with pytest.raises(ZepOpenAIError):
            async for _ in wrapper:
                pass


class TestStreamingIntegration:
    """Test streaming integration with OpenAI wrappers."""
    
    def test_chat_completions_streaming_with_zep(self, mock_zep_client):
        """Test chat completions streaming with Zep integration."""
        with patch.dict('sys.modules', {
            'openai': MagicMock(),
            'openai.types.chat': MagicMock(), 
            'openai.types.responses': MagicMock()
        }):
            from zep_cloud.external_clients.openai_client import ChatCompletionsWrapper
            
            mock_openai_completions = MagicMock()
            mock_stream = MockStream(["Hello", " there", "!"])
            mock_openai_completions.create.return_value = mock_stream
            
            wrapper = ChatCompletionsWrapper(mock_openai_completions, mock_zep_client)
            
            # Mock Zep context response
            mock_zep_client.memory.add.return_value = MagicMock(context="Test context")
            
            messages = [
                {"role": "system", "content": "Context: {context}"},
                {"role": "user", "content": "Hello"}
            ]
            
            # Request streaming
            result = wrapper.create(
                model="gpt-4.1-mini",
                messages=messages,
                session_id="test_session",
                stream=True
            )
            
            # Should return ZepStreamWrapper
            assert isinstance(result, ZepStreamWrapper)
            
            # Consume the stream
            collected = list(result)
            
            # Should have processed all chunks
            assert len(collected) == 3
            
            # Should have added final content to Zep
            assert mock_zep_client.memory.add.call_count == 2  # Context + final response
    
    @pytest.mark.asyncio
    async def test_async_chat_completions_streaming_with_zep(self, mock_async_zep_client):
        """Test async chat completions streaming with Zep integration."""
        with patch.dict('sys.modules', {
            'openai': MagicMock(),
            'openai.types.chat': MagicMock(), 
            'openai.types.responses': MagicMock()
        }):
            from zep_cloud.external_clients.openai_async import AsyncChatCompletionsWrapper
            
            mock_openai_completions = MagicMock()
            mock_stream = MockAsyncStream(["Hello", " there", "!"])
            
            async def mock_create(*args, **kwargs):
                if kwargs.get('stream'):
                    return mock_stream
                return MagicMock()
            
            mock_openai_completions.create = mock_create
            
            wrapper = AsyncChatCompletionsWrapper(mock_openai_completions, mock_async_zep_client)
            
            # Mock Zep context response
            async def mock_add(*args, **kwargs):
                mock_response = MagicMock()
                mock_response.context = "Test context"
                return mock_response
            
            mock_async_zep_client.memory.add = mock_add
            
            messages = [
                {"role": "system", "content": "Context: {context}"},
                {"role": "user", "content": "Hello"}
            ]
            
            # Request streaming
            result = await wrapper.create(
                model="gpt-4.1-mini",
                messages=messages,
                session_id="test_session",
                stream=True
            )
            
            # Should return AsyncZepStreamWrapper
            assert isinstance(result, AsyncZepStreamWrapper)
            
            # Consume the stream
            collected = []
            async for chunk in result:
                collected.append(chunk)
            
            # Should have processed all chunks
            assert len(collected) == 3
    
    def test_streaming_without_session_id(self, mock_zep_client):
        """Test streaming without session_id (pure OpenAI passthrough)."""
        with patch.dict('sys.modules', {
            'openai': MagicMock(),
            'openai.types.chat': MagicMock(), 
            'openai.types.responses': MagicMock()
        }):
            from zep_cloud.external_clients.openai_client import ChatCompletionsWrapper
            
            mock_openai_completions = MagicMock()
            mock_stream = MockStream(["Hello", " world"])
            mock_openai_completions.create.return_value = mock_stream
            
            wrapper = ChatCompletionsWrapper(mock_openai_completions, mock_zep_client)
            
            messages = [{"role": "user", "content": "Hello"}]
            
            # Request streaming without session_id
            result = wrapper.create(
                model="gpt-4.1-mini",
                messages=messages,
                stream=True
            )
            
            # Should return raw OpenAI stream, not wrapped
            assert result == mock_stream
            
            # Should not call Zep
            mock_zep_client.memory.add.assert_not_called()
            mock_zep_client.memory.get.assert_not_called()


class TestStreamingEdgeCases:
    """Test streaming edge cases and error conditions."""
    
    def test_stream_with_malformed_chunks(self, mock_zep_client):
        """Test streaming with malformed chunks."""
        # Create malformed chunks
        malformed_chunks = ["valid", None, ""]
        stream = MockStream(malformed_chunks)
        
        wrapper = ZepStreamWrapper(
            stream=stream,
            session_id="test_session",
            zep_client=mock_zep_client,
            extract_content_func=lambda x: x.choices[0].delta.content if x.choices else None,
            skip_zep_on_error=True
        )
        
        # Should handle malformed chunks gracefully
        list(wrapper)
        
        # Should only collect valid content
        assert "valid" in wrapper._collected_content
    
    def test_stream_extraction_function_none_return(self, mock_zep_client, mock_stream_chunks):
        """Test streaming with extraction function that returns None."""
        stream = MockStream(mock_stream_chunks)
        
        wrapper = ZepStreamWrapper(
            stream=stream,
            session_id="test_session",
            zep_client=mock_zep_client,
            extract_content_func=lambda x: None,  # Always returns None
            skip_zep_on_error=True
        )
        
        # Consume the stream
        list(wrapper)
        
        # Should not add anything to Zep since no content was extracted
        mock_zep_client.memory.add.assert_not_called()
    
    def test_stream_large_content_collection(self, mock_zep_client):
        """Test streaming with large content collection."""
        # Create many small chunks
        large_chunks = [f"chunk{i}" for i in range(1000)]
        stream = MockStream(large_chunks)
        
        wrapper = ZepStreamWrapper(
            stream=stream,
            session_id="test_session",
            zep_client=mock_zep_client,
            extract_content_func=lambda x: x.choices[0].delta.content,
            skip_zep_on_error=True
        )
        
        # Should handle large streams
        list(wrapper)
        
        # Should collect all content
        assert len(wrapper._collected_content) == 1000
        
        # Should add complete content to Zep
        mock_zep_client.memory.add.assert_called_once()
        call_args = mock_zep_client.memory.add.call_args
        messages = call_args[1].get('messages', [])
        expected_content = "".join(large_chunks)
        assert messages[0].content == expected_content