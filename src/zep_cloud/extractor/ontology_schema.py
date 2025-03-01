from enum import Enum
from typing import Optional, Dict, Any
import typing
from pydantic import BaseModel, Field, WithJsonSchema 
from typing_extensions import Annotated
import json
from pydantic.json_schema import GenerateJsonSchema, JsonSchemaValue
from pydantic_core import core_schema
from pydantic import model_validator, create_model
from typing import ClassVar, Type, Optional
from zep_cloud.types.entity_node import EntityNode
import asyncio
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(
    dotenv_path=find_dotenv()
)  # load environment variables from .env file, if present

API_KEY = os.environ.get("ZEP_API_KEY") or "YOUR_API_KEY"

# Define the entity property types
class EntityPropertyType(Enum):
    Text = "Text"
    Number = "Number"
    Float = "Float"
    Boolean = "Boolean"

# Base field class
class EntityField(BaseModel):
    description: str
    # All fields are optional by default

# Define the base classes for each property type
class EntityBaseText(EntityField):
    type: EntityPropertyType = EntityPropertyType.Text

class EntityBaseNumber(EntityField):
    type: EntityPropertyType = EntityPropertyType.Number

class EntityBaseFloat(EntityField):
    type: EntityPropertyType = EntityPropertyType.Float

class EntityBaseBoolean(EntityField):
    type: EntityPropertyType = EntityPropertyType.Boolean

# Create the annotated types - all are Optional by default
EntityText = Annotated[
    typing.Optional[str],  # Always Optional
    Field(default=None),   # Always has default=None
    Field(..., entity_type=EntityPropertyType.Text),
    WithJsonSchema(EntityBaseText.model_json_schema(), mode="serialization"),
]

EntityNumber = Annotated[
    typing.Optional[int],  # Always Optional
    Field(default=None),   # Always has default=None
    Field(..., entity_type=EntityPropertyType.Number),
    WithJsonSchema(EntityBaseNumber.model_json_schema(), mode="serialization"),
]

EntityFloat = Annotated[
    typing.Optional[float],  # Always Optional
    Field(default=None),     # Always has default=None
    Field(..., entity_type=EntityPropertyType.Float),
    WithJsonSchema(EntityBaseFloat.model_json_schema(), mode="serialization"),
]

EntityBoolean = Annotated[
    typing.Optional[bool],  # Always Optional
    Field(default=None),    # Always has default=None
    Field(..., entity_type=EntityPropertyType.Boolean),
    WithJsonSchema(EntityBaseBoolean.model_json_schema(), mode="serialization"),
]

# Custom JSON schema generator
class _CustomJsonSchema(GenerateJsonSchema):
    """
    _CustomJsonSchema is a helper class that flattens and removes nullable as these aren't relevant to the entity schema
    and this simplifies server-side deserialization
    """
    def nullable_schema(self, schema: core_schema.CoreSchema) -> JsonSchemaValue:
        return self.generate_inner(schema["schema"])

# Base model class for entity types
class EntityModel(BaseModel):
    @classmethod
    def model_json_schema(cls, *args, **kwargs):
        kwargs["schema_generator"] = _CustomJsonSchema
        return super().model_json_schema(*args, **kwargs)

# Function to convert entity model to Go schema
def entity_model_to_go_schema(model_class: typing.Type[EntityModel], name: str) -> dict[str, typing.Any]:
    """Convert a Pydantic EntityModel to a JSON schema for Go EntityType"""
    import json
    
    # Get the JSON schema for the model
    schema = model_class.model_json_schema()
    
    # Create the entity type structure expected by Go
    entity_type = {
        "name": name,
        "properties": []
    }
    
    # Extract properties from the schema
    for field_name, field_schema in schema.get("properties", {}).items():
        # Skip fields that don't have a type
        if "type" not in field_schema:
            continue
        
        # Get the property type from the schema
        property_type = field_schema.get("type")
        
        # Map JSON schema types to EntityPropertyType values
        type_mapping = {
            "string": "Text",
            "integer": "Number",
            "number": "Float",
            "boolean": "Boolean"
        }
        
        # Convert the type if needed
        if property_type in type_mapping:
            property_type = type_mapping[property_type]
        
        # Get the description
        description = field_schema.get("description", "")
        
        # Add the property to the entity type
        entity_type["properties"].append({
            "name": field_name,
            "type": property_type,
            "description": description
        })
    
    return entity_type

# Function to convert Go schema back to entity model
def go_schema_to_entity_model(schema_json: str) -> typing.Type[EntityModel]:
    """Convert a JSON schema from Go EntityType back to a Pydantic EntityModel class"""
    import json
    from pydantic import create_model
    
    # Parse the JSON schema
    if isinstance(schema_json, str):
        schema = json.loads(schema_json)
    else:
        schema = schema_json
    
    # Get the entity name and properties
    entity_name = schema.get("name", "DynamicEntity")
    properties = schema.get("properties", [])
    
    # Create field definitions for the model
    field_definitions = {}
    
    # Map property types to field types
    type_mapping = {
        "Text": EntityText,
        "Number": EntityNumber,
        "Float": EntityFloat,
        "Boolean": EntityBoolean
    }
    
    # Create field definitions for each property
    for prop in properties:
        prop_name = prop.get("name")
        prop_type = prop.get("type")
        prop_description = prop.get("description", "")
        
        if not prop_name or not prop_type:
            continue
        
        # Get the field type
        field_type = type_mapping.get(prop_type)
        if not field_type:
            continue
        
        # Create the field definition
        field_definitions[prop_name] = (
            field_type,
            Field(description=prop_description, default=None)
        )
    
    # Create the model class
    model_class = create_model(
        entity_name,
        __base__=EntityModel,
        **field_definitions
    )
    
    return model_class

def entity_model_from_dict(entity_dict: typing.Dict[str, typing.Any]) -> typing.Type[EntityModel]:
    """
    Create an EntityModel class from a dictionary representation of an entity type.
    This is useful when working with API responses.
    
    Args:
        entity_dict: Dictionary representing the entity type
        
    Returns:
        A dynamically created Pydantic model class
    """
    # Simply pass the dictionary to go_schema_to_entity_model
    return go_schema_to_entity_model(entity_dict)

async def main() -> None:
    class Person(EntityModel):
        first_name: EntityText = Field(
            description="The person's first name",
            default=None
        )
        last_name: EntityText = Field(
            description="The person's last name",
            default=None
        )
        age: EntityNumber = Field(
            description="The person's age",
            default=None
        )
        height: EntityFloat = Field(
            description="The person's height in meters",
            default=None
        )
        is_active: EntityBoolean = Field(
            description="Whether the person is active",
            default=None
        )
        summary: EntityText = Field(
            description="A summary of the person",
            default=None
        )

    # Convert to Go-compatible schema
    schema_json = entity_model_to_go_schema(Person, "Person")
    print(schema_json)

    # Convert back to Pydantic model
    RecreatedPerson = go_schema_to_entity_model(schema_json)
    print("RecreatedPerson", RecreatedPerson)
    print("class name", RecreatedPerson.__name__)

    # Create an instance of the recreated model
    person = RecreatedPerson(
        first_name="John",
        last_name="Doe",
        age=30
    )

    print(entity_model_to_go_schema(RecreatedPerson, "Person"))

    print(f"Model name: {RecreatedPerson.__name__}")
    print(f"Fields: {list(RecreatedPerson.model_fields.keys())}")
    print(f"Instance: {person.model_dump()}")
    from zep_cloud.client import AsyncZep

    client = AsyncZep(
        api_key=API_KEY,
    )
    # nodes = await client.graph.node.get_by_group_id("playground_dataset:56c905a2243943fab23caa03752fbf7f")
    entity_node = await client.graph.node.get('7cb1ae6b-b026-4668-ab73-645d8d8c1bba')
    entity_as_person = Person(**entity_node.dict())
    print(f"Entity as person: {entity_as_person.model_dump()}")
    print(f"Entity as person summary: {entity_as_person}")
if __name__ == "__main__":
    asyncio.run(main())


