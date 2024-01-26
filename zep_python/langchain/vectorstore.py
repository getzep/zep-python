from __future__ import annotations

import logging
from typing import Any, Dict, Iterable, List, Optional, Tuple

from zep_python import API_URL, NotFoundError, ZepClient
from zep_python.document import Document as ZepDocument
from zep_python.document import DocumentCollection

try:
    from langchain_core.documents import Document
    from langchain_core.vectorstores import VectorStore
except ImportError:
    raise ImportError(
        "Could not import langchain-core package. "
        "Please install it with `pip install langchain-core`."
    )


logger = logging.getLogger()


class ZepVectorStore(VectorStore):
    """`Zep` VectorStore.

    Provides methods for adding texts or documents to a Zep Collection,
    searching for similar documents, and deleting documents.

    Search scores are calculated using cosine similarity normalized to [0, 1].

    Args:
        collection_name (str): The name of the collection in the Zep store.
        description (Optional[str]): The description of the collection.
        metadata (Optional[Dict[str, Any]]): The metadata to associate with the
            collection.
        zep_client (Optional[ZepClient]): The Zep client to use.
        api_url (str): The URL of the Zep API. Defaults to "https://api.getzep.com".
            Not required if passing in a ZepClient.
        api_key (Optional[str]): The API key for the Zep API.
            Not required if passing in a ZepClient.
    """

    def __init__(
        self,
        collection_name: str,
        description: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        zep_client: Optional[ZepClient] = None,
        api_url: Optional[str] = API_URL,
        api_key: Optional[str] = None,
    ) -> None:
        super().__init__()
        if not collection_name:
            raise ValueError(
                "collection_name must be specified when using ZepVectorStore."
            )
        if zep_client is None:
            self._client = ZepClient(api_url=api_url, api_key=api_key)
        else:
            self._client = zep_client

        self.collection_name = collection_name
        self.c_description = description
        self.c_metadata = metadata

        self._collection = self._load_collection()

    def _load_collection(self) -> DocumentCollection:
        """
        Load the collection from the Zep backend.
        """

        try:
            collection = self._client.document.get_collection(self.collection_name)
        except NotFoundError:
            logger.info(
                f"Collection {self.collection_name} not found. Creating new collection."
            )
            collection = self._create_collection()

        return collection

    def _create_collection(self) -> DocumentCollection:
        """
        Create a new collection in the Zep backend.
        """
        collection = self._client.document.add_collection(
            name=self.collection_name,
            description=self.c_description,
            metadata=self.c_metadata,
        )
        return collection

    def _generate_documents_to_add(
        self,
        texts: Iterable[str],
        metadatas: Optional[List[Dict[Any, Any]]] = None,  # langchain spelling
        document_ids: Optional[List[str]] = None,
    ) -> List[ZepDocument]:
        documents: List[ZepDocument] = []
        for i, d in enumerate(texts):
            documents.append(
                ZepDocument(
                    content=d,
                    metadata=metadatas[i] if metadatas else None,
                    document_id=document_ids[i] if document_ids else None,
                )
            )
        return documents

    def add_texts(
        self,
        texts: Iterable[str],
        metadatas: Optional[List[Dict[str, Any]]] = None,  # langchain spelling
        document_ids: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> List[str]:
        """Run more texts through the embeddings and add to the vectorstore.

        Args:
            texts: Iterable of strings to add to the vectorstore.
            metadatas: Optional list of metadatas associated with the texts.
            document_ids: Optional list of document ids associated with the texts.
            kwargs: vectorstore specific parameters

        Returns:
            List of ids from adding the texts into the vectorstore.
        """
        if not self._collection:
            raise ValueError(
                "collection should be an instance of a Zep DocumentCollection"
            )

        documents = self._generate_documents_to_add(texts, metadatas, document_ids)
        uuids = self._collection.add_documents(documents)

        return uuids

    async def aadd_texts(
        self,
        texts: Iterable[str],
        metadatas: Optional[List[Dict[str, Any]]] = None,  # langchain spelling
        document_ids: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> List[str]:
        """Run more texts through the embeddings and add to the vectorstore."""
        if not self._collection:
            raise ValueError(
                "collection should be an instance of a Zep DocumentCollection"
            )

        documents = self._generate_documents_to_add(texts, metadatas, document_ids)
        uuids = await self._collection.aadd_documents(documents)

        return uuids

    def search(
        self,
        query: str,
        search_type: str,
        metadata_filter: Optional[Dict[str, Any]] = None,
        k: int = 3,
        **kwargs: Any,
    ) -> List[Document]:
        """Return docs most similar to query using specified search type."""
        if search_type == "similarity":
            return self.similarity_search(
                query, k=k, metadata=metadata_filter, **kwargs
            )
        elif search_type == "mmr":
            return self.max_marginal_relevance_search(
                query, k=k, metadata_filter=metadata_filter, **kwargs
            )
        else:
            raise ValueError(
                f"search_type of {search_type} not allowed. Expected "
                "search_type to be 'similarity' or 'mmr'."
            )

    async def asearch(
        self,
        query: str,
        search_type: str,
        metadata_filter: Optional[Dict[str, Any]] = None,
        k: int = 3,
        **kwargs: Any,
    ) -> List[Document]:
        """Return docs most similar to query using specified search type."""
        if search_type == "similarity":
            return await self.asimilarity_search(
                query, k=k, metadata=metadata_filter, **kwargs
            )
        elif search_type == "mmr":
            return await self.amax_marginal_relevance_search(
                query, k=k, metadata_filter=metadata_filter, **kwargs
            )
        else:
            raise ValueError(
                f"search_type of {search_type} not allowed. Expected "
                "search_type to be 'similarity' or 'mmr'."
            )

    def similarity_search(
        self,
        query: str,
        k: int = 4,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> List[Document]:
        """Return docs most similar to query."""

        results = self._similarity_search_with_relevance_scores(
            query, k=k, metadata_filter=metadata, **kwargs
        )
        return [doc for doc, _ in results]

    def similarity_search_with_score(
        self,
        query: str,
        k: int = 4,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> List[Tuple[Document, float]]:
        """Run similarity search with distance."""

        return self._similarity_search_with_relevance_scores(
            query, k=k, metadata_filter=metadata, **kwargs
        )

    def _similarity_search_with_relevance_scores(
        self,
        query: str,
        k: int = 4,
        metadata_filter: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> List[Tuple[Document, float]]:
        """
        Default similarity search with relevance scores.
        Return docs and relevance scores in the range [0, 1].

        0 is dissimilar, 1 is most similar.

        Args:
            query: input text
            k: Number of Documents to return. Defaults to 4.
            metadata_filter: Optional, metadata filter
            **kwargs: kwargs to be passed to similarity search. Should include:
                score_threshold: Optional, a floating point value between 0 to 1 and
                    filter the resulting set of retrieved docs

        Returns:
            List of Tuples of (doc, similarity_score)
        """

        if not self._collection:
            raise ValueError(
                "collection should be an instance of a Zep DocumentCollection"
            )

        results = self._collection.search(
            query, limit=k, metadata=metadata_filter, **kwargs
        )

        return [
            (
                Document(
                    page_content=doc.content,
                    metadata=doc.metadata or {},
                ),
                doc.score or 0.0,
            )
            for doc in results
        ]

    async def asimilarity_search_with_relevance_scores(
        self,
        query: str,
        k: int = 4,
        metadata_filter: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> List[Tuple[Document, float]]:
        """Return docs most similar to query."""

        if not self._collection:
            raise ValueError(
                "collection should be an instance of a Zep DocumentCollection"
            )

        results = await self._collection.asearch(
            query, limit=k, metadata=metadata_filter, **kwargs
        )

        return [
            (
                Document(
                    page_content=doc.content,
                    metadata=doc.metadata or {},
                ),
                doc.score or 0.0,
            )
            for doc in results
        ]

    async def asimilarity_search(
        self,
        query: str,
        k: int = 4,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> List[Document]:
        """Return docs most similar to query."""

        results = await self.asimilarity_search_with_relevance_scores(
            query, k, metadata_filter=metadata, **kwargs
        )

        return [doc for doc, _ in results]

    def max_marginal_relevance_search(  # type: ignore # ignore inconsistent override
        self,
        query: str,
        k: int = 4,
        fetch_k: int = 20,
        lambda_mult: float = 0.5,
        metadata_filter: Optional[Dict[str, Any]] = None,
    ) -> List[Document]:
        """Return docs selected using the maximal marginal relevance reranking.

        Maximal marginal relevance optimizes for similarity to query AND diversity
        among selected documents.

        Args:
            query: Text to look up documents similar to.
            k: Number of Documents to return. Defaults to 4.
            fetch_k: (Unsupported) Number of Documents to fetch to pass to MMR
                algorithm.
            lambda_mult: Number between 0 and 1 that determines the degree
                        of diversity among the results with 0 corresponding
                        to maximum diversity and 1 to minimum diversity.
                        Defaults to 0.5.
            metadata_filter: Optional, metadata to filter the resulting set of retrieved
                docs
        Returns:
            List of Documents selected by maximal marginal relevance.

        NOTE: Zep automatically tunes the number of results returned by the search prior
        to reranking based on `k`. `fetch_k` is ignored.
        """

        if not self._collection:
            raise ValueError(
                "collection should be an instance of a Zep DocumentCollection"
            )

        results = self._collection.search(
            query,
            limit=k,
            metadata=metadata_filter,
            search_type="mmr",
            mmr_lambda=lambda_mult,
        )

        return [
            Document(page_content=d.content, metadata=d.metadata or {}) for d in results
        ]

    async def amax_marginal_relevance_search(
        self,
        query: str,
        k: int = 4,
        fetch_k: int = 20,
        lambda_mult: float = 0.5,
        metadata_filter: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> List[Document]:
        """Return docs selected using the maximal marginal relevance reranking.

        Maximal marginal relevance optimizes for similarity to query AND diversity
        among selected documents.

        Args:
            query: Text to look up documents similar to.
            k: Number of Documents to return. Defaults to 4.
            fetch_k: (Unsupported) Number of Documents to fetch to pass to MMR
                algorithm.
            lambda_mult: Number between 0 and 1 that determines the degree
                        of diversity among the results with 0 corresponding
                        to maximum diversity and 1 to minimum diversity.
                        Defaults to 0.5.
            metadata_filter: Optional, metadata to filter the resulting set of retrieved
                docs
        Returns:
            List of Documents selected by maximal marginal relevance.

        NOTE: Zep automatically tunes the number of results returned by the
        search prior to reranking based on `k`. `fetch_k` is ignored.
        """

        if not self._collection:
            raise ValueError(
                "collection should be an instance of a Zep DocumentCollection"
            )

        results = await self._collection.asearch(
            query,
            limit=k,
            metadata=metadata_filter,
            search_type="mmr",
            mmr_lambda=lambda_mult,
        )

        return [
            Document(page_content=d.content, metadata=d.metadata or {}) for d in results
        ]

    @classmethod
    def from_texts(  # type: ignore # ignore inconsistent override
        cls,
        texts: List[str],
        collection_name: str,
        metadatas: Optional[List[dict]] = None,
        description: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        zep_client: Optional[ZepClient] = None,
        api_url: Optional[str] = API_URL,
        api_key: Optional[str] = None,
        **kwargs: Any,
    ) -> ZepVectorStore:
        """
        Class method that returns a ZepVectorStore instance initialized from texts.

        If the collection does not exist, it will be created.

        Args:
            texts (List[str]): The list of texts to add to the vectorstore.
            collection_name (str): The name of the collection in the Zep store.
            metadatas (Optional[List[Dict[str, Any]]]): Optional list of metadata
               associated with the texts.
            description (Optional[str]): The description of the collection.
            metadata (Optional[Dict[str, Any]]): The metadata to associate with the
                collection.
            zep_client (Optional[ZepClient]): The Zep client to use.
            api_url (Optional[str]): The URL of the Zep API. Defaults to
                "https://api.getzep.com". Not required if passing in a ZepClient.
            api_key (Optional[str]): The API key for the Zep API. Not required if
                passing in a ZepClient.
            **kwargs: Additional parameters specific to the vectorstore.

        Returns:
            ZepVectorStore: An instance of ZepVectorStore.
        """
        vecstore = cls(
            collection_name,
            description=description,
            metadata=metadata,
            zep_client=zep_client,
            api_url=api_url,
            api_key=api_key,
        )
        vecstore.add_texts(texts, metadatas)

        return vecstore

    @classmethod
    async def afrom_texts(  # type: ignore # ignore inconsistent override
        cls,
        texts: List[str],
        collection_name: str,
        metadatas: Optional[List[dict]] = None,
        description: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None,
        zep_client: Optional[ZepClient] = None,
        api_url: Optional[str] = API_URL,
        api_key: Optional[str] = None,
        **kwargs: Any,
    ) -> ZepVectorStore:
        """
        Class method that asynchronously returns a ZepVectorStore instance
        initialized from texts.

        If the collection does not exist, it will be created.

        Args:
            texts (List[str]): The list of texts to add to the vectorstore.
            collection_name (str): The name of the collection in the Zep store.
            metadatas (Optional[List[Dict[str, Any]]]): Optional list of metadata
               associated with the texts.
            description (Optional[str]): The description of the collection.
            metadata (Optional[Dict[str, Any]]): The metadata to associate with the
                collection.
            zep_client (Optional[ZepClient]): The Zep client to use.
            api_url (Optional[str]): The URL of the Zep API. Defaults to
                "https://api.getzep.com". Not required if passing in a ZepClient.
            api_key (Optional[str]): The API key for the Zep API. Not required if
                passing in a ZepClient.
            **kwargs: Additional parameters specific to the vectorstore.

        Returns:
            ZepVectorStore: An instance of ZepVectorStore.
        """
        vecstore = cls(
            collection_name,
            description=description,
            metadata=metadata,
            zep_client=zep_client,
            api_url=api_url,
            api_key=api_key,
        )
        await vecstore.aadd_texts(texts, metadatas)
        return vecstore

    @classmethod
    def from_documents(  # type: ignore # ignore inconsistent override
        cls,
        documents: List[Document],
        **kwargs: Any,
    ) -> ZepVectorStore:
        """Return VectorStore initialized from documents."""
        texts = [d.page_content for d in documents]
        metadatas = [d.metadata for d in documents]
        return cls.from_texts(texts, metadatas=metadatas, **kwargs)

    @classmethod
    async def afrom_documents(  # type: ignore # ignore inconsistent override
        cls,
        documents: List[Document],
        **kwargs: Any,
    ) -> ZepVectorStore:
        """Asynchronously return VectorStore initialized from documents."""
        texts = [d.page_content for d in documents]
        metadatas = [d.metadata for d in documents]
        return await cls.afrom_texts(texts, metadatas=metadatas, **kwargs)

    def delete(self, ids: Optional[List[str]] = None, **kwargs: Any) -> None:
        """Delete by Zep vector UUIDs.

        Parameters
        ----------
        ids : Optional[List[str]]
            The UUIDs of the vectors to delete.

        Raises
        ------
        ValueError
            If no UUIDs are provided.
        """

        if ids is None or len(ids) == 0:
            raise ValueError("No uuids provided to delete.")

        if self._collection is None:
            raise ValueError("No collection name provided.")

        for u in ids:
            self._collection.delete_document(u)
