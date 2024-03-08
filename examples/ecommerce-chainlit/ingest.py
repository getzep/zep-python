# Ingest Documents into a Zep Collection
import os

from dotenv import find_dotenv, load_dotenv
from shoe_data import shoes

from zep_python import ZepClient
from zep_python.langchain.vectorstore import ZepVectorStore

load_dotenv(dotenv_path=find_dotenv())

ZEP_API_URL = os.environ.get(
    "ZEP_API_URL"
)  # only required if you're using Zep Open Source

ZEP_API_KEY = os.environ.get("ZEP_API_KEY")  # Required for Zep Cloud
if ZEP_API_KEY is None:
    raise ValueError(
        "ZEP_API_KEY is required for Zep Cloud. "
        "Remove this check if using Zep Open Source."
    )

ZEP_COLLECTION_NAME = "shoe_data"

zep = ZepClient(
    api_key=ZEP_API_KEY,
    api_url=ZEP_API_URL,  # only required if you're using Zep Open Source
)

texts = [str(shoe) for shoe in shoes]

# Add to vectorDB
vectorstore = ZepVectorStore.from_texts(
    texts=texts,
    collection_name=ZEP_COLLECTION_NAME,
    zep_client=zep,
)

print(f"Added {len(shoes)} documents to {ZEP_COLLECTION_NAME}...")
