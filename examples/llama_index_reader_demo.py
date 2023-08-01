import time
from typing import List
from uuid import uuid4

from llama_index.node_parser import SimpleNodeParser
from llama_index.readers.schema.base import Document

from zep_python import ZepClient
from zep_python.document import Document as ZepDocument
from zep_python.experimental.llamaindex import ZepReader


def main():
    zep_api_url = "http://localhost:8000"
    collection_name = f"babbage{uuid4()}".replace("-", "")
    file = "babbages_calculating_engine.txt"

    print(f"Creating collection {collection_name}")

    client = ZepClient(base_url=zep_api_url)
    collection = client.document.add_collection(
        name=collection_name,  # required
        description="Charles Babbage's Babbage's Calculating Engine",  # optional
        metadata={"foo": "bar"},  # optional metadata
        embedding_dimensions=384,  # this must match the model you've configured in Zep
        is_auto_embedded=True,  # use Zep's built-in embedder. Defaults to True
    )

    node_parser = SimpleNodeParser.from_defaults(chunk_size=500, chunk_overlap=20)

    with open(file) as f:
        raw_text = f.read()

    print("Splitting text into chunks and adding them to the Zep vector store.")
    docs = node_parser.get_nodes_from_documents(
        [Document(text=raw_text)], show_progress=True
    )
    # Convert nodes to ZepDocument
    zep_docs = [ZepDocument(content=d.get_content()) for d in docs]
    uuids = collection.add_documents(zep_docs)
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

    query = "Was Babbage awarded a medal??"

    reader = ZepReader(api_url=zep_api_url)
    results = reader.load_data(collection_name=collection_name, query=query, top_k=5)

    print("\n".join([r.text for r in results]))


if __name__ == "__main__":
    main()
