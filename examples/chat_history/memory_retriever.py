import asyncio
import os
from typing import List, Optional

from dotenv import find_dotenv, load_dotenv

from zep_cloud.langchain.retriever import ZepCloudRetriever

load_dotenv(
    dotenv_path=find_dotenv()
)  # load environment variables from .env file, if present

API_KEY = os.environ.get("ZEP_API_KEY") or "YOUR_API_KEY"

async def main() -> None:
    zep_retriever = ZepCloudRetriever(
        api_key=API_KEY,
        search_scope="facts",
        min_score=0.8,
    )

    search_results = await zep_retriever.ainvoke("new shoes")
    print(search_results)


if __name__ == "__main__":
    asyncio.run(main())