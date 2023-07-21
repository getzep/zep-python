""" Example of using the Zep Python SDK asynchronously for Documents.
"""
import asyncio
import datetime

from zep_python import (
    APIError,
    Document,
    DocumentCollection,
    NotFoundError,
    ZepClient,
)


async def main() -> None:
    base_url = "http://localhost:8000"  # TODO: Replace with Zep API URL

    api_key = "YOUR_API_KEY"  # TODO: Replace with your API key

    async with ZepClient(base_url, api_key) as client:
        # Document operations
        print(f"------Document operations:")

        # Create document collection
        collection_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        collection = DocumentCollection(
            name=collection_name,
            metadata={"foo": "bar"},
            embedding_dimensions=768,
            embedding_model_name="bert-base-uncased",
            distance_function="cosine",
            is_normalized=True,
            description="Test document collection",
        )

        print(f"\n.  Creating document collection: {collection_name}")
        try:
            status = await client.add_collection(collection)
            print(status)
        except APIError as e:
            print(f"Unable to create document collection {collection_name}")
            print(e)
            return

        # 2.    Get document collection
        print(f"\n.  Getting document collection: {collection_name}")
        try:
            found_collection = await client.get_collection(collection_name)
            print(found_collection)
        except NotFoundError as e:
            print(f"Unable to get document collection {collection_name}")
            print(e)
        except APIError as e:
            print(f"Unable to get document collection {collection_name}")
            print(e)
            return

        # Modify document collection
        print(f"\n.  Modifying document collection: {collection_name}")
        modified_collection = DocumentCollection(
            name=collection_name,
            metadata={"fools": "gold"},
            description="Modified description",
        )

        try:
            status = await client.update_collection(modified_collection)
            print(status)
        except NotFoundError as e:
            print(f"Unable to modify document collection {collection_name}")
            print(e)
        except APIError as e:
            print(f"Unable to modify document collection {collection_name}")
            print(e)
            return

        # List document collections
        print(f"\n.  Listing document collections")
        try:
            document_collections = await client.list_collections()
            if len(document_collections) == 0:
                print("No document collections found")
            else:
                print([collection.name for collection in document_collections])
        except APIError as e:
            print(f"Unable to list document collections")
            print(e)
            return

        # Create document
        document_id = "test_doc_1"
        print(f"\n.  Creating document {document_id}")
        documents = [
            Document(
                document_id=document_id,
                content="This is a test document",
                metadata={"foo": "bar"},
            ),
            Document(
                document_id="test_doc_2",
                content="This is another test document",
                metadata={"foo": "bar"},
            ),
        ]
        doc_uuids = None
        try:
            doc_uuids = await client.add_document(collection_name, documents)
            print(doc_uuids)
        except APIError as e:
            print(f"Unable to create document")
            print(e)
            return

        # Get document
        document_uuid = doc_uuids[0]
        print(f"\n.  Getting document {document_uuid}")

        try:
            document = await client.get_document(collection_name, document_uuid)
            print(document)
        except NotFoundError as e:
            print(f"Unable to get document")
            print(e)
        except APIError as e:
            print(f"Unable to get document")
            print(e)
            return

        # Update document
        print(f"\n.  Updating document {document_uuid}")
        modified_document = Document(
            uuid=document_uuid,
            document_id="newdocid",
            metadata={"fools": "gold"},
        )
        try:
            status = await client.update_document(collection_name, modified_document)
            print(status)
        except NotFoundError as e:
            print(f"Unable to modify document")
            print(e)
        except APIError as e:
            print(f"Unable to modify document")
            print(e)
            # return

        # Get updated document
        document_uuid = doc_uuids[0]
        print(f"\n.  Getting updated document {document_uuid}")

        try:
            document = await client.get_document(collection_name, document_uuid)
            print(document)
        except NotFoundError as e:
            print(f"Unable to get document")
            print(e)
        except APIError as e:
            print(f"Unable to get document")
            print(e)
            return

        # Batch update documents
        print(f"\n.  Batch updating documents {document_uuid}, {doc_uuids[1]}")
        documents = [
            Document(
                uuid=document_uuid,
                document_id="newdocid",
                metadata={"fools": "gold"},
            ),
            Document(
                uuid=doc_uuids[1],
                document_id="newdocid2",
                metadata={"fools": "gold"},
            ),
        ]

        try:
            status = await client.batchupdate_documents(collection_name, documents)
            print(status)
        except NotFoundError as e:
            print(f"Unable to modify documents")
            print(e)
        except APIError as e:
            print(f"Unable to modify documents")
            print(e)
            # return

        # Batch get documents by id
        document_ids = {"document_id": ["newdocuid", "newdocid2"]}
        print(f"\n.  Batch getting documents by document id {document_ids}")
        try:
            documents = await client.batchget_documents_byid(
                collection_name, document_ids
            )
            print(documents)
        except NotFoundError as e:
            print(f"Unable to get documents")
            print(e)
        except APIError as e:
            print(f"Unable to get documents")
            print(e)
            return

        # Batch get documents by uuid
        document_uuids = {"uuid": [str(document_uuid), str(doc_uuids[1])]}
        print(f"\n.  Batch getting documents by uuid: {document_uuids}")
        try:
            documents = await client.batchget_documents_byuuid(
                collection_name, document_uuids
            )
            print(documents)
        except NotFoundError as e:
            print(f"Unable to get documents")
            print(e)
        except APIError as e:
            print(f"Unable to get documents")
            print(e)
            # return

        # Batch delete documents
        print(f"\n.  Batch deleting documents - {document_uuids}")
        delete_uuids = [str(document_uuid), str(doc_uuids[1])]
        try:
            status = await client.batchdelete_documents(collection_name, delete_uuids)
            print(status)
        except NotFoundError as e:
            print(f"Unable to delete documents")
            print(e)
        except APIError as e:
            print(f"Unable to delete documents")
            print(e)
            return

        # Delete document
        print(f"\n.  Deleting document {document_uuid}")
        try:
            status = await client.delete_document(collection_name, document_uuid)
            print(status)
        except NotFoundError as e:
            print(f"Unable to delete document")
            print(e)
        except APIError as e:
            print(f"Unable to delete document")
            print(e)
            return

        # Delete document collection
        print(f"\nLAST.  Deleting document collection: {collection_name}")
        try:
            status = await client.delete_collection(collection_name)
            print(status)
        except NotFoundError as e:
            print(f"Unable to delete document collection {collection_name}")
            print(e)
        except APIError as e:
            print(f"Unable to delete document collection {collection_name}")
            print(e)
            return


if __name__ == "__main__":
    asyncio.run(main())
