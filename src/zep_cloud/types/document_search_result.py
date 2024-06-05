# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1


class DocumentSearchResult(pydantic_v1.BaseModel):
    content: typing.Optional[str] = None
    created_at: typing.Optional[str] = None
    document_id: typing.Optional[str] = None
    embedding: typing.Optional[typing.List[float]] = None
    is_embedded: typing.Optional[bool] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    score: typing.Optional[float] = None
    updated_at: typing.Optional[str] = None
    uuid_: typing.Optional[str] = pydantic_v1.Field(alias="uuid", default=None)

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
