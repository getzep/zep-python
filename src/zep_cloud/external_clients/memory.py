import datetime
import json
import typing
from zep_cloud.core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zep_cloud.memory.client import (
    MemoryClient as BaseMemoryClient,
    AsyncMemoryClient as AsyncBaseMemoryClient,
)

from zep_cloud.extractor.models import ZepModel


class MemoryClient(BaseMemoryClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)

    def extract(
        self,
        session_id: str,
        model: ZepModel,
        current_date_time: typing.Optional[datetime.datetime] = None,
        last_n: typing.Optional[int] = 4,
        validate: typing.Optional[bool] = False,
    ):
        model_schema = json.dumps(model.model_json_schema())

        result = self.extract_data(
            session_id=session_id,
            model_schema=model_schema,
            validate=validate,
            last_n=last_n,
            current_date_time=current_date_time,
        )

        return model.model_validate(result)


class AsyncMemoryClient(AsyncBaseMemoryClient):
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)

    async def extract(
        self,
        session_id: str,
        model: ZepModel,
        current_date_time: typing.Optional[datetime.datetime] = None,
        last_n: typing.Optional[int] = 4,
        validate: typing.Optional[bool] = False,
    ):
        model_schema = json.dumps(model.model_json_schema())

        result = await self.extract_data(
            session_id=session_id,
            model_schema=model_schema,
            validate=validate,
            last_n=last_n,
            current_date_time=current_date_time,
        )

        result = {k: v for k, v in result.items() if v is not (None or "")}

        print(result)

        return model.model_validate(result)
