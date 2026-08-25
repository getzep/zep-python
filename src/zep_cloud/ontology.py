"""Declare a Zep ontology with Python classes.

``graph.set_ontology`` and ``project.set_ontology`` accept lists of
``EntityType`` and ``EdgeType``. Building those by hand means repeating each
property's name, type and description as data. This module lets an ontology be
declared once, as classes, and derives the payload from them::

    from zep_cloud.ontology import EdgeModel, EntityModel, EntityText, build_ontology
    from zep_cloud.types import EdgeSourceTarget

    class Traveler(EntityModel):
        \"\"\"Someone who takes trips.\"\"\"
        home_city: EntityText = None

    class TraveledTo(EdgeModel):
        \"\"\"A traveler visiting a destination.\"\"\"
        purpose: EntityText = None

    entity_types, edge_types = build_ontology(
        entities={"Traveler": Traveler},
        edges={
            "TRAVELED_TO": (
                TraveledTo,
                [EdgeSourceTarget(source_entity_type="Traveler", target_entity_type="Destination")],
            ),
        },
    )
    client.graph.set_ontology(graph_uuid, entity_types=entity_types, edge_types=edge_types)

The same output goes to ``client.project.set_ontology`` for the project default.

This is a plain function rather than a client subclass on purpose: the generated
clients expose their sub-clients as read-only properties and already define
``set_ontology``, so subclassing collides with both.
"""

import typing

from pydantic import BaseModel
from typing_extensions import Annotated

from .types import EdgeType, EntityProperty, EntityType

__all__ = [
    "EntityModel",
    "EdgeModel",
    "EntityText",
    "EntityInt",
    "EntityFloat",
    "EntityBoolean",
    "PropertyType",
    "build_ontology",
]


class PropertyType:
    """Marks a model field as an ontology property of a given wire type.

    The generated ``EntityPropertyType`` is a Literal union rather than an enum,
    so the wire value is carried here and read back off the field annotation.
    """

    def __init__(self, wire_type: str) -> None:
        self.wire_type = wire_type


# The four property types the API accepts. Declared once: a change to the wire
# spelling is a change here and nowhere else.
EntityText = Annotated[typing.Optional[str], PropertyType("text")]
EntityInt = Annotated[typing.Optional[int], PropertyType("int")]
EntityFloat = Annotated[typing.Optional[float], PropertyType("float")]
EntityBoolean = Annotated[typing.Optional[bool], PropertyType("boolean")]


class EntityModel(BaseModel):
    """Base class for an entity type. Subclass it and annotate the properties."""


class EdgeModel(BaseModel):
    """Base class for an edge type. Subclass it and annotate the properties."""


EdgeSpec = typing.Union[
    typing.Type[EdgeModel],
    typing.Tuple[typing.Type[EdgeModel], typing.List[typing.Any]],
]


def _description(model: type) -> str:
    """A type's description is its docstring, which is where a reader looks."""
    return (model.__doc__ or "").strip()


def _properties(model: typing.Type[BaseModel], label: str) -> typing.List[EntityProperty]:
    out: typing.List[EntityProperty] = []
    for name, field in model.model_fields.items():
        marker = next(
            (m for m in field.metadata if isinstance(m, PropertyType)),
            None,
        )
        if marker is None:
            raise ValueError(
                f"{label}.{name} is not an ontology property: annotate it with "
                f"EntityText, EntityInt, EntityFloat or EntityBoolean"
            )
        description = field.description or ""
        out.append(
            EntityProperty(name=name, type=marker.wire_type, description=description)
        )
    return out


def build_ontology(
    entities: typing.Optional[typing.Dict[str, typing.Type[EntityModel]]] = None,
    edges: typing.Optional[typing.Dict[str, EdgeSpec]] = None,
) -> typing.Tuple[typing.List[EntityType], typing.List[EdgeType]]:
    """Derive the entity and edge type lists from the given model classes.

    Pass the result to ``graph.set_ontology`` for one graph, or to
    ``project.set_ontology`` for the project default. v3 addressed many graphs in
    one call; v4 has one ontology endpoint per scope, so a caller targeting
    several graphs sends the same payload once per graph.
    """
    entity_types: typing.List[EntityType] = []
    for name, model in (entities or {}).items():
        entity_types.append(
            EntityType(
                name=name,
                description=_description(model),
                properties=_properties(model, name),
            )
        )

    edge_types: typing.List[EdgeType] = []
    for name, spec in (edges or {}).items():
        if isinstance(spec, tuple):
            edge_model, source_targets = spec
        else:
            edge_model, source_targets = spec, None
        edge_types.append(
            EdgeType(
                name=name,
                description=_description(edge_model),
                properties=_properties(edge_model, name),
                source_targets=list(source_targets) if source_targets else None,
            )
        )

    return entity_types, edge_types
