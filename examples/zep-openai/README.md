# ZepOpenAI Examples

This directory contains examples demonstrating how to use the ZepOpenAI wrapper as a drop-in replacement for the OpenAI client with automatic memory integration.

## Overview

The ZepOpenAI wrapper allows you to:
- Use the exact same API as the OpenAI client
- Automatically store conversations in Zep memory when you provide a `session_id`
- Inject conversation context into your prompts using placeholders
- Handle errors gracefully with `skip_zep_on_error`
- Support both sync and async operations
- Stream responses while maintaining memory integration

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables:**
   Create a `.env` file with your API keys:
   ```
   ZEP_API_KEY=your_zep_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Examples

### 1. Basic Sync Example (`basic_sync_example.py`)

Demonstrates the fundamental usage of ZepOpenAI:
- Regular OpenAI calls (no memory)
- Memory integration with `session_id`
- Custom context placeholders
- Error handling with `skip_zep_on_error`

**Run:**
```bash
python basic_sync_example.py
```

**Key Features:**
- Drop-in replacement for OpenAI client
- Automatic memory integration
- Context injection with `{context}` placeholder
- Custom placeholder support

### 2. Async Example (`async_example.py`)

Shows asynchronous operations with AsyncZepOpenAI:
- Basic async calls
- Memory integration in async context
- Concurrent request handling
- Async error handling

**Run:**
```bash
python async_example.py
```

**Key Features:**
- Full async/await support
- Concurrent request processing
- Async memory integration
- Both Chat Completions and Responses APIs

### 3. Streaming Example (`streaming_example.py`)

Demonstrates streaming capabilities:
- Sync and async streaming
- Memory integration with streamed content
- Context manager support
- Automatic content collection

**Run:**
```bash
python streaming_example.py
```

**Key Features:**
- Real-time streaming responses
- Automatic memory storage of streamed content
- Context manager for cleanup
- Conversation continuity across streams

## Key Concepts

### Memory Integration

When you provide a `session_id`, the wrapper automatically:
1. Stores your messages in Zep memory
2. Retrieves relevant context from previous conversations
3. Injects context into prompts using placeholders

### Context Placeholders

Use `{context}` in your prompts to inject conversation context:
```python
messages = [
    {"role": "system", "content": "You are helpful. Context: {context}"},
    {"role": "user", "content": "What did we discuss before?"}
]
```

You can also use custom placeholders:
```python
client.chat.completions.create(
    messages=[
        {"role": "system", "content": "Memory: {{memory}} Use this info."}
    ],
    session_id="my-session",
    context_placeholder="{{memory}}"
)
```

### Error Handling

Use `skip_zep_on_error=True` to continue even if Zep fails:
```python
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": "Hello"}],
    session_id="my-session",
    skip_zep_on_error=True  # Fallback to regular OpenAI if Zep fails
)
```

### Streaming with Memory

Streamed content is automatically collected and stored in memory when the stream completes:
```python
stream = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages,
    session_id="my-session",
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
# Content automatically added to memory after stream ends
```

## Common Patterns

### Simple Drop-in Replacement
```python
# Replace this:
# client = OpenAI(api_key="...")

# With this:
zep_client = Zep(api_key="...")
client = ZepOpenAI(zep_client=zep_client, api_key="...")

# Use exactly the same API
response = client.chat.completions.create(...)
```

### Memory-Enabled Conversations
```python
# Add session_id to enable memory
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "Context: {context}"},
        {"role": "user", "content": "Remember this: I love pizza"}
    ],
    session_id="user-123"
)

# Later in the conversation...
response = client.chat.completions.create(
    model="gpt-4.1-mini", 
    messages=[
        {"role": "system", "content": "Context: {context}"},
        {"role": "user", "content": "What do I love?"}
    ],
    session_id="user-123"  # Same session remembers previous context
)
```

## Notes

- The wrapper is fully compatible with the OpenAI Python client API
- Memory integration only occurs when `session_id` is provided
- Context injection requires placeholders in your prompt templates
- Streaming responses are automatically stored in memory after completion
- Error handling ensures graceful fallback to standard OpenAI behavior

## Troubleshooting

1. **Missing API keys**: Ensure both `ZEP_API_KEY` and `OPENAI_API_KEY` are set
2. **Memory not working**: Check that you're providing a `session_id` and using `{context}` placeholder
3. **Import errors**: Install all dependencies with `pip install -r requirements.txt`
4. **Streaming issues**: Ensure you're iterating through the entire stream for memory storage to occur