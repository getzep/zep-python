import asyncio
import os

from dotenv import find_dotenv, load_dotenv

from zep_cloud.client import AsyncZep
from zep_cloud.types import SearchFilters
from pydantic import Field
from zep_cloud.external_clients.ontology import EntityModel, EntityText, EntityFloat, EntityInt
load_dotenv(
    dotenv_path=find_dotenv()
)

API_KEY = os.environ.get("ZEP_API_KEY") or "YOUR_API_KEY"


async def main() -> None:
    client = AsyncZep(
        api_key=API_KEY,
    )
    class Purchase(EntityModel):
        """
        A purchase is an item that was purchased.
        """
        item_name: EntityText = Field(
            description="The name of the item purchased",
            default=None
        )
        item_price: EntityFloat = Field(
            description="The price of the item",
            default=None
        )
        quantity: EntityInt = Field(
            description="The quantity of the item purchased",
            default=None
        )
        additional_notes: EntityText = Field(
            description="Additional notes about the purchase",
            default=None
        )
    await client.graph.set_entity_types(
        entities={}
    )
    enntl = await client.graph.list_entity_types()
    print(enntl)


if __name__ == "__main__":
    asyncio.run(main())