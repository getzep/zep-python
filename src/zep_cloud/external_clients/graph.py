from zep_cloud.core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zep_cloud.graph.client import GraphClient as BaseGraphClient, AsyncGraphClient as AsyncBaseGraphClient


class GraphClient(BaseGraphClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )


class AsyncGraphClient(AsyncBaseGraphClient):
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )

    def set_entity_type_internal(self, entity_type: str):
        self.set_entity_types()

    def get_entity_type_internal(self):
        return self.get_entity_types()