from typing import Optional, Type, Any, Dict, Sequence
from pydantic import BaseModel

from zep_cloud import ZepDataClass
from zep_cloud.core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zep_cloud.memory.client import MemoryClient as BaseMemoryClient, AsyncMemoryClient as AsyncBaseMemoryClient


class MemoryClient(BaseMemoryClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )


class AsyncMemoryClient(AsyncBaseMemoryClient):
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )

    async def extract_data_for_model(
            session_id: str,
            model: Type[BaseModel],
            client: Any,
            additional_data: Optional[Dict[str, Any]] = None,
            last_n_messages: Optional[int] = None,
            request_options: Optional[Dict[str, Any]] = None,
    ) -> BaseModel:
        zep_data_classes: Sequence[ZepDataClass] = [
            value.default for name, value in model.__fields__.items()
            if isinstance(value.default, ZepDataClass)
        ]

        extracted_data: Dict[str, str] = await client.memory.extract_session_data(
            session_id=session_id,
            zep_data_classes=zep_data_classes,
            last_n_messages=last_n_messages,
            request_options=request_options,
        )

        model_data: Dict[str, Any] = additional_data if additional_data else {}
        for field in model.__fields__.values():
            if isinstance(field.default, ZepDataClass):
                model_data[field.name] = extracted_data.get(field.default.name)

        return model(**model_data)