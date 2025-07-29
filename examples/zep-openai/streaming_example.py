#!/usr/bin/env python3
"""
Streaming ZepOpenAI Example

This example demonstrates how to use streaming with the ZepOpenAI wrapper,
showing both sync and async streaming with automatic memory integration.
"""
import uuid

import asyncio
import os

from dotenv import load_dotenv
from zep_cloud import AsyncZep, Zep
from zep_cloud.openai import AsyncZepOpenAI, ZepOpenAI

# Load environment variables
load_dotenv()


def sync_streaming_example():
    """Demonstrate sync streaming with ZepOpenAI."""
    print("🌊 Sync Streaming Example")
    print("=" * 40)

    # Initialize clients
    zep_client = Zep(api_key=os.getenv("ZEP_API_KEY"))
    client = ZepOpenAI(zep_client=zep_client, api_key=os.getenv("OPENAI_API_KEY"))


    user_id = "user-streaming-demo" + uuid.uuid4().hex
    # Create zep user
    zep_client.user.add(
        user_id=user_id,
        first_name="John",
        last_name="Doe",
        email="john@example.com",
    )

    thread_id = "streaming-demo-sync" + uuid.uuid4().hex
    # Create the thread for the user
    zep_client.thread.create(user_id=user_id, thread_id=thread_id)

    # Example 1: Basic streaming without Zep
    print("\n1. Basic streaming (no memory):")
    stream = client.chat.completions.create(
        model="gpt-4.1-mini", messages=[{"role": "user", "content": "Tell me a short story about a robot"}], stream=True
    )

    print("Story: ", end="", flush=True)
    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print("\n")

    # Example 2: Streaming with Zep memory integration
    print(f"\n2. Streaming with memory (thread: {thread_id}):")
    stream = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a creative writer. Context: {context}"},
            {"role": "user", "content": "My favorite genre is science fiction."},
        ],
        thread_id=thread_id,
        stream=True,
    )

    print("Response: ", end="", flush=True)
    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print("\n")

    # Example 3: Continue the conversation with streaming
    print("\n3. Continue conversation with streaming:")
    stream = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a creative writer. Context: {context}"},
            {"role": "user", "content": "Write a short sci-fi story for me."},
        ],
        thread_id=thread_id,
        stream=True,
    )

    print("Sci-fi story: ", end="", flush=True)
    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print("\n")


async def async_streaming_example():
    """Demonstrate async streaming with AsyncZepOpenAI."""
    print("\n🚀 Async Streaming Example")
    print("=" * 40)

    # Initialize async clients
    zep_client = AsyncZep(api_key=os.getenv("ZEP_API_KEY"))
    client = AsyncZepOpenAI(zep_client=zep_client, api_key=os.getenv("OPENAI_API_KEY"))

    thread_id = "streaming-demo-async"

    # Example 1: Basic async streaming
    print("\n1. Async streaming without memory:")
    stream = await client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": "Explain quantum computing in simple terms"}],
        stream=True,
    )

    print("Explanation: ", end="", flush=True)
    async for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print("\n")

    # Example 2: Async streaming with memory
    print(f"\n2. Async streaming with memory (thread: {thread_id}):")
    stream = await client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a tech expert. Context: {context}"},
            {"role": "user", "content": "I'm interested in learning about AI and machine learning."},
        ],
        thread_id=thread_id,
        stream=True,
    )

    print("Response: ", end="", flush=True)
    async for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print("\n")

    # Example 3: Follow-up question with context
    print("\n3. Follow-up with remembered context:")
    stream = await client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a tech expert. Context: {context}"},
            {"role": "user", "content": "What should I start learning first?"},
        ],
        thread_id=thread_id,
        stream=True,
    )

    print("Recommendation: ", end="", flush=True)
    async for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
    print("\n")


def streaming_with_context_manager():
    """Demonstrate streaming with context manager for automatic cleanup."""
    print("\n🔧 Streaming with Context Manager")
    print("=" * 40)

    zep_client = Zep(api_key=os.getenv("ZEP_API_KEY"))
    client = ZepOpenAI(zep_client=zep_client, api_key=os.getenv("OPENAI_API_KEY"))

    thread_id = "context-manager-demo"

    # Using context manager ensures proper cleanup
    with client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are helpful. Context: {context}"},
            {"role": "user", "content": "Tell me about context managers in Python"},
        ],
        thread_id=thread_id,
        stream=True,
    ) as stream:
        print("Context manager explanation: ", end="", flush=True)
        for chunk in stream:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)

    print("\n✅ Stream automatically cleaned up!")


async def async_streaming_with_context_manager():
    """Demonstrate async streaming with context manager for automatic cleanup."""
    print("\n🔧 Async Streaming with Context Manager")
    print("=" * 40)

    zep_client = AsyncZep(api_key=os.getenv("ZEP_API_KEY"))
    client = AsyncZepOpenAI(zep_client=zep_client, api_key=os.getenv("OPENAI_API_KEY"))

    thread_id = "async-context-manager-demo"

    # Using async context manager ensures proper cleanup
    async with await client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are helpful. Context: {context}"},
            {"role": "user", "content": "Tell me about async context managers in Python"},
        ],
        thread_id=thread_id,
        stream=True,
    ) as stream:
        print("Async context manager explanation: ", end="", flush=True)
        async for chunk in stream:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)

    print("\n✅ Async stream automatically cleaned up!")


async def main():
    """Run all streaming examples."""
    print("🌊 ZepOpenAI Streaming Examples")
    print("=" * 50)

    # Run sync streaming examples
    sync_streaming_example()

    # Run async streaming examples
    await async_streaming_example()

    # Run context manager example
    streaming_with_context_manager()

    # Run async context manager example
    await async_streaming_with_context_manager()

    print("\n✅ All streaming examples completed!")
    print("\nKey streaming features demonstrated:")
    print("- Sync and async streaming")
    print("- Automatic content collection during streaming")
    print("- Memory integration with streaming responses")
    print("- Context manager support for cleanup (sync and async)")
    print("- Conversation continuity across streaming calls")
    print("\nNote: Streamed content is automatically added to Zep memory")
    print("      when the stream completes, enabling conversation continuity.")


if __name__ == "__main__":
    asyncio.run(main())
