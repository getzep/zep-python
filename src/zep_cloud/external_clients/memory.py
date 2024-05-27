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


class AsyncMemoryClient(AsyncBaseMemoryClient):
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )

    async def extract_session_data_from_model(
            self,
            session_id: str,
            model: Type[BaseModel],
            last_n_messages: Optional[int] = None):

        data_classes = data_classes_from_pydantic_model(
            model=model,
        )

        print(f"data_classes: {data_classes}")

        extracted_data = await self.extract_session_data(session_id, last_n_messages=last_n_messages, zep_data_classes=data_classes)

        model.update_with_extracted_data(data=extracted_data)

        return model
