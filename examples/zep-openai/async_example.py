#!/usr/bin/env python3
"""
Async ZepOpenAI Example

This example demonstrates how to use the AsyncZepOpenAI wrapper for asynchronous
operations with automatic memory integration.
"""
import uuid

import asyncio
import os

from dotenv import load_dotenv
from zep_cloud import AsyncZep
from zep_cloud.openai import AsyncZepOpenAI

# Load environment variables
load_dotenv()


async def main():
    # Initialize async Zep client
    zep_client = AsyncZep(api_key=os.getenv("ZEP_API_KEY"))

    # Initialize AsyncZepOpenAI client
    client = AsyncZepOpenAI(zep_client=zep_client, api_key=os.getenv("OPENAI_API_KEY"))

    print("🚀 Async ZepOpenAI Example")
    print("=" * 40)

    # Example 1: Basic async call
    print("\n1. Basic async call:")
    response = await client.chat.completions.create(
        model="gpt-4.1-mini", messages=[{"role": "user", "content": "Hello! Tell me a short joke."}]
    )
    print(f"Assistant: {response.choices[0].message.content}")

    user_id = "user-async-demo" + uuid.uuid4().hex
    # Create zep user
    await zep_client.user.add(
        user_id=user_id,
        first_name="John",
        last_name="Doe",
        email="john@example.com",
    )

    thread_id = "demo-thread-async" + uuid.uuid4().hex
    # Create the thread for the user
    await zep_client.thread.create(user_id=user_id, thread_id=thread_id)

    # Example 2: Async with memory integration
    print(f"\n2. Async with memory (thread: {thread_id}):")

    # Set up a conversation
    response = await client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a travel assistant. Context: {context}"},
            {"role": "user", "content": "I'm planning a trip to Japan in spring."},
        ],
        thread_id=thread_id,
    )
    print(f"Assistant: {response.choices[0].message.content}")

    # Continue the conversation
    response = await client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a travel assistant. Context: {context}"},
            {"role": "user", "content": "What should I pack for this trip?"},
        ],
        thread_id=thread_id,
    )
    print(f"Assistant: {response.choices[0].message.content}")

    # Example 3: Async with Responses API
    print("\n4. Async Responses API:")
    try:
        response = await client.responses.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Context: {context}"},
                {"role": "user", "content": "Write a haiku about coding"},
            ],
            thread_id="haiku-thread",
        )
        print(f"Haiku response: {response}")
    except Exception as e:
        print(f"Note: Responses API might not be available: {e}")

    # Example 4: Error handling in async context
    print("\n5. Async error handling:")
    try:
        response = await client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": "This should work fine"}],
            thread_id="error-test-thread" + uuid.uuid4().hex,
            skip_zep_on_error=True,
        )
        print(f"Assistant: {response.choices[0].message.content}")
    except Exception as e:
        print(f"Error handled gracefully: {e}")

    print("\n✅ Async example completed!")
    print("\nKey async features demonstrated:")
    print("- Async/await support for all operations")
    print("- Concurrent request handling")
    print("- Async memory integration")
    print("- Both Chat Completions and Responses APIs")
    print("- Async error handling")


if __name__ == "__main__":
    asyncio.run(main())
