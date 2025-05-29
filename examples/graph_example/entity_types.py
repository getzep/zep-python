import asyncio
import os

from dotenv import find_dotenv, load_dotenv

from zep_cloud import EntityEdgeSourceTarget
from zep_cloud.client import AsyncZep
from pydantic import Field
from zep_cloud.external_clients.ontology import EntityModel, EntityText, EdgeModel

load_dotenv(
    dotenv_path=find_dotenv()
)

API_KEY = os.environ.get("ZEP_API_KEY") or "YOUR_API_KEY"


async def main() -> None:
    client = AsyncZep(
        api_key=API_KEY,
    )

    class Destination(EntityModel):
        """
        A destination is a place that travelers visit.
        """
        destination_name: EntityText = Field(
            description="The name of the destination",
            default=None
        )
        country: EntityText = Field(
            description="The country of the destination",
            default=None
        )
        region: EntityText = Field(
            description="The region of the destination",
            default=None
        )
        description: EntityText = Field(
            description="A description of the destination",
            default=None
        )

    class TravelingTo(EdgeModel):
        """
        An edge representing a traveler going to a destination.
        """
        travel_date: EntityText = Field(
            description="The date of travel to this destination",
            default=None
        )
        purpose: EntityText = Field(
            description="The purpose of travel (Business, Leisure, etc.)",
            default=None
        )

    await client.graph.set_entity_types(
        entities={
            "Destination": Destination,
        },
        edges={
            "TRAVELING_TO": (
                TravelingTo,
                [
                    EntityEdgeSourceTarget(
                        source="User",
                        target="Destination"
                    )
                ]
            ),
        }
    )
    enntl = await client.graph.list_entity_types()
    print(enntl)

if __name__ == "__main__":
    asyncio.run(main())