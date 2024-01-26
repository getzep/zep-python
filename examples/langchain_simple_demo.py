import os
import uuid

from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

from zep_python import ZepClient
from zep_python.langchain.history import ZepChatMessageHistory
from zep_python.user import CreateUserRequest

load_dotenv()  # load environment variables from .env file, if present

API_KEY = os.environ.get("ZEP_API_KEY") or "YOUR_API_KEY"
API_URL = os.environ.get("ZEP_API_URL")  # only required if you're using Zep Open Source

OPENAI_API_KEY = os.environ.get(
    "OPENAI_API_KEY"
)  # ensure your environment contains a valid OpenAI API key


def main():
    zep = ZepClient(
        api_key=API_KEY,
        api_url=API_URL,  # only required if you're using Zep Open Source
    )
    user_id = uuid.uuid4().hex  # unique user id. can be any alphanum string
    session_id = (
        uuid.uuid4().hex
    )  # unique session id for this chat session. can be any alphanum string

    # Create a new user that we'll associate our chat session with
    # doing so allows us to organize our chat sessions by user, and delete all user data
    # when a user requests to be forgotten
    user_request = CreateUserRequest(
        user_id=user_id,
        email="jane@example.com",
        first_name="Jane",
        last_name="Smith",
        metadata={"foo": "bar"},
    )
    zep.user.add(user_request)

    zep_chat_history = ZepChatMessageHistory(
        zep_client=zep,
        session_id=session_id,
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You're an assistant who's good at {ability}"),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{question}"),
        ]
    )

    chain = prompt | ChatOpenAI(model="gpt-3.5-turbo-1106", api_key=OPENAI_API_KEY)

    chain_with_history = RunnableWithMessageHistory(
        chain,
        lambda session_id: zep_chat_history,
        input_messages_key="question",
        history_messages_key="history",
    )

    output = chain_with_history.invoke(
        {"ability": "math", "question": "What does cosine mean?"},
        config={"configurable": {"session_id": session_id}},
    )

    print(output)


if __name__ == "__main__":
    main()
