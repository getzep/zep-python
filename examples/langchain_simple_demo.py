import time
from typing import List
from uuid import uuid4

from faker import Faker
from langchain.docstore.document import Document
from langchain.embeddings import FakeEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.zep import CollectionConfig, ZepVectorStore

from zep_python import ZepClient

fake = Faker()
fake.random.seed(42)


def print_results(results: List[Document]):
    for result in results:
        content = " ".join(result.page_content.split(" "))
        print(f"{content} - ({result.metadata})\n")


def main():
    zep_api_url = "http://localhost:8000"
    collection_name = f"babbage{uuid4()}".replace("-", "")
    file = "babbages_calculating_engine.txt"

    print(f"Creating collection {collection_name}")

    client = ZepClient(base_url=zep_api_url)

    cfg = CollectionConfig(
        name=collection_name,
        description="Charles Babbage's Babbage's Calculating Engine",
        metadata={},
        embedding_dimensions=1536,
        is_auto_embedded=True,
    )

    vectorstore = ZepVectorStore(
        collection_name=collection_name,
        config=cfg,
        api_url=zep_api_url,
        embedding=FakeEmbeddings(size=1),
    )

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50,
        length_function=len,
    )

    with open(file) as f:
        raw_text = f.read()

    print("Splitting text into chunks and adding them to the Zep vector store.")
    docs = text_splitter.create_documents([raw_text])
    uuids = vectorstore.add_documents(docs)
    print(f"Added {len(uuids)} documents to collection {collection_name}")

    print("Waiting for documents to be embedded")
    while True:
        c = client.document.get_collection(collection_name)
        print(
            "Embedding status: "
            f"{c.document_embedded_count}/{c.document_count} documents embedded"
        )
        time.sleep(1)
        if c.status == "ready":
            break

    query = "What is Charles Babbage best known for?"

    print(f"\nSearching for '{query}'\n")
    results = vectorstore.search(query, search_type="similarity", k=5)
    print_results(results)

    print(f"\nSearching for '{query}' with MMR reranking\n")
    results = vectorstore.search(query, search_type="mmr", k=5)
    print_results(results)


if __name__ == "__main__":
    main()
