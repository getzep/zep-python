import os
from typing import List

from langchain.callbacks.tracers import ConsoleCallbackHandler
from langchain.schema import format_document
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel
from langchain_core.runnables import (
    ConfigurableField,
    RunnableLambda,
    RunnableParallel,
)
from langchain_core.runnables.utils import ConfigurableFieldSingleOption
from langchain_openai import ChatOpenAI

from zep_cloud.client import Zep
from zep_cloud.langchain import ZepVectorStore

ZEP_COLLECTION_NAME = os.environ.get("ZEP_COLLECTION_NAME")
if ZEP_COLLECTION_NAME is None:
    raise ValueError("ZEP_COLLECTION_NAME is required for ingestion. ")

ZEP_API_KEY = os.environ.get("ZEP_API_KEY")  # Required for Zep Cloud
if ZEP_API_KEY is None:
    raise ValueError(
        "ZEP_API_KEY is required for Zep Cloud. "
        "Remove this check if using Zep Open Source."
    )

zep = Zep(
    api_key=ZEP_API_KEY,
)

# Initialize ZepVectorStore
vectorstore = ZepVectorStore(
    collection_name=ZEP_COLLECTION_NAME,
    api_key=ZEP_API_KEY,
)

# Zep offers native, hardware-accelerated MMR. Enabling this will improve
# the diversity of results, but may also reduce relevance. You can tune
# the lambda parameter to control the tradeoff between relevance and diversity.
# Enabling is a good default.
retriever = vectorstore.as_retriever().configurable_fields(
    search_type=ConfigurableFieldSingleOption(
        id="search_type",
        options={
            "Similarity": "similarity",
            "Similarity with MMR Reranking": "mmr",
        },
        default="Similarity with MMR Reranking",
        name="Search Type",
        description="Type of search to perform: 'similarity' or 'mmr'",
    ),
    search_kwargs=ConfigurableField(
        id="search_kwargs",
        name="Search kwargs",
        description=(
            "Specify 'k' for number of results to return and 'lambda_mult' for"
            " tuning MMR relevance vs diversity."
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
        ("user", "{question}"),
    ]
)

DEFAULT_DOCUMENT_PROMPT = PromptTemplate.from_template(template="{page_content}")


# User input
class UserInput(BaseModel):
    question: str


def _combine_documents(
    docs: List[Document],
    document_prompt: PromptTemplate = DEFAULT_DOCUMENT_PROMPT,
    document_separator: str = "\n\n",
):
    doc_strings = [format_document(doc, document_prompt) for doc in docs]
    return document_separator.join(doc_strings)


extract_question = RunnableLambda(lambda x: x["question"])

_inputs = RunnableParallel(
    {
        "question": lambda x: x["question"],
        "context": extract_question | retriever | _combine_documents,
    },
).with_types(input_type=UserInput)

chain = (_inputs | answer_prompt | ChatOpenAI() | StrOutputParser()).with_config(
    callbacks=[ConsoleCallbackHandler()]
)
