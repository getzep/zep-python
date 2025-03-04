from zep_cloud.core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zep_cloud.graph.client import GraphClient as BaseGraphClient, AsyncGraphClient as AsyncBaseGraphClient
from zep_cloud.types import EntityType
import typing
from zep_cloud.extractor.ontology_schema import entity_model_to_go_schema
if typing.TYPE_CHECKING:
    from zep_cloud.extractor.ontology_schema import EntityModel
from zep_cloud.core.request_options import RequestOptions

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

    async def set_entity_types(self, entities: dict[str, "EntityModel"], request_options: RequestOptions | None = None):
        print("Setting entity types", entities)
        api_entity_types: list[EntityType] = []
        for name, entity in entities.items():
            entity_dict = entity_model_to_go_schema(entity, name)
            api_entity_types.append(EntityType(**entity_dict))
        print("api_entity_types", api_entity_types)
        res = await self.set_entity_types_internal(entity_types=api_entity_types, request_options=request_options)
        print("res", res)
        return res

    def get_entity_type_internal(self):
        return self.get_entity_types()