#!/usr/bin/env python3
"""
Basic Sync ZepOpenAI Example

This example demonstrates how to use the ZepOpenAI wrapper as a drop-in replacement
for the OpenAI client with automatic memory integration.
"""

import os
import time
import uuid

from dotenv import load_dotenv
from zep_cloud import Zep
from zep_cloud.openai import ZepOpenAI

# Load environment variables
load_dotenv()


def main():
    # Initialize Zep client
    zep_client = Zep(api_key=os.getenv("ZEP_API_KEY"))

    # Initialize ZepOpenAI client (drop-in replacement for OpenAI)
    client = ZepOpenAI(zep_client=zep_client, api_key=os.getenv("OPENAI_API_KEY"))

    print("🤖 Basic ZepOpenAI Example")
    print("=" * 40)

    # Example 1: Regular OpenAI call (no memory integration)
    print("\n1. Regular OpenAI call (no thread_id):")
    response = client.chat.completions.create(
        model="gpt-4.1-mini", messages=[{"role": "user", "content": "Hello! What's 2+2?"}]
    )
    print(f"Assistant: {response.choices[0].message.content}")

    user_id = "user-streaming-demo" + uuid.uuid4().hex
    # Create zep user
    zep_client.user.add(
        user_id=user_id,
        first_name="Alice",
        email="alice@example.com",
    )

    thread_id = "demo-thread-basic" + uuid.uuid4().hex
    # Create the thread for the user
    zep_client.thread.create(user_id=user_id, thread_id=thread_id)


    # Example 2: With Zep memory integration
    print(f"\n2. With Zep memory integration (thread: {thread_id}):")

    # First message with context placeholder
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Context: {context}"},
            {"role": "user", "content": "My name is Alice and I love pizza."},
        ],
        thread_id=thread_id,
    )
    print(f"Assistant: {response.choices[0].message.content}")
    time.sleep(20)  # Wait for Zep to process the memory

    # Second message - Zep should remember previous conversation
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Context: {context}"},
            {"role": "user", "content": "What's my name and what do I like?"},
        ],
        thread_id=thread_id,
    )
    print(f"Assistant: {response.choices[0].message.content}")

    # Example 3: Custom context placeholder
    print("\n3. Custom context placeholder:")
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are helpful. Memory: {{memory}} Use this info."},
            {"role": "user", "content": "What do you remember about me?"},
        ],
        thread_id=thread_id,
        context_placeholder="{{memory}}",
    )
    print(f"Assistant: {response.choices[0].message.content}")

    # Example 4: Error handling
    print("\n4. Error handling with skip_zep_on_error:")
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": "This works even if Zep has issues"}],
            thread_id="invalid-thread" + uuid.uuid4().hex,  # Invalid thread to trigger error
            skip_zep_on_error=True,  # Continue even if Zep fails
        )
        print(f"Assistant: {response.choices[0].message.content}")
    except Exception as e:
        print(f"Error: {e}")

    print("\n✅ Example completed!")
    print("\nKey features demonstrated:")
    print("- Drop-in replacement for OpenAI client")
    print("- Automatic memory integration with thread_id")
    print("- Context injection with placeholders")
    print("- Custom context placeholders")
    print("- Error handling options")


if __name__ == "__main__":
    main()
