"""
Example of using the Zep Python SDK asynchronously with Graph functionality.

This script demonstrates the following functionality:
- Creating a group.
- Updating a group.
- Adding episodes to the group (text and JSON).
- Retrieving nodes from the group.
- Retrieving edges from the group.
- Searching the group for specific content.

The script showcases various operations using the Zep Graph API, including
group management, adding different types of episodes, and querying the graph structure.
"""

import asyncio
import os
import uuid

from dotenv import find_dotenv, load_dotenv

from zep_cloud.client import AsyncZep

load_dotenv(
    dotenv_path=find_dotenv()
)  # load environment variables from .env file, if present

API_KEY = os.environ.get("ZEP_API_KEY") or "YOUR_API_KEY"


async def main() -> None:
    client = AsyncZep(
        api_key=API_KEY,
    )

    group_id = uuid.uuid4().hex
    print(f"Creating group {group_id}...")
    group = await client.group.add(
        group_id=group_id,
        name="My Group",
        description="This is my group",
    )
    print(f"Group {group_id} created {group}")

    print(f"Adding episode to group {group_id}...")
    await client.graph.add(
        group_id=group_id,
        data="This is a test episode",
        type="text",
    )

    print(f"Adding more meaningful episode to group {group_id}...")
    await client.graph.add(
        group_id=group_id,
        data="Eric Clapton is a rock star",
        type="text",
    )

    print(f"Adding a JSON episode to group {group_id}...")
    json_string = '{"name": "Eric Clapton", "age": 78, "genre": "Rock"}'
    await client.graph.add(
        group_id=group_id,
        data=json_string,
        type="json",
    )
    await asyncio.sleep(20)

    # TODO: Need to enable non-message episodic content retrieval
    print(f"Getting episodes from group {group_id}...")
    results = await client.graph.episode.get_by_group_id(group_id, lastn=2)
    print(f"Episodes from group {group_id} {results.episodes}")
    episode = await client.graph.episode.get(results.episodes[0].uuid_)
    print(f"Episode {episode.uuid_} from group {group_id} {episode}")

    print(f"Getting nodes from group {group_id}...")
    nodes = await client.graph.node.get_by_group_id(group_id)
    print(f"Nodes from group {group_id} {nodes}")

    print(f"Getting edges from group {group_id}...")
    edges = await client.graph.edge.get_by_group_id(group_id)
    print(f"Edges from group {group_id} {edges}")

    print(f"Searching group {group_id}...")
    search_results = await client.graph.search(
        group_id=group_id,
        query="Eric Clapton",
    )
    print(f"Search results from group {group_id} {search_results}")

    await client.group.delete(group_id)
    print(f"Group {group_id} deleted")


if __name__ == "__main__":
    asyncio.run(main())
