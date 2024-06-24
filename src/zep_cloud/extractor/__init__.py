# Zep Extraction requires Pydantic v2. If v2 is not installed, catch the error
# and set the variables to None


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
    ZepModel = PydanticV2Required
    ZepText = PydanticV2Required
    ZepNumber = PydanticV2Required
    ZepFloat = PydanticV2Required
    ZepRegex = PydanticV2Required
    ZepZipCode = PydanticV2Required
    ZepDate = PydanticV2Required
    ZepDateTime = PydanticV2Required
    ZepEmail = PydanticV2Required
    ZepPhoneNumber = PydanticV2Required

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
