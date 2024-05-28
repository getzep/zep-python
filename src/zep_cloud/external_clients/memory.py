from typing import Optional, Type, Any, Dict, Sequence, List
from pydantic import BaseModel
from ..core.pydantic_utilities import pydantic_v1

from zep_cloud import ZepDataClass
from zep_cloud.core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zep_cloud.memory.client import MemoryClient as BaseMemoryClient, AsyncMemoryClient as AsyncBaseMemoryClient


class MemoryClient(BaseMemoryClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )


def data_classes_from_pydantic_model(
        model: Type[BaseModel],
) -> List[ZepDataClass]:
    zep_data_classes = [
        value.default for name, value in model.__fields__.items()
        if isinstance(value.default, ZepDataClass)
    ]

    return zep_data_classes


class BaseDataExtractorModel(BaseModel):
    def update_with_extracted_data(self, data: Dict[str, Any]):
        for field, value in data.items():
            if hasattr(self, field):
                setattr(self, field, value)


class AsyncMemoryClient(AsyncBaseMemoryClient):
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )

    async def extract_session_data_from_model(
            self,
            session_id: str,
            model: Type[BaseDataExtractorModel],
            last_n_messages: Optional[int] = None) -> Dict[str, Any]:
        """
           Extracts session data from a specified model.

           This method uses the provided Pydantic model to extract data from the session. It then updates the model instance
           with the extracted data and returns it as a dictionary.

           Parameters
           ----------
           session_id : str
               The ID of the session from which to extract data.
           model : Type[BaseDataExtractorModel]
               The base model class to use for data extraction.
           last_n_messages : Optional[int]
               The number of most recent session messages to consider for data extraction. If not provided, all messages are considered.

           Returns
           -------
           Dict[str, Any]
               A dictionary representation of the updated model instance with the extracted data.
           """
        data_classes = data_classes_from_pydantic_model(
            model=model,
        )
        extracted_data = await self.extract_session_data(session_id, last_n_messages=last_n_messages,
                                                         zep_data_classes=data_classes)

        model_instance = model()
        model_instance.update_with_extracted_data(data=extracted_data)

        return model_instance.dict()
