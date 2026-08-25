import pytest
from pydantic import Field

from zep_cloud.ontology import (
    EdgeModel,
    EntityBoolean,
    EntityFloat,
    EntityInt,
    EntityModel,
    EntityText,
    build_ontology,
)
from zep_cloud.types import EdgeSourceTarget


class Traveler(EntityModel):
    """Someone who takes trips."""

    home_city: EntityText = None
    trips_taken: EntityInt = None
    loyalty_points: EntityFloat = None
    is_member: EntityBoolean = None


class TraveledTo(EdgeModel):
    """A traveler visiting a destination."""

    purpose: EntityText = Field(default=None, description="Why they went")


def test_entity_type_is_derived_from_the_class():
    entity_types, edge_types = build_ontology(entities={"Traveler": Traveler})
    assert edge_types == []
    (entity,) = entity_types
    assert entity.name == "Traveler"
    # The docstring is the description, which is where a reader looks.
    assert entity.description == "Someone who takes trips."
    assert [p.name for p in entity.properties] == [
        "home_city",
        "trips_taken",
        "loyalty_points",
        "is_member",
    ]


def test_each_annotation_maps_to_its_wire_type():
    entity_types, _ = build_ontology(entities={"Traveler": Traveler})
    assert [p.type for p in entity_types[0].properties] == [
        "text",
        "int",
        "float",
        "boolean",
    ]


def test_field_description_is_carried_through():
    _, edge_types = build_ontology(edges={"TRAVELED_TO": TraveledTo})
    (prop,) = edge_types[0].properties
    assert prop.description == "Why they went"


def test_edge_source_targets_are_passed_through():
    _, edge_types = build_ontology(
        edges={
            "TRAVELED_TO": (
                TraveledTo,
                [
                    EdgeSourceTarget(
                        source_entity_type="Traveler",
                        target_entity_type="Destination",
                    )
                ],
            )
        }
    )
    (target,) = edge_types[0].source_targets
    assert target.source_entity_type == "Traveler"
    assert target.target_entity_type == "Destination"


def test_an_edge_without_source_targets_omits_them():
    _, edge_types = build_ontology(edges={"TRAVELED_TO": TraveledTo})
    assert edge_types[0].source_targets is None


def test_an_unannotated_field_is_rejected_by_name():
    # Silently dropping a field would ship an ontology missing a property the
    # caller declared.
    class Bad(EntityModel):
        """Has a field that is not an ontology property."""

        oops: str = "x"

    with pytest.raises(ValueError, match="Bad.oops is not an ontology property"):
        build_ontology(entities={"Bad": Bad})


def test_empty_input_builds_empty_lists():
    assert build_ontology() == ([], [])
