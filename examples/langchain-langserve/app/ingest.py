# Ingest Documents into a Zep Collection
import os

from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader

from zep_python import ZepClient
from zep_python.langchain.vectorstore import ZepVectorStore

load_dotenv()

SOURCE = "https://en.wikipedia.org/wiki/Leonard_Bernstein"  # noqa: E501

ZEP_API_URL = os.environ.get(
    "ZEP_API_URL"
)  # only required if you're using Zep Open Source

ZEP_API_KEY = os.environ.get("ZEP_API_KEY")  # Required for Zep Cloud
if ZEP_API_KEY is None:
    raise ValueError(
        "ZEP_API_KEY is required for Zep Cloud. "
        "Remove this check if using Zep Open Source."
    )

ZEP_COLLECTION_NAME = os.environ.get("ZEP_COLLECTION")
if ZEP_COLLECTION_NAME is None:
    raise ValueError(
        "ZEP_COLLECTION_NAME is required for ingestion. "
    )

zep = ZepClient(
    api_key=ZEP_API_KEY,
    api_url=ZEP_API_URL,  # only required if you're using Zep Open Source
)

# Load
loader = WebBaseLoader(SOURCE)
data = loader.load()

print(f"Loaded: {len(data)} documents")

# Split
text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=200)
all_splits = text_splitter.split_documents(data)

print(f"Adding {len(all_splits)} documents to {ZEP_COLLECTION_NAME}...")

# Add to vectorDB
vectorstore = ZepVectorStore.from_documents(
    documents=all_splits,
    collection_name=ZEP_COLLECTION_NAME,
    zep_client=zep,
)

print(f"Added {len(all_splits)} documents to {ZEP_COLLECTION_NAME}...")
