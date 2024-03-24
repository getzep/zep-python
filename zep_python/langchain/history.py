from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional, Union

from zep_python import API_URL, NotFoundError, ZepClient
from zep_python.memory.models import Memory, Message
from zep_python.message.models import get_zep_message_role_type

try:
    from langchain_core.chat_history import BaseChatMessageHistory
    from langchain_core.messages import (
        AIMessage,
        BaseMessage,
        HumanMessage,
        SystemMessage,
    )
except ImportError:
    raise ImportError(
        "Could not import langchain-core package. "
        "Please install it with `pip install langchain-core`."
    )

logger = logging.getLogger(__name__)


class ZepChatMessageHistory(BaseChatMessageHistory):
    """
    LangChain Chat message history that uses Zep as a backend.

    Attributes
    ----------
    session_id : str
        The unique identifier of the session.
    zep_client : ZepClient
        The Zep client used for making API requests.
        Pass in this rather than the API key and URL.
    api_url : str
        The Zep API service URL. Not required if using Zep Cloud.
    api_key : str
        The Zep API key. Not required if using Zep Open Source.
    memory_type : str
        The type of memory to use. Can be "perpetual", "summary_retrieval",
        or "message_window". Defaults to "perpetual".
    summary_instruction : Optional[str]
        Additional instructions for generating dialog summaries.
    """

    def __init__(
        self,
        session_id: str,
        zep_client: Optional[ZepClient] = None,
        api_url: Optional[str] = API_URL,
        api_key: Optional[str] = None,
        memory_type: Optional[str] = None,
        ai_prefix: Optional[str] = None,
        human_prefix: Optional[str] = None,
        summary_instruction: Optional[str] = None,
    ) -> None:
        if zep_client is None:
            self._client = ZepClient(api_url=api_url, api_key=api_key)
        else:
            self._client = zep_client

        self.session_id = session_id
        self.memory_type = memory_type or "perpetual"

        self.ai_prefix = ai_prefix or "ai"
        self.human_prefix = human_prefix or "human"
        self.summary_instruction = summary_instruction

    @property
    def messages(self) -> List[BaseMessage]:  # type: ignore
        """Retrieve messages from Zep memory"""

        zep_memory: Optional[Memory] = self._get_memory()
        if not zep_memory:
            return []

        messages: List[BaseMessage] = []
        # Extract facts and summary, if present, and messages
        if zep_memory.facts:
            messages.append(SystemMessage(content="\n".join(zep_memory.facts)))

        if zep_memory.summary:
            if len(zep_memory.summary.content) > 0:
                messages.append(SystemMessage(content=zep_memory.summary.content))

        if zep_memory.messages:
            for msg in zep_memory.messages:
                metadata = {
                    "uuid": msg.uuid,
                    "created_at": msg.created_at,
                    "token_count": msg.token_count,
                    "metadata": msg.metadata,
                }
                message_class = AIMessage if msg.role == "ai" else HumanMessage
                messages.append(
                    message_class(content=msg.content, additional_kwargs=metadata)
                )

        return messages

    @property
    def zep_messages(self) -> Union[List[Message], None]:
        """Retrieve summary from Zep memory"""
        zep_memory: Optional[Memory] = self._get_memory()
        if not zep_memory:
            return []

        return zep_memory.messages

    @property
    def zep_summary(self) -> Optional[str]:
        """Retrieve summary from Zep memory"""
        zep_memory: Optional[Memory] = self._get_memory()
        if not zep_memory or not zep_memory.summary:
            return None

        return zep_memory.summary.content

    def _get_memory(self) -> Optional[Memory]:
        """Retrieve memory from Zep"""
        try:
            zep_memory: Memory = self._client.memory.get_memory(
                self.session_id, self.memory_type
            )
        except NotFoundError:
            logger.warning(
                f"Session {self.session_id} not found in Zep. Returning None"
            )
            return None
        return zep_memory

    def add_user_message(  # type: ignore
        self, message: str, metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        """Convenience method for adding a human message string to the store.

        Args:
            message: The string contents of a human message.
            metadata: Optional metadata to attach to the message.
        """
        from langchain_core.messages import HumanMessage

        self.add_message(HumanMessage(content=message), metadata=metadata)

    def add_ai_message(  # type: ignore
        self, message: str, metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        """Convenience method for adding an AI message string to the store.

        Args:
            message: The string contents of an AI message.
            metadata: Optional metadata to attach to the message.
        """
        from langchain_core.messages import AIMessage

        self.add_message(AIMessage(content=message), metadata=metadata)

    def add_message(
        self, message: BaseMessage, metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        """Append the message to the Zep memory history"""

        if message.content is None:
            raise ValueError("Message content cannot be None")

        if isinstance(message.content, list):
            raise ValueError("Message content cannot be a list")

        if message.type == "ai":
            message.name = self.ai_prefix
        elif message.type == "human":
            message.name = self.human_prefix

        zep_message = Message(
            content=message.content,
            # If name is not set, use type as role
            role=message.name or message.type,
            role_type=get_zep_message_role_type(message.type),
            metadata=metadata,
        )
        zep_memory = Memory(
            messages=[zep_message], summary_instruction=self.summary_instruction
        )

        self._client.memory.add_memory(self.session_id, zep_memory)

    def clear(self) -> None:
        """Clear session memory from Zep. Note that Zep is long-term storage for memory
        and this is not advised unless you have specific data retention requirements.
        """
        try:
            self._client.memory.delete_memory(self.session_id)
        except NotFoundError:
            logger.warning(
                f"Session {self.session_id} not found in Zep. Skipping delete."
            )
