from enum import Enum
import typing
from pydantic import BaseModel, Field, WithJsonSchema, create_model
from typing_extensions import Annotated
from pydantic.json_schema import GenerateJsonSchema, JsonSchemaValue
from pydantic_core import core_schema

from zep_cloud import EntityEdgeSourceTarget, EntityType


class EntityPropertyType(Enum):
    Text = "Text"
    Int = "Int"
    Float = "Float"
    Boolean = "Boolean"

class EntityField(BaseModel):
    """Base class for entity field definitions"""
    description: str
    type: EntityPropertyType

class EntityBaseText(EntityField):
    """Entity field with Text type"""
    type: EntityPropertyType = EntityPropertyType.Text

class EntityBaseInt(EntityField):
    """Entity field with Int type"""
    type: EntityPropertyType = EntityPropertyType.Int

class EntityBaseFloat(EntityField):
    """Entity field with Float type"""
    type: EntityPropertyType = EntityPropertyType.Float

class EntityBaseBoolean(EntityField):
    """Entity field with Boolean type"""
    type: EntityPropertyType = EntityPropertyType.Boolean

# Annotated types for entity properties
# These types are used to define the properties of entity and edge models
# Each type includes:
# 1. The base Python type (str, int, float, bool)
# 2. A default value of None
# 3. Entity type information
# 4. JSON schema information for serialization

EntityText = Annotated[
    typing.Optional[str],
    Field(default=None),
    Field(..., entity_type=EntityPropertyType.Text),
    WithJsonSchema(EntityBaseText.model_json_schema(), mode="serialization"),
]

EntityInt = Annotated[
    typing.Optional[int],
    Field(default=None),
    Field(..., entity_type=EntityPropertyType.Int),
    WithJsonSchema(EntityBaseInt.model_json_schema(), mode="serialization"),
]

EntityFloat = Annotated[
    typing.Optional[float],
    Field(default=None),     
    Field(..., entity_type=EntityPropertyType.Float),
    WithJsonSchema(EntityBaseFloat.model_json_schema(), mode="serialization"),
]

EntityBoolean = Annotated[
    typing.Optional[bool],  
    Field(default=None),    
    Field(..., entity_type=EntityPropertyType.Boolean),
    WithJsonSchema(EntityBaseBoolean.model_json_schema(), mode="serialization"),
]

class _CustomJsonSchema(GenerateJsonSchema):
    """
    _CustomJsonSchema is a helper class that flattens and removes nullable as these aren't relevant to the entity schema
    and this simplifies server-side deserialization
    """
    def nullable_schema(self, schema: core_schema.CoreSchema) -> JsonSchemaValue:
        return self.generate_inner(schema["schema"])

class _BaseSchemaModel(BaseModel):
    """Base class for models that need custom JSON schema generation"""
    @classmethod
    def model_json_schema(cls, *args, **kwargs):
        kwargs["schema_generator"] = _CustomJsonSchema
        return super().model_json_schema(*args, **kwargs)

class EntityModel(_BaseSchemaModel):
    """Entity model for representing entity types"""
    pass

class EdgeModel(_BaseSchemaModel):
    """Edge model for representing edge types"""
    pass

def _model_to_api_schema_common(model_class: typing.Union["EntityModel", "EdgeModel"], name: str, is_edge: bool = False) -> dict[str, typing.Any]:
    """Common function to convert a Pydantic Model to a JSON schema for API EntityType or EdgeType"""

    schema = model_class.model_json_schema()

    # Define the type with proper typings for properties as a list of dictionaries
    result_type: dict[str, typing.Any] = {
        "name": name,
        "description": model_class.__doc__.strip() if model_class.__doc__ else "",
        "properties": []
    }

    # Add source_targets field for edge types
    if is_edge:
        result_type["source_targets"] = []

    for field_name, field_schema in schema.get("properties", {}).items():
        if "type" not in field_schema:
            continue

        property_type = field_schema.get("type")
        type_mapping = {
            "string": "Text",
            "integer": "Int",
            "number": "Float",
            "boolean": "Boolean"
        }

        if property_type in type_mapping:
            property_type = type_mapping[property_type]
        else:
            raise ValueError(f"Unsupported property type: {property_type}")

        description = field_schema.get("description", "")

        result_type["properties"].append({
            "name": field_name,
            "type": property_type,
            "description": description
        })

    return result_type


def entity_model_to_api_schema(model_class: "EntityModel", name: str) -> dict[str, typing.Any]:
    """Convert a Pydantic EntityModel to a JSON schema for API EntityType"""
    return _model_to_api_schema_common(model_class, name, is_edge=False)


def edge_model_to_api_schema(model_class: "EdgeModel", name: str) -> dict[str, typing.Any]:
    """Convert a Pydantic EdgeModel to a JSON schema for API EntityEdge"""
    return _model_to_api_schema_common(model_class, name, is_edge=True)


def convert_edge_schema_to_model(edge_schema: EntityType) -> (typing.Type[EdgeModel], list[EntityEdgeSourceTarget]):
    """
    Convert a JSON schema from Go EntityType back to a Pydantic EdgeModel class

    This function takes an EntityType object (which can represent an edge type in the API)
    and converts it to a Pydantic EdgeModel class. It maps the properties from the EntityType
    to the appropriate Pydantic field types (EntityText, EntityInt, etc.) and creates a new
    model class dynamically using create_model.

    Args:
        edge_schema: The EntityType object representing an edge type

    Returns:
        A tuple containing:
        - The dynamically created EdgeModel class
        - The list of source_targets from the edge_schema
    """

    edge_name = edge_schema.name
    properties = edge_schema.properties
    edge_description = edge_schema.description

    field_definitions: dict[str, typing.Any] = {}

    type_mapping = {
        'Text': EntityText,
        'Int': EntityInt,
        'Float': EntityFloat,
        'Boolean': EntityBoolean,
    }

    for prop in properties:
        prop_name = prop.name
        prop_type = prop.type
        prop_description = prop.description

        if not prop_name or not prop_type:
            continue

        field_type = type_mapping.get(prop_type)
        if not field_type:
            continue

        field_definitions[prop_name] = (
            field_type,
            Field(description=prop_description, default=None),
        )

    model_class = create_model(
        edge_name,
        __base__=EntityModel,
        __module__=EntityModel.__module__,
        __doc__=edge_description,
        **field_definitions,
    )

    return model_class, edge_schema.source_targets
