from zep.core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zep.base_document.client import BaseDocumentClient, AsyncBaseDocumentClient


class DocumentClient(BaseDocumentClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )


class AsyncDocumentClient(AsyncBaseDocumentClient):
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )
