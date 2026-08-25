import pytest
from pydantic import Field
from typing_extensions import Annotated

from zep_cloud.ontology import (
    EdgeModel,
    EntityBoolean,
    EntityFloat,
    EntityInt,
    EntityModel,
    EntityText,
    Identity,
    build_ontology,
)
from zep_cloud.types import EdgeSourceTarget


class Traveler(EntityModel):
    """Someone who takes trips."""

    home_city: Annotated[EntityText, Identity] = Field(
        default=None, description="The city they live in"
    )
    trips_taken: EntityInt = Field(default=None, description="How many trips they took")
    loyalty_points: EntityFloat = Field(default=None, description="Points earned")
    is_member: EntityBoolean = Field(default=None, description="Whether they joined")


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


def test_an_identity_annotated_property_is_listed_as_one():
    entity_types, _ = build_ontology(entities={"Traveler": Traveler})
    assert entity_types[0].identity_properties == ["home_city"]


def test_identity_properties_are_listed_in_declaration_order():
    class Place(EntityModel):
        """A place."""

        country: Annotated[EntityText, Identity] = Field(
            default=None, description="Its country"
        )
        region: EntityText = Field(default=None, description="Its region")
        city: Annotated[EntityText, Identity] = Field(
            default=None, description="Its city"
        )

    entity_types, _ = build_ontology(entities={"Place": Place})
    assert entity_types[0].identity_properties == ["country", "city"]


def test_a_type_with_no_identity_properties_omits_them():
    class Place(EntityModel):
        """A place."""

        country: EntityText = Field(default=None, description="Its country")

    entity_types, _ = build_ontology(entities={"Place": Place})
    assert entity_types[0].identity_properties is None


def test_an_edge_property_is_never_an_identity_property():
    # Only nodes are deduplicated, and EdgeType has no identity_properties to
    # carry one, so an Identity annotation on an edge is dropped rather than
    # failing to serialize.
    class Mentions(EdgeModel):
        """A mention."""

        note: Annotated[EntityText, Identity] = Field(
            default=None, description="The note"
        )

    _, edge_types = build_ontology(edges={"MENTIONS": Mentions})
    assert not hasattr(edge_types[0], "identity_properties")


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


def test_a_property_with_no_description_is_rejected_by_name():
    # The description goes into the extraction prompt; an empty one is accepted
    # by the write path and quietly degrades extraction.
    class Bad(EntityModel):
        """Has a property with no description."""

        country: EntityText = None

    with pytest.raises(ValueError, match="Bad.country needs a description"):
        build_ontology(entities={"Bad": Bad})


def test_a_type_with_no_docstring_is_rejected_by_name():
    class Bad(EntityModel):
        country: EntityText = Field(default=None, description="Its country")

    with pytest.raises(ValueError, match="Bad needs a docstring"):
        build_ontology(entities={"Bad": Bad})


def test_an_edge_with_no_docstring_is_rejected_by_name():
    # The name in the message is the ontology type name, which is what the
    # caller wrote and what the API will see, not the Python class name.
    class Bad(EdgeModel):
        note: EntityText = Field(default=None, description="The note")

    with pytest.raises(ValueError, match="BAD needs a docstring"):
        build_ontology(edges={"BAD": Bad})


def test_empty_input_builds_empty_lists():
    assert build_ontology() == ([], [])
