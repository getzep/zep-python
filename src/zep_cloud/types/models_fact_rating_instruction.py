# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .models_fact_rating_examples import ModelsFactRatingExamples


class ModelsFactRatingInstruction(UniversalBaseModel):
    examples: typing.Optional[ModelsFactRatingExamples] = pydantic.Field(default=None)
    """
    Examples is a list of examples that demonstrate how facts might be rated based on your instruction. You should provide
    an example of a highly rated example, a low rated example, and a medium (or in between example). For example, if you are rating
    based on relevance to a trip planning application, your examples might be:
    High: "Joe's dream vacation is Bali"
    Medium: "Joe has a fear of flying",
    Low: "Joe's favorite food is Japanese",
    """

    instruction: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string describing how to rate facts as they apply to your application. A trip planning application may
    use something like "relevancy to planning a trip, the user's preferences when traveling,
    or the user's travel history."
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
