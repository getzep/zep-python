from dataclasses import Field
from typing import Optional, Type, Any, Dict, Sequence, List
from pydantic import BaseModel

from zep_cloud import ZepDataClass
from zep_cloud.core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from zep_cloud.memory.client import MemoryClient as BaseMemoryClient, AsyncMemoryClient as AsyncBaseMemoryClient


class BaseDataExtractorModel(BaseModel):
    data: Dict[str, Any] = {}

    def update_data(self, new_data: Dict[str, Any]):
        for key, value in new_data.items():
            self.data[key] = value

    def get_data(self) -> Dict[str, Any]:
        return self.data


def data_classes_from_pydantic_model(
        model: Type[BaseDataExtractorModel],
) -> List[ZepDataClass]:
    """
    Extracts ZepDataClass instances from a Pydantic model.

    This function iterates over the fields of the provided Pydantic model and collects all default values
    that are instances of ZepDataClass.

    Parameters
    ----------
    model : Type[BaseDataExtractorModel]
        The Pydantic model from which to extract ZepDataClass instances.

    Returns
    -------
    List[ZepDataClass]
        A list of ZepDataClass instances found in the model's default values.
    """
    zep_data_classes = [
        value.default for name, value in model.__fields__.items()
        if isinstance(value.default, ZepDataClass)
    ]

    return zep_data_classes


class MemoryClient(BaseMemoryClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )

    def extract_session_data_from_model(
            self,
            session_id: str,
            model_instance: BaseDataExtractorModel,
            last_n_messages: Optional[int] = None) -> BaseDataExtractorModel:
        """
        Extracts session data from a specified model instance.

        This method uses the provided Pydantic model instance to extract data from the session. It then updates the model instance
        with the extracted data and returns it.

        Parameters
        ----------
        session_id : str
            The ID of the session from which to extract data.
        model_instance : BaseDataExtractorModel
            The model instance to use for data extraction.
        last_n_messages : Optional[int]
            The number of most recent session messages to consider for data extraction. If not provided, all messages are considered.

        Returns
        -------
        BaseDataExtractorModel
            The updated model instance with the extracted data.
        """
        data_classes = data_classes_from_pydantic_model(
            model=type(model_instance),
        )
        extracted_data = self.extract_session_data(session_id, last_n_messages=last_n_messages, zep_data_classes=data_classes)

        model_instance.update_data(extracted_data)

        return model_instance


class AsyncMemoryClient(AsyncBaseMemoryClient):
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )

    async def extract_session_data_from_model(
            self,
            session_id: str,
            model_instance: BaseDataExtractorModel,
            last_n_messages: Optional[int] = None) -> BaseDataExtractorModel:
        """
        Extracts session data from a specified model instance.

        This method uses the provided Pydantic model instance to extract data from the session. It then updates the model instance
        with the extracted data and returns it.

        Parameters
        ----------
        session_id : str
            The ID of the session from which to extract data.
        model_instance : BaseDataExtractorModel
            The model instance to use for data extraction.
        last_n_messages : Optional[int]
            The number of most recent session messages to consider for data extraction. If not provided, all messages are considered.

        Returns
        -------
        BaseDataExtractorModel
            The updated model instance with the extracted data.
        """
        data_classes = data_classes_from_pydantic_model(
            model=type(model_instance),
        )
        extracted_data = await self.extract_session_data(session_id, last_n_messages=last_n_messages,
                                                         zep_data_classes=data_classes)

        model_instance.update_data(extracted_data)

        return model_instance
