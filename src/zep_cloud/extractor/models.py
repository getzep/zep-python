import datetime
import typing
from enum import Enum

from pydantic import BaseModel, Field, WithJsonSchema
from typing_extensions import Annotated

from pydantic.json_schema import GenerateJsonSchema, JsonSchemaValue
from pydantic_core import core_schema


class ZepDataType(Enum):
    ZepText = "ZepText"
    ZepZipCode = "ZepZipCode"
    ZepDate = "ZepDate"
    ZepDateTime = "ZepDateTime"
    ZepEmail = "ZepEmail"
    ZepPhoneNumber = "ZepPhoneNumber"
    ZepFloat = "ZepFloat"
    ZepNumber = "ZepNumber"
    ZepRegex = "ZepRegex"


class ZepField(BaseModel):
    description: typing.Optional[str] = None


class ZepBaseText(ZepField):
    type: ZepDataType = ZepDataType.ZepText


ZepText = Annotated[
    typing.Optional[str],
    Field(..., zep_type=ZepDataType.ZepText),
    WithJsonSchema(ZepBaseText.model_json_schema(), mode="serialization"),
]


class ZepBaseNumber(ZepField):
    type: ZepDataType = ZepDataType.ZepFloat
    pattern: typing.Optional[str] = None


ZepNumber = Annotated[
    typing.Optional[int],
    Field(..., zep_type=ZepDataType.ZepNumber),
    WithJsonSchema(ZepBaseNumber.model_json_schema(), mode="serialization"),
]


class ZepBaseFloat(ZepField):
    type: ZepDataType = ZepDataType.ZepFloat


ZepFloat = Annotated[
    typing.Optional[float],
    Field(..., zep_type=ZepDataType.ZepFloat),
    WithJsonSchema(ZepBaseFloat.model_json_schema(), mode="serialization"),
]


class ZepBaseRegex(ZepField):
    type: ZepDataType = ZepDataType.ZepRegex


ZepRegex = Annotated[
    typing.Optional[str],
    Field(..., zep_type=ZepDataType.ZepRegex),
    WithJsonSchema(ZepBaseRegex.model_json_schema(), mode="serialization"),
]


class ZepBaseZipCode(ZepField):
    type: ZepDataType = ZepDataType.ZepZipCode


ZepZipCode = Annotated[
    typing.Optional[str],
    Field(..., zep_type=ZepDataType.ZepZipCode),
    WithJsonSchema(ZepBaseZipCode.model_json_schema(), mode="serialization"),
]


class ZepBaseDate(ZepField):
    type: ZepDataType = ZepDataType.ZepDate


ZepDate = Annotated[
    typing.Optional[datetime.date],
    Field(..., zep_type=ZepDataType.ZepDate),
    WithJsonSchema(ZepBaseDate.model_json_schema(), mode="serialization"),
]


class ZepBaseDateTime(ZepField):
    type: ZepDataType = ZepDataType.ZepDateTime


ZepDateTime = Annotated[
    typing.Optional[datetime.datetime],
    Field(..., zep_type=ZepDataType.ZepDateTime),
    WithJsonSchema(ZepBaseDateTime.model_json_schema(), mode="serialization"),
]


class ZepBaseEmail(ZepField):
    type: ZepDataType = ZepDataType.ZepEmail


ZepEmail = Annotated[
    typing.Optional[str],
    Field(..., zep_type=ZepDataType.ZepEmail),
    WithJsonSchema(ZepBaseEmail.model_json_schema(), mode="serialization"),
]


class ZepBasePhoneNumber(ZepField):
    type: ZepDataType = ZepDataType.ZepPhoneNumber


ZepPhoneNumber = Annotated[
    typing.Optional[str],
    Field(..., zep_type=ZepDataType.ZepPhoneNumber),
    WithJsonSchema(ZepBasePhoneNumber.model_json_schema(), mode="serialization"),
]


class _CustomJsonSchema(GenerateJsonSchema):
    """
    _CustomJsonSchema is a helper class that flattens and remove nullable as these aren't relevant to the Zep schema
    and this simplifies server-side deserialization
    """

    def nullable_schema(self, schema: core_schema.CoreSchema) -> JsonSchemaValue:
        return self.generate_inner(schema["schema"])


class ZepModel(BaseModel):
    @classmethod
    def model_json_schema(cls, *args, **kwargs):
        kwargs["schema_generator"] = _CustomJsonSchema
        return super().model_json_schema(*args, **kwargs)
