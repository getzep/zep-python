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
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.runnables.utils import ConfigurableFieldSingleOption
from langchain_openai import ChatOpenAI

from zep_python import ZepClient
from zep_python.langchain import ZepChatMessageHistory, ZepVectorStore

ZEP_API_KEY = os.environ.get("ZEP_API_KEY")  # Required for Zep Cloud
ZEP_API_URL = os.environ.get(
    "ZEP_API_URL"
)  # only required if you're using Zep Open Source

ZEP_COLLECTION_NAME = os.environ.get("ZEP_COLLECTION")
if ZEP_COLLECTION_NAME is None:
    raise ValueError(
        "ZEP_COLLECTION_NAME is required for ingestion. "
    )

if ZEP_API_KEY is None:
    raise ValueError(
        "ZEP_API_KEY is required for Zep Cloud. "
        "Remove this check if using Zep Open Source."
    )

zep = ZepClient(
    api_key=ZEP_API_KEY,
    api_url=ZEP_API_URL,  # only required if you're using Zep Open Source
)

# Initialize ZepVectorStore
vectorstore = ZepVectorStore(
    collection_name=ZEP_COLLECTION_NAME,
    zep_client=zep,
)

# Zep offers native, hardware-accelerated MMR. Enabling this will improve
# the diversity of results, but may also reduce relevance. You can tune
# the lambda parameter to control the tradeoff between relevance and diversity.
# Enabling is a good default.
retriever = vectorstore.as_retriever().configurable_fields(
    search_type=ConfigurableFieldSingleOption(
        id="search_type",
        options={"Similarity": "similarity", "Similarity with MMR Reranking": "mmr"},
        default="Similarity with MMR Reranking",
        name="Search Type",
        description="Type of search to perform: 'similarity' or 'mmr'",
    ),
    search_kwargs=ConfigurableField(
        id="search_kwargs",
        name="Search kwargs",
        description=(
            "Specify 'k' for number of results to return and 'lambda_mult' for tuning"
            " MMR relevance vs diversity."
        ),
    ),
)

# RAG answer synthesis prompt
template = """Answer the question based only on the following context:
    <context>
    {context}
    </context>"""
answer_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", template),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{question}"),
    ]
)

DEFAULT_DOCUMENT_PROMPT = PromptTemplate.from_template(template="{page_content}")


# User input
class UserInput(BaseModel):
    question: str
    session_id: str


def _combine_documents(
    docs: List[Document],
    document_prompt: PromptTemplate = DEFAULT_DOCUMENT_PROMPT,
    document_separator: str = "\n\n",
):
    doc_strings = [format_document(doc, document_prompt) for doc in docs]
    return document_separator.join(doc_strings)


_search_query = RunnableLambda(
    lambda x: zep.memory.synthesize_question(session_id=x["session_id"]),
)
_inputs = RunnableParallel(
    {
        "question": lambda x: x["question"],
        "session_id": lambda x: x["session_id"],
        "chat_history": lambda x: x["chat_history"],
        "context": _search_query | retriever | _combine_documents,
    },
)


def invoke_chain(user_input: UserInput):
    result_chain = RunnableWithMessageHistory(
        RunnablePassthrough.assign(session_id=lambda x: user_input["session_id"])
        | _inputs
        | answer_prompt
        | ChatOpenAI()
        | StrOutputParser(),
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
