import typing

from zep_cloud.core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zep_cloud.core.request_options import RequestOptions
from zep_cloud.external_clients.ontology import (
    EdgeModel,
    edge_model_to_api_schema,
    entity_model_to_api_schema,
)
from zep_cloud.graph.client import AsyncGraphClient as AsyncBaseGraphClient
from zep_cloud.graph.client import GraphClient as BaseGraphClient
from zep_cloud.types import EdgeSourceTarget, EdgeType, EntityType, Ontology

if typing.TYPE_CHECKING:
    from zep_cloud.external_clients.ontology import EntityModel

EdgeSpec = typing.Union[
    "EdgeModel",
    typing.Tuple["EdgeModel", typing.List[EdgeSourceTarget]],
]


def build_ontology(
    entities: typing.Dict[str, "EntityModel"],
    edges: typing.Optional[typing.Dict[str, EdgeSpec]] = None,
) -> typing.Tuple[typing.List[EntityType], typing.List[EdgeType]]:
    """Turn the Pydantic ontology models into the types the v4 API accepts.

    This is the whole value the hand-written layer adds: the wire shape is a
    list of entity and edge types, and this derives it from Python classes so an
    ontology is declared once, in the type system.
    """
    api_entity_types: typing.List[EntityType] = []
    for name, entity in entities.items():
        api_entity_types.append(EntityType(**entity_model_to_api_schema(entity, name)))

    api_edge_types: typing.List[EdgeType] = []
    if edges:
        for name, edge_data in edges.items():
            if isinstance(edge_data, tuple):
                edge_model, source_targets = edge_data
            else:
                edge_model, source_targets = edge_data, None

            edge_dict = edge_model_to_api_schema(edge_model, name)
            if source_targets:
                edge_dict["source_targets"] = [
                    st.dict() if hasattr(st, "dict") else st for st in source_targets
                ]
            api_edge_types.append(EdgeType(**edge_dict))

    return api_entity_types, api_edge_types


class GraphClient(BaseGraphClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)

    def set_entity_types(
        self,
        graph_uuid: str,
        entities: typing.Dict[str, "EntityModel"],
        edges: typing.Optional[typing.Dict[str, EdgeSpec]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ontology:
        """
        Set the entity and edge types for one graph, replacing its existing ontology.

        The graph is an explicit argument. v3 took ``user_ids`` and ``graph_ids``
        and fanned out server-side; v4 has one ontology endpoint per scope
        (spec-3 14.4), so a caller targeting several graphs calls this once per
        graph, and a caller targeting the project default passes the same
        ``build_ontology`` output to ``client.project.set_ontology``.

        Examples
        --------
        client.graph.set_entity_types(
            graph_uuid="...",
            entities={"Traveler": Traveler},
            edges={
                "TRAVELED_TO": (
                    TraveledTo,
                    [EdgeSourceTarget(source_entity_type="Traveler", target_entity_type="Destination")],
                ),
            },
        )
        """
        entity_types, edge_types = build_ontology(entities, edges)
        return self.set_ontology(
            graph_uuid,
            entity_types=entity_types,
            edge_types=edge_types,
            request_options=request_options,
        )


class AsyncGraphClient(AsyncBaseGraphClient):
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)

    async def set_entity_types(
        self,
        graph_uuid: str,
        entities: typing.Dict[str, "EntityModel"],
        edges: typing.Optional[typing.Dict[str, EdgeSpec]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ontology:
        """Asynchronous counterpart of :meth:`GraphClient.set_entity_types`."""
        entity_types, edge_types = build_ontology(entities, edges)
        return await self.set_ontology(
            graph_uuid,
            entity_types=entity_types,
            edge_types=edge_types,
            request_options=request_options,
        )
