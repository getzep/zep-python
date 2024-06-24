# mypy: disable-error-code=no-redef

from typing import Type

# Zep Extraction requires Pydantic v2. If v2 is not installed, catch the error
# and set the variables to PydanticV2Required


class PydanticV2Required:
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Pydantic v2 is required to use this class.")


try:
    from zep_cloud.extractor.models import (
        ZepModel,
        ZepText,
        ZepNumber,
        ZepFloat,
        ZepRegex,
        ZepZipCode,
        ZepDate,
        ZepDateTime,
        ZepEmail,
        ZepPhoneNumber,
    )
except ImportError:
    ZepModel: Type = PydanticV2Required
    ZepText: Type = PydanticV2Required
    ZepNumber: Type = PydanticV2Required
    ZepFloat: Type = PydanticV2Required
    ZepRegex: Type = PydanticV2Required
    ZepZipCode: Type = PydanticV2Required
    ZepDate: Type = PydanticV2Required
    ZepDateTime: Type = PydanticV2Required
    ZepEmail: Type = PydanticV2Required
    ZepPhoneNumber: Type = PydanticV2Required

__all__ = [
    "ZepModel",
    "ZepText",
    "ZepNumber",
    "ZepFloat",
    "ZepRegex",
    "ZepZipCode",
    "ZepDate",
    "ZepDateTime",
    "ZepEmail",
    "ZepPhoneNumber",
]
