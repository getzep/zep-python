import os
from operator import itemgetter
from typing import List, Tuple

from langchain.schema import AIMessage, HumanMessage, format_document
from langchain_community.chat_models import ChatOpenAI
from langchain_core.documents import Document
from langchain_core.messages import BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.runnables import (
    ConfigurableField,
    RunnableBranch,
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.runnables.utils import ConfigurableFieldSingleOption

from zep_python import ZepClient
from zep_python.langchain import ZepChatMessageHistory, ZepVectorStore

ZEP_API_KEY = os.environ.get("ZEP_API_KEY", None)  # Required for Zep Cloud
ZEP_API_URL = os.environ.get(
    "ZEP_API_URL"
)  # only required if you're using Zep Open Source

ZEP_COLLECTION_NAME = os.environ.get("ZEP_COLLECTION", "langchaintest")

if ZEP_API_KEY is None:
    raise ValueError(
        "ZEP_API_KEY is required for Zep Cloud. "
        "Remove this check if using Zep Open Source."
    )

zep = ZepClient(
    api_key=ZEP_API_KEY,
    # api_url=ZEP_API_URL,  # only required if you're using Zep Open Source
)

# Initialize ZepVectorStore and ZepChatMessageHistory
vectorstore = ZepVectorStore(
    collection_name=ZEP_COLLECTION_NAME,
    zep_client=zep,
)
chat_history = ZepChatMessageHistory(
    session_id="langchain_test",  # This uniquely identifies the conversation
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
        default="mmr",
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
ANSWER_PROMPT = ChatPromptTemplate.from_messages(
    [
        ("system", template),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{question}"),
    ]
)

# Conversational Retrieval Chain
DEFAULT_DOCUMENT_PROMPT = PromptTemplate.from_template(template="{page_content}")


def _combine_documents(
    docs: List[Document],
    document_prompt: PromptTemplate = DEFAULT_DOCUMENT_PROMPT,
    document_separator: str = "\n\n",
):
    doc_strings = [format_document(doc, document_prompt) for doc in docs]
    return document_separator.join(doc_strings)


_search_query = RunnableLambda(
    lambda session_id: zep.memory.asynthesize_question(session_id=session_id),
)

chain_with_history = RunnableWithMessageHistory(
    _condense_chain,
    lambda session_id: chat_history,
    input_messages_key="question",
    history_messages_key="history",
)


# User input
class ChatHistory(BaseModel):
    chat_history: List[Tuple[str, str]] = Field(..., extra={"widget": {"type": "chat"}})
    question: str


_inputs = RunnableParallel(
    {
        "question": lambda x: x["question"],
        "chat_history": lambda x: _format_chat_history(x["chat_history"]),
        "context": _search_query | retriever | _combine_documents,
    }
).with_types(input_type=ChatHistory)

chain = _inputs | ANSWER_PROMPT | ChatOpenAI() | StrOutputParser()
