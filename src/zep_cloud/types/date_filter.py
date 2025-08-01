# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .comparison_operator import ComparisonOperator


class DateFilter(UniversalBaseModel):
    comparison_operator: ComparisonOperator = pydantic.Field()
    """
    Comparison operator for date filter
    """

    date: str = pydantic.Field()
    """
    Date to filter on
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
