import os
from operator import itemgetter
from typing import List, Tuple
import uuid
from langchain.globals import set_verbose
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
    RunnableBranch,
    ConfigurableFieldSpec,
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
    test_session_id = "ec0b3368269a41a4b8ba5bffe7270709"
    ZEP_API_KEY = os.environ.get("ZEP_API_KEY", None)  # Required for Zep Cloud

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
        chat_history: List[Tuple[str, str]] = Field(..., extra={"widget": {"type": "chat"}})
        question: str

    _inputs = RunnableParallel(
        {
            "question": lambda x: (print("whole x", x), x["question"]),
            "chat_history": lambda x: x["chat_history"],
            "context": _search_query
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
        {"question": "What did we talk about recently?"},
        config={
            "configurable": {
                "session_id": test_session_id,
            },
            "callbacks": [ConsoleCallbackHandler()]
        },
    )

    print(output)

if __name__ == "__main__":
    main()

