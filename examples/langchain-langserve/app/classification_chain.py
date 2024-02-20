import os
from typing import List

from langchain.callbacks.tracers import ConsoleCallbackHandler
from langchain.schema import format_document
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel
from langchain_core.runnables import (
    ConfigurableField,
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
    RunnableBranch
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.runnables.utils import ConfigurableFieldSingleOption
from langchain_openai import ChatOpenAI

from zep_python import ZepClient
from zep_python.langchain import ZepChatMessageHistory, ZepVectorStore

from langchain_community.chat_models import ChatAnthropic

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

langchain_chain = (
        PromptTemplate.from_template(
            """You are an expert in langchain. \
    Always answer questions starting with "As Harrison Chase told me". \
    Respond to the following question:
    
    Question: {question}
    Answer:"""
        )
        | ChatAnthropic()
)
anthropic_chain = (
        PromptTemplate.from_template(
            """You are an expert in anthropic. \
    Always answer questions starting with "As Dario Amodei told me". \
    Respond to the following question:
    
    Question: {question}
    Answer:"""
        )
        | ChatAnthropic()
)
general_chain = (
        PromptTemplate.from_template(
            """Respond to the following question:
    
    Question: {question}
    Answer:"""
        )
        | ChatAnthropic()
)

branch = RunnableBranch(
    (lambda x: "anthropic" in x["topic"].lower(), anthropic_chain),
    (lambda x: "langchain" in x["topic"].lower(), langchain_chain),
    general_chain,
)

topic_classifier = (
        PromptTemplate.from_template(
            """Given the user question below, classify it as either being about `LangChain`, `Anthropic`, or `Other`.
    
    Do not respond with more than one word.
    
    <question>
    {question}
    </question>
    
    Classification:"""
        )
        | ChatAnthropic()
        | StrOutputParser()
)


# User input
class UserInput(BaseModel):
    question: str
    session_id: str

def invoke_chain(user_input: UserInput):
    result_chain = RunnableWithMessageHistory(
        RunnablePassthrough.assign(session_id=lambda x: user_input["session_id"])
        | {
            "topic": topic_classifier,
            "question": lambda x: x["question"],
            "topic_z": lambda x: zep.memory.class,
        } | branch,
        lambda session_id: ZepChatMessageHistory(
            session_id=session_id,
            zep_client=zep,
            memory_type="perpetual",
        ),
        input_messages_key="question",
        history_messages_key="chat_history",
        )

    return result_chain.invoke(
        user_input, config={"configurable": {"session_id": user_input["session_id"]}}
    )

chain = (
    RunnableLambda(invoke_chain)
    .with_types(input_type=UserInput)
    .with_config(callbacks=[ConsoleCallbackHandler()])
)