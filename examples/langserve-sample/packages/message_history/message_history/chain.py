import os
from typing import List, Tuple, Optional, Any
from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnableSerializable,
    RunnableConfig,
    ConfigurableField
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from zep_python import ZepClient
from zep_python.langchain import ZepChatMessageHistory, ZepVectorStore

ZEP_API_KEY = os.environ.get("ZEP_API_KEY", None)  # Required for Zep Cloud
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
    # api_url=ZEP_API_URL,  # only required if you're using Zep Open Source
)

# RAG answer synthesis prompt
template = """You are a west coast rapper, I want you to rap the answer to the following question:
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
    ),
    input_messages_key="question",
    history_messages_key="chat_history",
)



