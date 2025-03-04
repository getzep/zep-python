"""
Example of using Zep Graph API to create an AI wellness companion scenario.
This playground demonstrates user interactions with a wellness assistant,
mixing health tracking data, coaching conversations, and personalized recommendations.
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

async def create_wellness_playground() -> None:
    client = AsyncZep(api_key=API_KEY)
    
    # Create a user for the playground
    user_id = uuid.uuid4().hex
    await client.user.add(user_id=user_id, first_name="Alex", last_name="Chen", email="alex.chen@example.com")
    print(f"Created playground user: {user_id}")

    # Sample user interactions and system events
    episodes = [
        {
            "type": "message",
            "data": "Alex (user): I've been feeling really stressed lately and having trouble sleeping."
        },
        {
            "type": "json",
            "data": {
                "event_type": "daily_tracking",
                "user_email": "alex.chen@example.com",
                "date": "2025-02-20",
                "steps": "8500",
                "sleep_hours": "6.5",
                "water_intake": "2.0",
                "mood": "stressed",
                "heart_rate": "75",
                "status": "active"
            }
        },
        {
            "type": "message",
            "data": "WellnessAI (assistant): I notice your sleep has been below target lately. Let's try a guided breathing exercise before bed. Would you like to start now?"
        },
        {
            "type": "message",
            "data": "Alex (user): Yes, that would be helpful."
        },
        {
            "type": "json",
            "data": {
                "event_type": "wellness_activity",
                "user_email": "alex.chen@example.com",
                "activity_type": "breathing_exercise",
                "duration": "5",
                "completion": "full",
                "timestamp": "2025-02-20T22:00:00Z",
                "status": "completed"
            }
        },
        {
            "type": "message",
            "data": "Alex (user): What should I eat for lunch? I have a busy day ahead."
        },
        {
            "type": "json",
            "data": {
                "event_type": "meal_tracking",
                "user_email": "alex.chen@example.com",
                "meal_type": "lunch",
                "calories": "550",
                "protein": "25",
                "fiber": "8",
                "timestamp": "2025-02-20T12:30:00Z",
                "status": "logged"
            }
        },
        {
            "type": "message",
            "data": "WellnessAI (assistant): Based on your activity level and goals, I recommend a protein-rich lunch. How about a quinoa bowl with grilled chicken and vegetables?"
        },
        {
            "type": "json",
            "data": {
                "event_type": "exercise_tracking",
                "user_email": "alex.chen@example.com",
                "activity_type": "yoga",
                "duration": "20",
                "intensity": "moderate",
                "calories_burned": "150",
                "timestamp": "2025-02-20T07:00:00Z",
                "status": "completed"
            }
        },
        {
            "type": "message",
            "data": "Community Coach (support): Great job incorporating morning yoga! How are you feeling after a week of practice?"
        },
        {
            "type": "json",
            "data": {
                "event_type": "progress_report",
                "user_email": "alex.chen@example.com",
                "report_type": "weekly",
                "stress_trend": "decreasing",
                "sleep_quality": "improving",
                "activity_streak": "5",
                "timestamp": "2025-02-20T23:59:59Z",
                "status": "generated"
            }
        }
    ]

    # Add all episodes to the graph
    for episode in episodes:
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
    
    print("Added all wellness episodes to the graph")
    print("Waiting for graph processing...")
    await asyncio.sleep(30)
    
    return user_id

if __name__ == "__main__":
    user_id = asyncio.run(create_wellness_playground())
    print(f"\nPlayground ready! User ID: {user_id}")
    print("You can now explore the wellness graph and add new episodes!") 