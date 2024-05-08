from zep_cloud.core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zep_cloud.document.client import DocumentClient as BaseDocumentClient, AsyncDocumentClient as AsyncBaseDocumentClient


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