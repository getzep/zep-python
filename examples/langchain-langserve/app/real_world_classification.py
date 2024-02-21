import os
from langchain_core.output_parsers import StrOutputParser
from langchain.callbacks.tracers import ConsoleCallbackHandler
from langchain_core.prompts.prompt import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel
from langchain_core.runnables import (
    RunnableLambda,
    RunnablePassthrough,
    RunnableBranch
)
from langchain_core.runnables.history import RunnableWithMessageHistory
from zep_python import ZepClient
from zep_python.langchain import ZepChatMessageHistory
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.chat_models import ChatOpenAI
from langchain.agents import AgentType, initialize_agent, AgentExecutor
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from langchain_community.tools import WikipediaQueryRun
from langchain.agents import load_tools

ZEP_API_KEY = os.environ.get("ZEP_API_KEY")  # Required for Zep Cloud
ZEP_API_URL = os.environ.get(
    "ZEP_API_URL"
)  # only required if you're using Zep Open Source

llm = ChatOpenAI(temperature=0.0)
yahoo_chain = initialize_agent(
    [YahooFinanceNewsTool()],
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
)

stack_chain = initialize_agent(
    load_tools(["stackexchange"]),
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
)

wiki_chain = initialize_agent(
    [WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())],
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
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

wikipedia_search_prompt = PromptTemplate.from_template(
    """Please answer the question based only on the following context:
Context: {context}
Question: {question}
Answer:"""
)


def invoke_agent_executor(agent: AgentExecutor, x: any):
    result = agent.invoke(input=x["question"])
    return result["output"]


general_chain = PromptTemplate.from_template(
    """Please say that you cannot answer the question, be sarcastic:

Question: {question}
Answer:"""
)

branch = RunnableBranch(
    (lambda x: "research" in x["topic"].lower(), lambda x: invoke_agent_executor(wiki_chain, x)),
    (lambda x: "finance_news" in x["topic"].lower(), lambda x: invoke_agent_executor(yahoo_chain, x)),
    (lambda x: "dev_question" in x["topic"].lower(), lambda x: invoke_agent_executor(stack_chain, x)),
    general_chain | StrOutputParser(),
)


# User input
class UserInput(BaseModel):
    question: str
    session_id: str


def classify_session(session_id: str):
    result = zep.memory.classify_session(
        session_id,
        "intent",
        [
            "research",
            "dev_question",
            "finance_news",
            "none",
        ],
    )
    return result.class_


def invoke_chain(user_input: UserInput):
    result_chain = RunnableWithMessageHistory(
        RunnablePassthrough.assign(session_id=lambda x: user_input["session_id"])
        | {
            "question": lambda x: x["question"],
            "topic": lambda x: classify_session(x["session_id"]),
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
