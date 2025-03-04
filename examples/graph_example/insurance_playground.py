"""
Example of using Zep Graph API to create an insurance claims processing scenario.
This playground demonstrates customer interactions with an insurance system,
mixing chat messages and claim events to build a knowledge graph.
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

async def create_insurance_playground() -> None:
    client = AsyncZep(api_key=API_KEY)
    
    # Create a user for the playground
    user_id = uuid.uuid4().hex
    await client.user.add(user_id=user_id, first_name="John", last_name="Doe", email="john.doe@example.com")
    print(f"Created playground user: {user_id}")

    # Sample user interactions and system events
    episodes = [
        {
            "type": "message",
            "data": "John (user): Hi, I need to file a claim for a car accident that happened yesterday."
        },
        {
            "type": "json",
            "data": {
                "event_type": "claim_submission",
                "claim_id": "CLAIM-2025-12345",
                "user_email": "john.doe@example.com",
                "incident_type": "car_accident",
                "claim_amount": 5200,
                "status": "pending_review",
                "submission_date": "2025-02-15T09:30:00Z",
                "location": "downtown_intersection"
            }
        },
        {
            "type": "message",
            "data": "InsuranceBot (assistant): I'll help you file that claim. Can you provide the police report number and upload photos of the damage?"
        },
        {
            "type": "message",
            "data": "John (user): The police report number is #PD-98765, and I've uploaded 4 photos of the damage."
        },
        {
            "type": "json",
            "data": {
                "event_type": "document_submission",
                "claim_id": "CLAIM-2025-12345",
                "user_email": "john.doe@example.com",
                "document_type": "police_report",
                "reference": "PD-98765",
                "photos_uploaded": 4,
                "submission_timestamp": "2025-02-15T09:35:00Z"
            }
        },
        {
            "type": "message",
            "data": "System Alert: Automated review detected possible pre-existing damage in submitted photos."
        },
        {
            "type": "json",
            "data": {
                "event_type": "fraud_detection",
                "claim_id": "CLAIM-2025-12345",
                "user_email": "john.doe@example.com",
                "flag_type": "damage_review",
                "risk_score": 0.6,
                "flag_reason": "possible_preexisting_damage",
                "detection_timestamp": "2025-02-15T09:40:00Z"
            }
        },
        {
            "type": "message",
            "data": "Claims Agent (internal): Review required for claim CLAIM-2025-12345. Please check photo timestamps against accident date."
        },
        {
            "type": "json",
            "data": {
                "event_type": "policy_recommendation",
                "user_email": "john.doe@example.com",
                "current_policy": "auto_basic",
                "recommended_policy": "auto_premium",
                "monthly_difference": 20,
                "benefits": ["roadside_assistance", "rental_coverage"],
                "recommendation_reason": "recent_claim",
                "timestamp": "2025-02-15T10:00:00Z"
            }
        },
        {
            "type": "message",
            "data": "InsuranceBot (assistant): While we process your claim, I notice you might benefit from our Premium Auto coverage. It includes rental car coverage, which would be helpful in situations like this."
        },
        {
            "type": "json",
            "data": {
                "event_type": "user_profile_update",
                "user_email": "john.doe@example.com",
                "age": 35,
                "driving_history": "clean_5_years",
                "homeowner": True,
                "risk_score": 0.8,
                "preferred_contact": "email",
                "update_timestamp": "2025-02-15T10:05:00Z"
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
    
    print("Added all insurance episodes to the graph")
    print("Waiting for graph processing...")
    await asyncio.sleep(30)
    
    return user_id

if __name__ == "__main__":
    user_id = asyncio.run(create_insurance_playground())
    print(f"\nPlayground ready! User ID: {user_id}")
    print("You can now explore the insurance claim graph and add new episodes!") 