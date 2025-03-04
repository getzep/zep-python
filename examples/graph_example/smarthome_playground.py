"""
Example of using Zep Graph API to create a smart home automation scenario.
This playground demonstrates user interactions with smart devices,
mixing device data, support conversations, and energy usage patterns.
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

async def create_smarthome_playground() -> None:
    client = AsyncZep(api_key=API_KEY)
    
    # Create a user for the playground
    user_id = uuid.uuid4().hex
    await client.user.add(user_id=user_id, first_name="Emma", last_name="Wilson", email="emma.wilson@example.com")
    print(f"Created playground user: {user_id}")

    # Sample user interactions and system events
    episodes = [
        {
            "type": "message",
            "data": "Emma (user): Hey SmartHome, turn down the temperature in the bedroom."
        },
        {
            "type": "json",
            "data": {
                "event_type": "device_command",
                "device_id": "NEST-BDRM-01",
                "user_email": "emma.wilson@example.com",
                "command": "temperature_adjust",
                "value": 68,
                "timestamp": "2025-02-20T22:30:00Z",
                "location": "bedroom"
            }
        },
        {
            "type": "message",
            "data": "SmartHome (assistant): Temperature in bedroom set to 68°F. Would you like me to schedule this temperature for your regular bedtime?"
        },
        {
            "type": "message",
            "data": "Emma (user): Yes, please do that every night at 10 PM."
        },
        {
            "type": "json",
            "data": {
                "event_type": "automation_created",
                "device_id": "NEST-BDRM-01",
                "user_email": "emma.wilson@example.com",
                "schedule": "daily",
                "time": "22:00",
                "action": "set_temperature",
                "value": 68,
                "location": "bedroom",
                "timestamp": "2025-02-20T22:32:00Z"
            }
        },
        {
            "type": "message",
            "data": "System Alert: Motion detected by front door camera."
        },
        {
            "type": "json",
            "data": {
                "event_type": "security_alert",
                "device_id": "RING-FRONT-01",
                "user_email": "emma.wilson@example.com",
                "alert_type": "motion",
                "location": "front_door",
                "video_clip": "available",
                "timestamp": "2025-02-20T23:15:00Z"
            }
        },
        {
            "type": "message",
            "data": "Emma (user): The garage door isn't responding to the app. Can you help?"
        },
        {
            "type": "json",
            "data": {
                "event_type": "support_ticket",
                "ticket_id": "TICKET-2025-789",
                "user_email": "emma.wilson@example.com",
                "device_id": "GARAGE-MAIN-01",
                "issue_type": "connectivity",
                "status": "open",
                "priority": "high",
                "timestamp": "2025-02-21T09:00:00Z"
            }
        },
        {
            "type": "message",
            "data": "Support (agent): I can see your garage door is offline. Let's try resetting the Wi-Fi module. Can you press the reset button for 10 seconds?"
        },
        {
            "type": "json",
            "data": {
                "event_type": "energy_report",
                "user_email": "emma.wilson@example.com",
                "report_type": "daily",
                "total_kwh": "25.5",
                "highest_usage_device": "NEST-BDRM-01",
                "savings_tips": "bedroom_temp_optimization",
                "timestamp": "2025-02-21T00:00:00Z"
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
    
    print("Added all smart home episodes to the graph")
    print("Waiting for graph processing...")
    await asyncio.sleep(30)
    
    return user_id

if __name__ == "__main__":
    user_id = asyncio.run(create_smarthome_playground())
    print(f"\nPlayground ready! User ID: {user_id}")
    print("You can now explore the smart home graph and add new episodes!") 