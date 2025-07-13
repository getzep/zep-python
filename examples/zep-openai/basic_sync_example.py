#!/usr/bin/env python3
"""
Basic Sync ZepOpenAI Example

This example demonstrates how to use the ZepOpenAI wrapper as a drop-in replacement
for the OpenAI client with automatic memory integration.
"""

import os
from dotenv import load_dotenv
from zep_cloud import Zep
from zep_cloud.external_clients import ZepOpenAI

# Load environment variables
load_dotenv()

def main():
    # Initialize Zep client
    zep_client = Zep(api_key=os.getenv("ZEP_API_KEY"))
    
    # Initialize ZepOpenAI client (drop-in replacement for OpenAI)
    client = ZepOpenAI(
        zep_client=zep_client,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    print("🤖 Basic ZepOpenAI Example")
    print("=" * 40)
    
    # Example 1: Regular OpenAI call (no memory integration)
    print("\n1. Regular OpenAI call (no session_id):")
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": "Hello! What's 2+2?"}
        ]
    )
    print(f"Assistant: {response.choices[0].message.content}")
    
    # Example 2: With Zep memory integration
    session_id = "demo-session-basic"
    print(f"\n2. With Zep memory integration (session: {session_id}):")
    
    # First message with context placeholder
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Context: {context}"},
            {"role": "user", "content": "My name is Alice and I love pizza."}
        ],
        session_id=session_id
    )
    print(f"Assistant: {response.choices[0].message.content}")
    
    # Second message - Zep should remember previous conversation
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Context: {context}"},
            {"role": "user", "content": "What's my name and what do I like?"}
        ],
        session_id=session_id
    )
    print(f"Assistant: {response.choices[0].message.content}")
    
    # Example 3: Custom context placeholder
    print(f"\n3. Custom context placeholder:")
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are helpful. Memory: {{memory}} Use this info."},
            {"role": "user", "content": "What do you remember about me?"}
        ],
        session_id=session_id,
        context_placeholder="{{memory}}"
    )
    print(f"Assistant: {response.choices[0].message.content}")
    
    # Example 4: Error handling
    print(f"\n4. Error handling with skip_zep_on_error:")
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": "This works even if Zep has issues"}
            ],
            session_id="invalid-session",
            skip_zep_on_error=True  # Continue even if Zep fails
        )
        print(f"Assistant: {response.choices[0].message.content}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n✅ Example completed!")
    print("\nKey features demonstrated:")
    print("- Drop-in replacement for OpenAI client")
    print("- Automatic memory integration with session_id")
    print("- Context injection with placeholders")
    print("- Custom context placeholders")
    print("- Error handling options")

if __name__ == "__main__":
    main()