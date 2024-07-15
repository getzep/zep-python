import datetime
import json
import typing
from packaging import version

import pydantic

from zep_cloud.core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zep_cloud.memory.client import (
    AsyncMemoryClient as AsyncBaseMemoryClient,
)
from zep_cloud.memory.client import (
    MemoryClient as BaseMemoryClient,
)

if typing.TYPE_CHECKING:
    from zep_cloud.extractor.models import ZepModel

MIN_PYDANTIC_VERSION = "2.0"


class MemoryClient(BaseMemoryClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)

    def extract(
        self,
        session_id: str,
        model: "ZepModel",
        current_date_time: typing.Optional[datetime.datetime] = None,
        last_n: int = 4,
        validate: bool = False,
    ):
        """Extracts structured data from a session based on a ZepModel schema.
        This method retrieves data based on a given model and session details.
        It then returns the extracted and validated data as an instance of the given ZepModel.

        Parameters
        ----------
        session_id: str
            Session ID.
        model: ZepModel
            An instance of a ZepModel subclass defining the expected data structure and field types.
        current_date_time: typing.Optional[datetime.datetime]
            Your current date and time in ISO 8601 format including timezone.
            This is used for determining relative dates.
        last_n: typing.Optional[int]
            The number of messages in the chat history from which to extract data.
        validate: typing.Optional[bool]
            Validate that the extracted data is present in the dialog and correct per the field description.
            Mitigates hallucination, but is slower and may result in false negatives.

        Returns
        -------
        ZepModel: An instance of the provided ZepModel subclass populated with the
            extracted and validated data.

        Examples
        --------
        class CustomerInfo(ZepModel):
            name: Optional[ZepText] = Field(description="Customer name", default=None)
            email: Optional[ZepEmail] = Field(description="Customer email", default=None)
            signup_date: Optional[ZepDate] = Field(description="Customer Sign up date", default=None)

        client = AsyncMemoryClient(...)

        customer_data = await client.memory.extract(
            session_id="session123",
            model=CustomerInfo(),
            current_date_time=datetime.datetime.now(),  # Filter data up to now
        )

        print(customer_data.name)  # Access extracted and validated customer name
        """

        if version.parse(pydantic.VERSION) < version.parse(MIN_PYDANTIC_VERSION):
            raise RuntimeError(
                f"Pydantic version {MIN_PYDANTIC_VERSION} or greater is required."
            )

        model_schema = json.dumps(model.model_json_schema())

        result = self.extract_data(
            session_id=session_id,
            model_schema=model_schema,
            validate=validate,
            last_n=last_n,
            current_date_time=(
                current_date_time.isoformat() if current_date_time else None
            ),
        )

        return model.model_validate(result)


class AsyncMemoryClient(AsyncBaseMemoryClient):
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)

    async def extract(
        self,
        session_id: str,
        model: "ZepModel",
        current_date_time: typing.Optional[datetime.datetime] = None,
        last_n: int = 4,
        validate: bool = False,
    ):
        """Extracts structured data from a session based on a ZepModel schema.
        This method retrieves data based on a given model and session details.
        It then returns the extracted and validated data as an instance of the given ZepModel.

        Parameters
        ----------
        session_id: str
            Session ID.
        model: ZepModel
            An instance of a ZepModel subclass defining the expected data structure and field types.
        current_date_time: typing.Optional[datetime.datetime]
            Your current date and time in ISO 8601 format including timezone.
            This is used for determining relative dates.
        last_n: typing.Optional[int]
            The number of messages in the chat history from which to extract data.
        validate: typing.Optional[bool]
            Validate that the extracted data is present in the dialog and correct per the field description.
            Mitigates hallucination, but is slower and may result in false negatives.

        Returns
        -------
        ZepModel: An instance of the provided ZepModel subclass populated with the
            extracted and validated data.

        Examples
        --------
        class CustomerInfo(ZepModel):
            name: Optional[ZepText] = Field(description="Customer name", default=None)
            name: Optional[ZepEmail] = Field(description="Customer email", default=None)
            signup_date: Optional[ZepDate] = Field(description="Customer Sign up date", default=None)

        client = AsyncMemoryClient(...)

        customer_data = await client.memory.extract(
            session_id="session123",
            model=CustomerInfo(),
            current_date_time=datetime.datetime.now(),  # Filter data up to now
        )

        print(customer_data.name)  # Access extracted and validated customer name
        """

        if version.parse(pydantic.VERSION) < version.parse(MIN_PYDANTIC_VERSION):
            raise RuntimeError(
                f"Pydantic version {MIN_PYDANTIC_VERSION} or greater is required."
            )

        model_schema = json.dumps(model.model_json_schema())

        result = await self.extract_data(
            session_id=session_id,
            model_schema=model_schema,
            validate=validate,
            last_n=last_n,
            current_date_time=(
                current_date_time.isoformat() if current_date_time else None
            ),
        )

        return model.model_validate(result)
