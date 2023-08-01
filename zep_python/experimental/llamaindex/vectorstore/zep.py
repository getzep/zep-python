import logging
import math
from typing import Any, List, Optional

from llama_index.schema import TextNode
from llama_index.vector_stores.types import (
    MetadataFilters,
    NodeWithEmbedding,
    VectorStore,
    VectorStoreQuery,
    VectorStoreQueryResult,
)
from llama_index.vector_stores.utils import (
    legacy_metadata_dict_to_node,
    metadata_dict_to_node,
    node_to_metadata_dict,
)

from zep_python import NotFoundError, ZepClient
from zep_python.document import Document as ZepDocument
from zep_python.document import DocumentCollection

logger = logging.getLogger(__name__)


class ZepVectorStore(VectorStore):
    """Zep Vector Store.



    Args:
        api_url (str): Zep API URL
        api_key (str): Zep API key, optional
        collection_name (str):
            name of the collection to store the embeddings in

    """

    stores_text = True
    flat_metadata = False

    def __init__(
        self,
        collection_name: str,
        api_url: str,
        api_key: Optional[str] = None,
        collection_description: Optional[str] = None,
        collection_metadata: Optional[dict] = None,
        embedding_dimensions: Optional[int] = None,
        is_auto_embedded: Optional[bool] = True,
        **kwargs: Any,
    ) -> None:
        """Init params."""

        self._client = ZepClient(base_url=api_url, api_key=api_key)

        try:
            self._collection = self._client.document.get_collection(
                name=collection_name
            )
        except NotFoundError:
            if embedding_dimensions is None:
                raise ValueError(
                    "embedding_dimensions must be specified if collection does not"
                    " exist"
                )
            logger.info(
                f"Collection {collection_name} does not exist, "
                f"will try creating one with dimensions={embedding_dimensions}"
            )
            self._collection = self._client.document.add_collection(
                name=collection_name,
                embedding_dimensions=embedding_dimensions,
                is_auto_embedded=is_auto_embedded,
                description=collection_description,
                metadata=collection_metadata,
            )

    @property
    def client(self) -> ZepClient:
        """Get client."""
        return self._client

    def add(self, embedding_results: List[NodeWithEmbedding]) -> List[str]:
        """Add embedding results to collection.

        Args
            embedding_results: List[NodeWithEmbedding]: list of embedding results

        """
        if not isinstance(self._collection, DocumentCollection):
            raise ValueError("Collection not initialized")

        if self._collection.is_auto_embedded:
            raise ValueError("Collection is auto embedded, cannot add embeddings")

        docs: List[ZepDocument] = []
        ids: List[str] = []

        for result in embedding_results:
            metadata_dict = node_to_metadata_dict(
                result.node, remove_text=True, flat_metadata=self.flat_metadata
            )

            if len(result.node.get_content()) == 0:
                raise ValueError("Cannot add empty document to Zep")

            docs.append(
                ZepDocument(
                    document_id=result.id,
                    content=result.node.get_content(),
                    embedding=result.embedding,
                    metadata=metadata_dict,
                )
            )
            ids.append(result.id)

        self._collection.add_documents(docs)

        return ids

    def delete(
        self, doc_id: Optional[str] = None, *, uuid: str, **delete_kwargs: Any
    ) -> None:
        """Delete doc.

        Args:
            doc_id (Optional[str]): document id (not supported)
            uuid (str): Zep uuid of the document to delete

        """
        if not isinstance(self._collection, DocumentCollection):
            raise ValueError("Collection not initialized")

        if doc_id and len(doc_id) > 0:
            raise NotImplementedError(
                "Delete by ref_doc_id not yet implemented for Zep."
            )

        if not uuid or len(uuid) == 0:
            raise ValueError("uuid must be specified")

        self._collection.delete_document(uuid=uuid)

    def query(
        self,
        query: VectorStoreQuery,
        **kwargs: Any,
    ) -> VectorStoreQueryResult:
        """Query index for top k most similar nodes.

        Args:
            query (List[float]): query embedding

        """

        if not isinstance(self._collection, DocumentCollection):
            raise ValueError("Collection not initialized")

        if query.query_embedding is None and query.query_str is None:
            raise ValueError("query must have either query_str or query_embedding")

        results = self._collection.search(
            text=query.query_str,
            embedding=query.query_embedding,
            limit=query.similarity_top_k,
        )

        similarities = []
        ids = []
        nodes = []
        for d in results:
            """shape of the result is [(vector, distance, metadata)]"""
            text = metadata.pop("text", None)
            node = metadata_dict_to_node(metadata)

            nodes.append(node)
            similarities.append(1.0 - math.exp(-distance))
            ids.append(id_)

        return VectorStoreQueryResult(nodes=nodes, similarities=similarities, ids=ids)
