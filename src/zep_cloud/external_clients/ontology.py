from enum import Enum
import typing
from pydantic import BaseModel, Field, WithJsonSchema 
from typing_extensions import Annotated
from pydantic.json_schema import GenerateJsonSchema, JsonSchemaValue
from pydantic_core import core_schema

class EntityPropertyType(Enum):
    Text = "Text"
    Number = "Number"
    Float = "Float"
    Boolean = "Boolean"

class EntityField(BaseModel):
    description: str

class EntityBaseText(EntityField):
    type: EntityPropertyType = EntityPropertyType.Text

class EntityBaseNumber(EntityField):
    type: EntityPropertyType = EntityPropertyType.Number

class EntityBaseFloat(EntityField):
    type: EntityPropertyType = EntityPropertyType.Float

class EntityBaseBoolean(EntityField):
    type: EntityPropertyType = EntityPropertyType.Boolean

EntityText = Annotated[
    typing.Optional[str],
    Field(default=None),
    Field(..., entity_type=EntityPropertyType.Text),
    WithJsonSchema(EntityBaseText.model_json_schema(), mode="serialization"),
]

EntityNumber = Annotated[
    typing.Optional[int],
    Field(default=None),
    Field(..., entity_type=EntityPropertyType.Number),
    WithJsonSchema(EntityBaseNumber.model_json_schema(), mode="serialization"),
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

class EntityModel(BaseModel):
    @classmethod
    def model_json_schema(cls, *args, **kwargs):
        kwargs["schema_generator"] = _CustomJsonSchema
        return super().model_json_schema(*args, **kwargs)

def entity_model_to_api_schema(model_class: typing.Type[EntityModel], name: str) -> dict[str, typing.Any]:
    """Convert a Pydantic EntityModel to a JSON schema for Go EntityType"""
    
    schema = model_class.model_json_schema()
    
    entity_type = {
        "name": name,
        "properties": []
    }
    
    for field_name, field_schema in schema.get("properties", {}).items():
        if "type" not in field_schema:
            continue
        
        property_type = field_schema.get("type")
        
        type_mapping = {
            "string": "Text",
            "integer": "Number",
            "number": "Float",
            "boolean": "Boolean"
        }
        
        if property_type in type_mapping:
            property_type = type_mapping[property_type]
        
        description = field_schema.get("description", "")
        
        entity_type["properties"].append({
            "name": field_name,
            "type": property_type,
            "description": description
        })
    
    return entity_type

