from zep_cloud.core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zep_cloud.graph.client import GraphClient as BaseGraphClient, AsyncGraphClient as AsyncBaseGraphClient
from zep_cloud.types import EntityType
import typing
from zep_cloud.external_clients.ontology import entity_model_to_api_schema
if typing.TYPE_CHECKING:
    from zep_cloud.external_clients.ontology import EntityModel
from zep_cloud.core.request_options import RequestOptions

class GraphClient(BaseGraphClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )

    def set_entity_types(self, entities: dict[str, "EntityModel"], request_options: typing.Optional[RequestOptions] = None):
        api_entity_types: list[EntityType] = []
        for name, entity in entities.items():
            entity_dict = entity_model_to_api_schema(entity, name)
            api_entity_types.append(EntityType(**entity_dict))
        res = self.set_entity_types_internal(entity_types=api_entity_types, request_options=request_options)
        return res


class AsyncGraphClient(AsyncBaseGraphClient):
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )

    async def set_entity_types(self, entities: dict[str, "EntityModel"], request_options: typing.Optional[RequestOptions] = None):
        api_entity_types: list[EntityType] = []
        for name, entity in entities.items():
            entity_dict = entity_model_to_api_schema(entity, name)
            api_entity_types.append(EntityType(**entity_dict))
        res = await self.set_entity_types_internal(entity_types=api_entity_types, request_options=request_options)
        return res
   