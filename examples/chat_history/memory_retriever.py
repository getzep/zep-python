import asyncio
import os
from typing import List, Optional

from dotenv import find_dotenv, load_dotenv

from zep_cloud.langchain.retriever import ZepCloudRetriever

load_dotenv(
    dotenv_path=find_dotenv()
)  # load environment variables from .env file, if present

API_KEY = os.environ.get("ZEP_API_KEY") or "YOUR_API_KEY"
SESSION_ID = os.environ.get("ZEP_SESSION_ID")

async def main() -> None:
    zep_retriever = ZepCloudRetriever(
        session_ids=[SESSION_ID],
        api_key=API_KEY,
        search_scope="summary",
    )

    search_results = await zep_retriever.ainvoke("new shoes")

    for r in search_results:
        print(r)
        if r.metadata["score"] > 0.8:  # Only print results with similarity of 0.8 or higher
            print(r.page_content, "Score: ", r.metadata["score"])


if __name__ == "__main__":
    asyncio.run(main())