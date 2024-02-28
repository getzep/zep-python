import os

from langchain.callbacks.tracers import ConsoleCallbackHandler
from langchain_community.chat_models import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory

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


def classify_session(session_id: str):
    result = zep.memory.classify_session(
        session_id, "intent", ["langchain", "anthropic", "none"], persist=True
    )
    return result.class_


def invoke_chain(user_input: UserInput):
    result_chain = RunnableWithMessageHistory(
        RunnablePassthrough.assign(session_id=lambda x: user_input["session_id"])
        | {
            "question": lambda x: x["question"],
            "topic": lambda x: classify_session(x["session_id"]),
        }
        | branch,
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
