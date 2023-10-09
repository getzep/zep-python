import time
from typing import List
from uuid import uuid4

from dotenv import load_dotenv
from faker import Faker
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import FakeEmbeddings
from langchain.memory import ZepMemory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.zep import CollectionConfig, ZepVectorStore

from zep_python.zep_client import ZepClient

fake = Faker()
fake.random.seed(42)


def print_memory(results: List):
    for result in results:
        print(f"{result.role}: {result.content} - {result.metadata}\n")


def main():
    zep_api_url = "http://localhost:8000"
    collection_name = f"babbage{uuid4()}".replace("-", "")
    file = "babbages_calculating_engine.txt"

    client = ZepClient(base_url=zep_api_url)

    print(f"Creating collection {collection_name}")

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
        chunk_size=600,
        chunk_overlap=100,
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

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)

    # Create a session_id for our ZepMemory
    # This is a unique id to identify the session or user,
    # and can be an arbitrary string
    session_id = str(uuid4())

    memory = ZepMemory(
        url=zep_api_url,
        session_id=session_id,
        memory_key="chat_history",
        return_messages=True,
    )

    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(),
        memory=memory,
        verbose=True,
    )

    print(chain.run("Who at the Royal Society presented an award to Babbage?"))

    print(chain.run("What were Babbage's dealings with the Astronomical Society?"))

    print(chain.run("When did Babbage publish his writings on early computing?"))

    print("\n\nInspect Zep's memory")
    print_memory(memory.chat_memory.zep_messages)


if __name__ == "__main__":
    load_dotenv()  # Make sure you have your OpenAI API key in a .env file
    main()
