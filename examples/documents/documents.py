""" Using Zep as a vector database. A simple sync example. """
import os
import time
from uuid import uuid4

from dotenv import load_dotenv
from faker import Faker
from utils import print_results, read_chunk_from_file

from zep_python import ZepClient
from zep_python.document import Document

fake = Faker()

load_dotenv()  # load environment variables from .env file, if present

API_KEY = os.environ.get("ZEP_API_KEY") or "YOUR_API_KEY"
API_URL = os.environ.get("ZEP_API_URL")  # only required if you're using Zep Open Source

INPUT_FILE = "babbages_calculating_engine.txt"


def main():
    max_chunk_size = 500
    collection_name = f"babbage{uuid4()}".replace("-", "")

    client = ZepClient(api_key=API_KEY, api_url=API_URL)
    collection = client.document.add_collection(
        name=collection_name,  # required
        description="Charles Babbage's Babbage's Calculating Engine",  # optional
        metadata=fake.pydict(allowed_types=[str]),  # optional metadata
    )

    chunks = read_chunk_from_file(INPUT_FILE, max_chunk_size)

    documents = [
        Document(
            content=chunk,
            document_id=fake.unique.file_name(extension="txt"),
            metadata=fake.pydict(allowed_types=[str]),  # optional metadata
        )
        for chunk in chunks
    ]

    print(f"\nAdding {len(documents)} documents to collection {collection_name}")

    uuids = collection.add_documents(documents)

    print(f"\nAdded {len(uuids)} documents to collection {collection_name}")

    # monitor embedding progress
    while True:
        c = client.document.get_collection(collection_name)
        print(
            "Embedding status: "
            f"{c.document_embedded_count}/{c.document_count} documents embedded"
        )
        time.sleep(1)
        if c.status == "ready":
            break

    # List all collections
    collections = client.document.list_collections()
    print(f"\nFound {len(collections)} collections")
    print("\n".join([c.name for c in collections]))

    # Update collection description and metadata
    client.document.update_collection(
        collection_name,
        description="Charles Babbage's Babbage's Calculating Engine 2",
        metadata=fake.pydict(allowed_types=[str]),
    )

    # Get updated collection
    collection = client.document.get_collection(collection_name)
    print(f"\nUpdated collection description: {collection.description}")

    # search for documents
    # Using "the moon" here as we should find documents related to "astronomy"
    query = "the moon"
    search_results = collection.search(text=query, limit=3)
    print(f"\nFound {len(search_results)} documents matching query '{query}'")
    print_results(search_results)

    # retrieve a single document by uuid
    document_to_retrieve = uuids[25]
    print(f"\nRetrieving document {document_to_retrieve}")
    retrieved_document = collection.get_document(document_to_retrieve)
    print(retrieved_document.to_dict())

    # Update a document's metadata
    print(f"\nUpdating document {document_to_retrieve} metadata")
    collection.update_document(
        document_to_retrieve,
        document_id="new_document_id",
        metadata={"foo": "bar", "baz": "qux"},
    )

    # search for documents using both text and metadata
    metadata_query = {
        "where": {"jsonpath": '$[*] ? (@.baz == "qux")'},
    }
    new_search_results = collection.search(text=query, metadata=metadata_query, limit=3)
    print(
        f"\nFound {len(new_search_results)} documents matching query '{query}'"
        f" {metadata_query}"
    )
    print_results(new_search_results)

    # delete a document
    print(f"\nDeleting document {document_to_retrieve}")
    collection.delete_document(document_to_retrieve)

    # Get a list of documents in the collection by uuid
    docs_to_get = uuids[40:43]
    print(f"\nGetting documents: {docs_to_get}")
    documents = collection.get_documents(docs_to_get)
    print(f"Got {len(documents)} documents")
    print_results(documents)

    # Delete the collection
    # Uncomment to delete the collection
    # print(f"Deleting collection {collection_name}")
    # client.document.delete_collection(collection_name)


if __name__ == "__main__":
    main()
