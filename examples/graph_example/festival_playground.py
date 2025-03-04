"""
Example of using Zep Graph API to create a music festival planning scenario.
This playground demonstrates mixing message and JSON episodes to build
a rich knowledge graph that users can explore and extend.
"""

import asyncio
import os
import uuid
import json
from dotenv import find_dotenv, load_dotenv

from zep_cloud.client import AsyncZep
from zep_cloud.types import Message

load_dotenv(dotenv_path=find_dotenv())

API_KEY = os.environ.get("ZEP_API_KEY") or "YOUR_API_KEY"

# Sample festival data episodes
FESTIVAL_EPISODES = [
    {
        "type": "json",
        "data": {
            "event_name": "SoundWave Festival 2024",
            "dates": "July 15-17, 2024",
            "venue": "Oceanside Park",
            "capacity": 50000,
            "ticket_tiers": [
                {"type": "Early Bird", "price": 299},
                {"type": "Regular", "price": 399},
                {"type": "VIP", "price": 799}
            ]
        }
    },
    {
        "type": "message",
        "data": "Organizer: We're excited to announce that Arctic Monkeys will be headlining the main stage on July 15th!"
    },
    {
        "type": "json",
        "data": {
            "artist": "Arctic Monkeys",
            "performance_details": {
                "date": "July 15, 2024",
                "stage": "Main Stage",
                "set_time": "21:00-23:00",
                "genre": ["Alternative Rock", "Indie Rock"],
                "rider_requirements": {
                    "technical": "Full band setup",
                    "backstage": "Private green room"
                }
            }
        }
    },
    {
        "type": "message",
        "data": "Attendee: Will there be food vendors at the festival? I have dietary restrictions."
    },
    {
        "type": "json",
        "data": {
            "vendors": {
                "food_courts": [
                    {
                        "name": "Global Eats Plaza",
                        "vendors": ["VeganDelight", "Mediterranean Fresh", "Sushi Station"],
                        "dietary_options": ["Vegan", "Gluten-Free", "Halal"]
                    },
                    {
                        "name": "Street Food Market",
                        "vendors": ["Taco Truck", "Pizza Paradise", "BBQ Pit"],
                        "dietary_options": ["Vegetarian", "Dairy-Free"]
                    }
                ]
            }
        }
    },
    {
        "type": "message",
        "data": "Staff: We've just confirmed Taylor Swift for July 16th! This will be her only festival appearance this summer."
    },
    {
        "type": "json",
        "data": {
            "artist": "Taylor Swift",
            "performance_details": {
                "date": "July 16, 2024",
                "stage": "Main Stage",
                "set_time": "21:00-23:30",
                "genre": ["Pop", "Country Pop"],
                "special_effects": ["Pyrotechnics", "LED Screens"],
                "expected_attendance": 45000
            }
        }
    }
]

async def create_festival_playground() -> None:
    client = AsyncZep(api_key=API_KEY)
    
    # Create a user for the playground
    user_id = uuid.uuid4().hex
    await client.user.add(user_id=user_id, first_name="Festival_Admin")
    print(f"Created playground user: {user_id}")

    # Add all episodes to the graph
    for episode in FESTIVAL_EPISODES:
        if episode["type"] == "json":
            await client.graph.add(
                user_id=user_id,
                type="json",
                data=json.dumps(episode["data"])
            )
        else:  # message type
            await client.graph.add(
                user_id=user_id,
                type="message",
                data=episode["data"]
            )
    
    print("Added all festival episodes to the graph")
    print("Waiting for graph processing...")
    await asyncio.sleep(30)
    
    # Get all nodes to verify the graph
    nodes = await client.graph.node.get_by_user_id(user_id)
    print("\nCreated nodes:")
    for node in nodes:
        print(f"- {node.name} ({node.type})")
    
    return user_id

if __name__ == "__main__":
    user_id = asyncio.run(create_festival_playground())
    print(f"\nPlayground ready! User ID: {user_id}")
    print("You can now explore the festival graph and add new episodes!") 