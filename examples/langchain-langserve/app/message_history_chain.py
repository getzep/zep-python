import os
from typing import List, Tuple

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.runnables import (
    RunnableParallel,
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

from zep_python import ZepClient
from zep_python.langchain import ZepChatMessageHistory

ZEP_API_KEY = os.environ.get("ZEP_API_KEY")  # Required for Zep Cloud
ZEP_API_URL = os.environ.get(
    "ZEP_API_URL"
)  # only required if you're using Zep Open Source
if ZEP_API_KEY is None:
    raise ValueError(
        "ZEP_API_KEY is required for Zep Cloud. "
        "Remove this check if using Zep Open Source."
    )

zep = ZepClient(
    api_key=ZEP_API_KEY,
    api_url=ZEP_API_URL,  # only required if you're using Zep Open Source
)

# RAG answer synthesis prompt
template = """You are a 19 century poet, I want you to answer to the following question as one would:
    """
ANSWER_PROMPT = ChatPromptTemplate.from_messages(
    [
        ("system", template),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{question}"),
    ]
)


# User input
class ChatHistory(BaseModel):
    chat_history: List[Tuple[str, str]] = Field(..., extra={"widget": {"type": "chat"}})
    question: str
    session_id: str


_inputs = RunnableParallel(
    {
        "question": lambda x: x["question"],
        "chat_history": lambda x: x["chat_history"],
    },
).with_types(input_type=ChatHistory)

chain = RunnableWithMessageHistory(
    _inputs | ANSWER_PROMPT | ChatOpenAI() | StrOutputParser(),
    lambda session_id: ZepChatMessageHistory(
        session_id=session_id,  # This uniquely identifies the conversation
        zep_client=zep,
        memory_type="perpetual",
    ),
    input_messages_key="question",
    history_messages_key="chat_history",
)
