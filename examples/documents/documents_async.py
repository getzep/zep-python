""" Using Zep as a vector database. A simple sync example. """
import asyncio
import os
import time
from uuid import uuid4

from faker import Faker
from utils import print_results, read_chunk_from_file

from zep_python import ZepClient
from zep_python.document import Document

fake = Faker()
fake.random.seed(42)


async def main(file: str):
    max_chunk_size = 500
    collection_name = f"babbage{uuid4()}".replace("-", "")

    print(f"Creating collection {collection_name}")

    api_key = os.environ.get("API_KEY")
    if api_key is None:
        raise ValueError("API_KEY environment variable must be set")

    client = ZepClient(api_key=api_key)
    collection = client.document.add_collection(
        name=collection_name,  # required
        description="Charles Babbage's Babbage's Calculating Engine",  # optional
        metadata=fake.pydict(allowed_types=[str]),  # optional metadata
    )

    chunks = read_chunk_from_file(file, max_chunk_size)

    documents = [
        Document(
            content=chunk,
            document_id=fake.unique.file_name(extension="txt"),
            metadata=fake.pydict(allowed_types=[str]),  # optional metadata
        )
        for chunk in chunks
    ]

    print(f"Adding {len(documents)} documents to collection {collection_name}")

    uuids = await collection.aadd_documents(documents)

    print(f"Added {len(uuids)} documents to collection {collection_name}")

    # monitor embedding progress
    while True:
        c = await client.document.aget_collection(collection_name)
        print(
            "Embedding status: "
            f"{c.document_embedded_count}/{c.document_count} documents embedded"
        )
        time.sleep(1)
        if c.status == "ready":
            break

    # List all collections
    collections = await client.document.alist_collections()
    print(f"Found {len(collections)} collections")
    print("\n".join([c.name for c in collections]))

    # Update collection description and metadata
    await client.document.aupdate_collection(
        collection_name,
        description="Charles Babbage's Babbage's Calculating Engine 2",
        metadata=fake.pydict(allowed_types=[str]),
    )

    # Get updated collection
    collection = await client.document.aget_collection(collection_name)
    print(f"Updated collection description: {collection.description}")

    # search for documents
    # Using "the moon" here as we should find documents related to "astronomy"
    query = "the moon"
    search_results = await collection.asearch(text=query, limit=5)
    print(f"Found {len(search_results)} documents matching query '{query}'")
    print_results(search_results)

    # retrieve a single document by uuid
    document_to_retrieve = uuids[25]
    print(f"Retrieving document {document_to_retrieve}")
    retrieved_document = await collection.aget_document(document_to_retrieve)
    print(retrieved_document.dict())

    # Update a document's metadata
    print(f"Updating document {document_to_retrieve} metadata")
    await collection.aupdate_document(
        document_to_retrieve,
        description="Charles Babbage's Babbage's Calculating Engine 2",
        metadata={"foo": "bar", "baz": "qux"},
    )

    # search for documents using both text and metadata
    metadata_query = {
        "where": {"jsonpath": '$[*] ? (@.baz == "qux")'},
    }
    new_search_results = await collection.asearch(
        text=query, metadata=metadata_query, limit=5
    )
    print(
        f"Found {len(new_search_results)} documents matching query '{query}'"
        f" {metadata_query}"
    )
    print_results(new_search_results)

    # Search by embedding
    interesting_document = search_results[0]
    print(f"Searching for documents similar to:\n{interesting_document.content}\n")
    embedding_search_results = await collection.asearch(
        embedding=interesting_document.embedding, limit=5
    )
    print(f"Found {len(embedding_search_results)} documents matching embedding")
    print("Most similar documents:")
    print_results(embedding_search_results)

    # delete a document
    print(f"Deleting document {document_to_retrieve}")
    await collection.adelete_document(document_to_retrieve)

    # Get a list of documents in the collection by uuid
    docs_to_get = uuids[40:50]
    print(f"Getting documents: {docs_to_get}")
    documents = await collection.aget_documents(docs_to_get)
    print(f"Got {len(documents)} documents")
    print_results(documents)

    # Index the collection
    # We wouldn't ordinarily do this until the collection is larger.
    # See the documentation for more details.
    print(f"Indexing collection {collection_name}")
    collection.create_index(force=True)  # Do not use force unless testing!

    # search for documents now that the collection is indexed
    search_results = collection.search(text=query, limit=5)
    print(f"Found {len(search_results)} documents matching query '{query}'")
    print_results(search_results)

    # Delete the collection
    print(f"Deleting collection {collection_name}")
    await client.document.adelete_collection(collection_name)


if __name__ == "__main__":
    file = "babbages_calculating_engine.txt"
    asyncio.run(main(file))
