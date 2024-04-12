from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .base_memory.client import BaseMemoryClient
from .base_memory.types.base_memory_get_request_memory_type import BaseMemoryGetRequestMemoryType
from .types.memory import Memory

import typing


class MemoryClient(BaseMemoryClient):
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        super().__init__(
            client_wrapper=client_wrapper
        )

    # Memory APIs : Get Memory
    def get_memory(
            self,
            session_id: str,
            memory_type: typing.Optional[BaseMemoryGetRequestMemoryType] = None,
            lastn: typing.Optional[int] = None,
    ) -> Memory:
        """
        Retrieve memory for the specified session.

        Parameters
        ----------
        session_id : str
            The ID of the session for which to retrieve memory.
        memory_type : Optional[str]
            The type of memory to retrieve: perpetual, summary_retriever, or
                message_window. Defaults to perpetual.
        lastn : Optional[int], optional
            The number of most recent memory entries to retrieve. Defaults to None (all
            entries).

        Returns
        -------
        Memory
            A memory object containing a Summary, metadata, and list of Messages.

        Raises
        ------
        ValueError
            If the session ID is None or empty.
        APIError
            If the API response format is unexpected.
        """
        return self.get(
            session_id=session_id,
            memory_type=memory_type,
            lastn=lastn,
        )

    # Memory APIs : Add Memory
    def add_memory(self, session_id: str, memory_messages: Memory) -> None:
        """
        Add memory to the specified session.

        Parameters
        ----------
        session_id : str
            The ID of the session to which memory should be added.
        memory_messages : Memory
            A Memory object representing the memory messages to be added.

        Returns
        -------
        str
            The response text from the API.

        Raises
        ------
        ValueError
            If the session ID is None or empty.
        APIError
            If the API response format is unexpected.
        """
        return self.create(session_id=session_id, request=memory_messages)

    # Memory APIs : Delete Memory
    def delete_memory(self, session_id: str) -> str:
        """
        Delete memory for the specified session.

        Parameters
        ----------
        session_id : str
            The ID of the session for which memory should be deleted.

        Returns
        -------
        str
            The response text from the API.

        Raises
        ------
        ValueError
            If the session ID is None or empty.
        APIError
            If the API response format is unexpected.
        """
        return self.delete(session_id=session_id)
