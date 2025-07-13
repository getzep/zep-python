#!/usr/bin/env python3
"""
Async ZepOpenAI Example

This example demonstrates how to use the AsyncZepOpenAI wrapper for asynchronous
operations with automatic memory integration.
"""

import asyncio
import os
from dotenv import load_dotenv
from zep_cloud import AsyncZep
from zep_cloud.external_clients import AsyncZepOpenAI

# Load environment variables
load_dotenv()

async def main():
    # Initialize async Zep client
    zep_client = AsyncZep(api_key=os.getenv("ZEP_API_KEY"))
    
    # Initialize AsyncZepOpenAI client
    client = AsyncZepOpenAI(
        zep_client=zep_client,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    print("🚀 Async ZepOpenAI Example")
    print("=" * 40)
    
    # Example 1: Basic async call
    print("\n1. Basic async call:")
    response = await client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": "Hello! Tell me a short joke."}
        ]
    )
    print(f"Assistant: {response.choices[0].message.content}")
    
    # Example 2: Async with memory integration
    session_id = "demo-session-async"
    print(f"\n2. Async with memory (session: {session_id}):")
    
    # Set up a conversation
    response = await client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a travel assistant. Context: {context}"},
            {"role": "user", "content": "I'm planning a trip to Japan in spring."}
        ],
        session_id=session_id
    )
    print(f"Assistant: {response.choices[0].message.content}")
    
    # Continue the conversation
    response = await client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a travel assistant. Context: {context}"},
            {"role": "user", "content": "What should I pack for this trip?"}
        ],
        session_id=session_id
    )
    print(f"Assistant: {response.choices[0].message.content}")
    
    # Example 3: Multiple concurrent requests
    print(f"\n3. Concurrent async requests:")
    
    async def ask_question(question: str, session: str):
        response = await client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are helpful. Context: {context}"},
                {"role": "user", "content": question}
            ],
            session_id=session
        )
        return f"Q: {question}\nA: {response.choices[0].message.content}"
    
    # Run multiple requests concurrently
    tasks = [
        ask_question("What's the capital of France?", "session-1"),
        ask_question("What's 10 * 15?", "session-2"),
        ask_question("Name a programming language", "session-3")
    ]
    
    results = await asyncio.gather(*tasks)
    for result in results:
        print(f"\n{result}")
    
    # Example 4: Async with Responses API
    print(f"\n4. Async Responses API:")
    try:
        response = await client.responses.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "Context: {context}"},
                {"role": "user", "content": "Write a haiku about coding"}
            ],
            session_id="haiku-session"
        )
        print(f"Haiku response: {response}")
    except Exception as e:
        print(f"Note: Responses API might not be available: {e}")
    
    # Example 5: Error handling in async context
    print(f"\n5. Async error handling:")
    try:
        response = await client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": "This should work fine"}
            ],
            session_id="error-test-session",
            skip_zep_on_error=True
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