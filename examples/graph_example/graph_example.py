"""
Example of using the Zep Python SDK asynchronously.

This script demonstrates the following functionality:
- Creating a user.
- Creating a session associated with the created user.
- Adding messages to the session.
- Searching the session memory for a specific query.
- Searching the session memory with MMR reranking.
- Searching the session memory with a metadata filter.
- optionally deleting the session.
"""

import asyncio
import os
import uuid

from dotenv import find_dotenv, load_dotenv
from conversations import history

from zep_cloud.client import AsyncZep
from zep_cloud.types import Message

load_dotenv(
    dotenv_path=find_dotenv()
)  # load environment variables from .env file, if present

API_KEY = os.environ.get("ZEP_API_KEY") or "YOUR_API_KEY"


async def main() -> None:
    client = AsyncZep(
        api_key=API_KEY,
    )
    user_id = uuid.uuid4().hex
    session_id = uuid.uuid4().hex
    await client.user.add(user_id=user_id, first_name="Paul")
    print(f"User {user_id} created")
    await client.memory.add_session(session_id=session_id, user_id=user_id)
    print(f"Session {session_id} created")
    for message in history[1]:
        await client.memory.add(
            session_id,
            messages=[
                Message(
                    role=message["role"],
                    role_type=message["role_type"],
                    content=message["content"],
                )
            ],
        )

    episode_result = await client.graph.episode.get_by_user_id(user_id, lastn=3)
    episodes = episode_result.episodes
    print(f"Episodes for user {user_id}:")
    print(episodes)
    episode = await client.graph.episode.get_by_uuid(episodes[0].uuid_)
    print(episode)

    edges = await client.graph.edge.get_by_user_id(user_id)
    print(f"Edges for user {user_id}:")
    print(edges)
    edge = await client.graph.edge.get_by_uuid(edges[0].uuid_)
    print(edge)

    nodes = await client.graph.node.get_by_user_id(user_id)
    print(f"Nodes for user {user_id}:")
    print(nodes)
    node = await client.graph.node.get_by_uuid(nodes[0].uuid_)
    print(node)

    print("Searching user graph memory...")
    search_results = await client.graph.search(
        user_id=user_id,
        query="What is the weather in San Francisco?",
    )
    print(search_results.edges)

    print("Adding a new text episode to the graph...")
    await client.graph.add(
        user_id=user_id,
        text="The user is an avid fan of Eric Clapton",
    )
    print("Text episode added")
    print("Adding a new JSON episode to the graph...")
    json_string = '{"name": "Eric Clapton", "age": 78, "genre": "Rock"}'
    await client.graph.add(
        user_id=user_id,
        json=json_string,
    )
    print("JSON episode added")

    print("Waiting for the graph to be updated...")
    # wait for the graph to be updated
    await asyncio.sleep(15)

    print("Getting nodes from the graph...")
    nodes = await client.graph.node.get_by_user_id(user_id)
    print(nodes)

    print("Finding Eric Clapton in the graph...")
    clapton_node = [node for node in nodes if node.name == "Eric Clapton"]
    print(clapton_node)

    print("Performing Eric Clapton centered search...")
    search_results = await client.graph.search(
        user_id=user_id,
        query="Eric Clapton",
        center_node_uuid=clapton_node[0].uuid_,
    )
    print(search_results.edges)


if __name__ == "__main__":
    asyncio.run(main())
