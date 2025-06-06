from zep_cloud import EntityEdgeSourceTarget, EdgeType
from zep_cloud.core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zep_cloud.external_clients.ontology import EdgeModel, edge_model_to_api_schema
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

    def set_ontology(
            self,
            entities: dict[str, "EntityModel"],
            edges: typing.Optional[dict[str, typing.Union["EdgeModel", typing.Tuple["EdgeModel", typing.List[EntityEdgeSourceTarget]]]]] = None,
            request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Sets the entity and edge types for a project, replacing any existing ones.

        Parameters
        ----------
        entities : dict[str, "EntityModel"]

        edges : typing.Optional[dict[str, typing.Union["EdgeModel", typing.Tuple["EdgeModel", typing.List[EntityEdgeSourceTarget]]]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Examples
        --------

        class Destination(EntityModel):

        \"""A destination is a place that travelers visit.\"""
            destination_name: EntityText = Field(
                description="The name of the destination",
                default=None
            )
            country: EntityText = Field(
                description="The country of the destination",
                default=None
            )
            region: EntityText = Field(
                description="The region of the destination",
                default=None
            )
            description: EntityText = Field(
                description="A description of the destination",
                default=None
            )


        class TravelingTo(EdgeModel):

        \"""An edge representing a traveler going to a destination.\"""
            travel_date: EntityText = Field(
                description="The date of travel to this destination",
                default=None
            )
            purpose: EntityText = Field(
                description="The purpose of travel (Business, Leisure, etc.)",
                default=None
            )

        client.graph.set_ontology(
            entities={
                "Destination": Destination,
            },
            edges={
                "TRAVELING_TO": (
                    TravelingTo,
                    [
                        EntityEdgeSourceTarget(
                            source="User",
                            target="Destination"
                        )
                    ]
                ),
            }
        )
        """
        return self.set_entity_types(
            entities=entities,
            edges=edges,
            request_options=request_options,
        )

    def set_entity_types(
            self,
            entities: dict[str, "EntityModel"],
            edges: typing.Optional[dict[str, typing.Union["EdgeModel", typing.Tuple["EdgeModel", typing.List[EntityEdgeSourceTarget]]]]] = None,
            request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Sets the entity and edge types for a project, replacing any existing ones.

        Parameters
        ----------
        entities : dict[str, "EntityModel"]

        edges : typing.Optional[dict[str, typing.Union["EdgeModel", typing.Tuple["EdgeModel", typing.List[EntityEdgeSourceTarget]]]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Examples
        --------

        class Destination(EntityModel):

        \"""A destination is a place that travelers visit.\"""
            destination_name: EntityText = Field(
                description="The name of the destination",
                default=None
            )
            country: EntityText = Field(
                description="The country of the destination",
                default=None
            )
            region: EntityText = Field(
                description="The region of the destination",
                default=None
            )
            description: EntityText = Field(
                description="A description of the destination",
                default=None
            )


        class TravelingTo(EdgeModel):

        \"""An edge representing a traveler going to a destination.\"""
            travel_date: EntityText = Field(
                description="The date of travel to this destination",
                default=None
            )
            purpose: EntityText = Field(
                description="The purpose of travel (Business, Leisure, etc.)",
                default=None
            )

        client.graph.set_entity_types(
            entities={
                "Destination": Destination,
            },
            edges={
                "TRAVELING_TO": (
                    TravelingTo,
                    [
                        EntityEdgeSourceTarget(
                            source="User",
                            target="Destination"
                        )
                    ]
                ),
            }
        )
        """
        api_entity_types: list[EntityType] = []
        api_edge_types: list[EdgeType] = []

        for name, entity in entities.items():
            entity_dict = entity_model_to_api_schema(entity, name)
            api_entity_types.append(EntityType(**entity_dict))

        if edges:
            for name, edge_data in edges.items():
                # Handle both EdgeModel directly and tuple of (model, source_targets)
                if isinstance(edge_data, tuple):
                    edge_model, source_targets = edge_data
                else:
                    edge_model = edge_data
                    source_targets = None

                edge_dict = edge_model_to_api_schema(edge_model, name)
                if source_targets:
                    edge_dict["source_targets"] = [st.dict() for st in source_targets]
                api_edge_types.append(EdgeType(**edge_dict))
        res = self.set_entity_types_internal(
            entity_types=api_entity_types,
            edge_types=api_edge_types,
            request_options=request_options,
        )
        return res


class AsyncGraphClient(AsyncBaseGraphClient):
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )

    async def set_ontology(
            self,
            entities: dict[str, "EntityModel"],
            edges: typing.Optional[dict[str, typing.Union["EdgeModel", typing.Tuple["EdgeModel", typing.List[EntityEdgeSourceTarget]]]]] = None,
            request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Sets the entity and edge types for a project, replacing any existing ones.

        Parameters
        ----------
        entities : dict[str, "EntityModel"]

        edges : typing.Optional[dict[str, typing.Union["EdgeModel", typing.Tuple["EdgeModel", typing.List[EntityEdgeSourceTarget]]]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Examples
        --------

        class Destination(EntityModel):

        \"""A destination is a place that travelers visit.\"""
            destination_name: EntityText = Field(
                description="The name of the destination",
                default=None
            )
            country: EntityText = Field(
                description="The country of the destination",
                default=None
            )
            region: EntityText = Field(
                description="The region of the destination",
                default=None
            )
            description: EntityText = Field(
                description="A description of the destination",
                default=None
            )


        class TravelingTo(EdgeModel):

        \"""An edge representing a traveler going to a destination.\"""
            travel_date: EntityText = Field(
                description="The date of travel to this destination",
                default=None
            )
            purpose: EntityText = Field(
                description="The purpose of travel (Business, Leisure, etc.)",
                default=None
            )

        await client.graph.set_ontology(
            entities={
                "Destination": Destination,
            },
            edges={
                "TRAVELING_TO": (
                    TravelingTo,
                    [
                        EntityEdgeSourceTarget(
                            source="User",
                            target="Destination"
                        )
                    ]
                ),
            }
        )
        """
        return await self.set_entity_types(
            entities=entities,
            edges=edges,
            request_options=request_options
        )

    async def set_entity_types(
            self,
            entities: dict[str, "EntityModel"],
            edges: typing.Optional[dict[str, typing.Union["EdgeModel", typing.Tuple["EdgeModel", typing.List[EntityEdgeSourceTarget]]]]] = None,
            request_options: typing.Optional[RequestOptions] = None,
    ):
        """
        Sets the entity and edge types for a project, replacing any existing ones.

        Parameters
        ----------
        entities : dict[str, "EntityModel"]

        edges : typing.Optional[dict[str, typing.Union["EdgeModel", typing.Tuple["EdgeModel", typing.List[EntityEdgeSourceTarget]]]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Examples
        --------

        class Destination(EntityModel):

        \"""A destination is a place that travelers visit.\"""
            destination_name: EntityText = Field(
                description="The name of the destination",
                default=None
            )
            country: EntityText = Field(
                description="The country of the destination",
                default=None
            )
            region: EntityText = Field(
                description="The region of the destination",
                default=None
            )
            description: EntityText = Field(
                description="A description of the destination",
                default=None
            )


        class TravelingTo(EdgeModel):

        \"""An edge representing a traveler going to a destination.\"""
            travel_date: EntityText = Field(
                description="The date of travel to this destination",
                default=None
            )
            purpose: EntityText = Field(
                description="The purpose of travel (Business, Leisure, etc.)",
                default=None
            )

        await client.graph.set_entity_types(
            entities={
                "Destination": Destination,
            },
            edges={
                "TRAVELING_TO": (
                    TravelingTo,
                    [
                        EntityEdgeSourceTarget(
                            source="User",
                            target="Destination"
                        )
                    ]
                ),
            }
        )
        """
        api_entity_types: list[EntityType] = []
        api_edge_types: list[EdgeType] = []

        for name, entity in entities.items():
            entity_dict = entity_model_to_api_schema(entity, name)
            api_entity_types.append(EntityType(**entity_dict))

        if edges:
            for name, edge_data in edges.items():
                # Handle both EdgeModel directly and tuple of (model, source_targets)
                if isinstance(edge_data, tuple):
                    edge_model, source_targets = edge_data
                else:
                    edge_model = edge_data
                    source_targets = None

                edge_dict = edge_model_to_api_schema(edge_model, name)
                if source_targets:
                    edge_dict["source_targets"] = [st.dict() for st in source_targets]
                api_edge_types.append(EdgeType(**edge_dict))

        res = await self.set_entity_types_internal(
            entity_types=api_entity_types,
            edge_types=api_edge_types,
            request_options=request_options
        )
        return res
   