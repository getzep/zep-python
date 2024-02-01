import os
from typing import List, Tuple

from langchain.callbacks.tracers import ConsoleCallbackHandler
from langchain.schema import AIMessage, HumanMessage, format_document
from langchain_core.documents import Document
from langchain_core.messages import BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
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


def main():
    test_session_id = "52c57a03e61041b9b5f8c314d03b380e"
    ZEP_API_KEY = os.environ.get("ZEP_API_KEY", None)  # Required for Zep Cloud

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
    print("ZepVectorStore initialized")
    chat_history = ZepChatMessageHistory(
        session_id=test_session_id,  # This uniquely identifies the conversation
        zep_client=zep,
    )

    print("ZepVectorStore and ZepChatMessageHistory initialized")

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
        lambda session_id: zep.memory.synthesize_question(session_id=test_session_id),
    )

    # Condense a chat history and follow-up question into a standalone question
    _template = """Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question, in its original language.
    Chat History:
    {chat_history}
    Follow Up Input: {question}
    Standalone question:"""  # noqa: E501
    CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)

    def _format_chat_history(chat_history: List[Tuple[str, str]]) -> List[BaseMessage]:
        print("_format_chat_history chat_history", chat_history)
        buffer: List[BaseMessage] = []
        for human, ai in chat_history:
            buffer.append(HumanMessage(content=human))
            buffer.append(AIMessage(content=ai))
        return buffer

    _condense_chain = (
        RunnablePassthrough.assign(
            chat_history=lambda x: _format_chat_history(x["chat_history"])
        )
        | CONDENSE_QUESTION_PROMPT
        | ChatOpenAI(temperature=0)
        | StrOutputParser()
    )

    # User input
    class ChatHistory(BaseModel):
        chat_history: List[Tuple[str, str]] = Field(
            ..., extra={"widget": {"type": "chat"}}
        )
        question: str
        session_id: str

    _inputs = RunnableParallel(
        {
            "question": lambda x: (print("whole x", x), x["question"]),
            "chat_history": lambda x: x["chat_history"],
            "session_id": lambda x: x["session_id"],
            "context": _search_query | retriever | _combine_documents,
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

    output = chain.invoke(
        {
            "session_id": test_session_id,
            "question": "What did japanese scientists discover?",
        },
        config={
            "configurable": {
                "session_id": test_session_id,
            },
            "callbacks": [ConsoleCallbackHandler()],
        },
    )

    print(output)


if __name__ == "__main__":
    main()
