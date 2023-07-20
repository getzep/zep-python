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
        document_collection_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

        document_collection = DocumentCollection(
            name=document_collection_name,
            metadata={"foo": "bar"},
            embedding_dimensions=768,
            embedding_model_name="bert-base-uncased",
            distance_function="cosine",
            is_normalized=True,
            description="Test document collection"
        )

        
        print(f"\n1.  Creating document collection: {document_collection_name}")
        try:
            document_collection = await client.add_documentcollection(
                document_collection
            )
            print(document_collection)
        except APIError as e:
            print(f"Unable to create document collection {document_collection_name}")
            print(e)

        # 3.    Get document collection
        print(f"\n2.  Getting document collection: {document_collection_name}")
        try:
            get_collection = await client.get_documentcollection(
                document_collection_name
            )
            print(document_collection)
        except NotFoundError as e:
            print(f"Unable to get document collection {document_collection_name}")
            print(e)
        except APIError as e:
            print(f"Unable to get document collection {document_collection_name}")
            print(e)
        

        # Modify document collection
        print(f"\n3.  Modifying document collection: {document_collection_name}")
        modified_collection = DocumentCollection(
            name=document_collection_name,
            metadata={"fools": "gold"},
            description = "Modified description"
        )

        try:
            document_collection = await client.update_documentcollection(
                modified_collection
            )

            print(document_collection)
        except NotFoundError as e:
            print(f"Unable to modify document collection {document_collection_name}")
            print(e)
        except APIError as e:
            print(f"Unable to modify document collection {document_collection_name}")
            print(e)
            
if __name__ == "__main__":
    asyncio.run(main())
