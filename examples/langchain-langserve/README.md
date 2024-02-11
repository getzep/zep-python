# LangServe Example

This README provides a comprehensive guide to setting up and running the Zep LangServe Example project.

## Installation

This project uses [Poetry](https://python-poetry.org/) for managing dependencies.

To get started with the installation, follow these steps:

1. **Install Poetry**

   Haven't got Poetry on your machine yet? You can install it by following the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).

2. **Create the Poetry Environment and Install Dependencies**
    Run the command below to create a new virtual environment for the project:
    ```bash
    poetry install
    ```

3. **Activate the Poetry Environment**

    Use the following command to activate the Poetry environment.
    ```bash
    poetry shell
    ```


## Setting Up Environment Variables

To run the LangServe Sample App, please set the following environment variables:

```dotenv
# Please use examples/.env.example as a template for .env file

# Required
ZEP_API_KEY=<zep-project-api-key># Your Zep Project API Key
ZEP_COLLECTION=<zep-collection-name># used in ingestion script and in vector store examples
OPENAI_API_KEY=<openai-api-key># Your OpenAI API Key

# Optional (If you want to use langsmith with LangServe Sample App)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=<your-langchain-api-key>
LANGCHAIN_PROJECT=<your-langchain-project-name># If not specified, defaults to "default"
```

## Data Ingestion

The `ingest.py` script creates Document Collections and populates them with content from a web article. To use this script, simply run the following command:

```bash
python app/ingest.py
```

## Starting the Server

To start the server, navigate to the application directory and run the following command:

```bash
python app/server.py
```

This will start the server and listen for incoming connections.

## Running the Message History Chain

The `memory.py` script is used to create a session and populate it with a series of Messages.

1. **Execute the script**

   ```bash
   python ../chat_history/memory.py
   ```

2. **Copy the Session ID**
   Once you've executed the script, you'll see an output that looks something like this:

   ```bash
   ---Add Memory for Session: 0d1c45eaa52b4a2ba51988329c07e2eb
   ```
   The alphanumeric sequence following "Session:" is your Session ID. Make sure to copy it for later use.

   This Session ID will be needed when you're working in the LangServe Playground.


## Running the Message History Chain

Here's how to get the Message History chain up and running:

1. **Start the Server**

   First, make sure your server is up and running. If it isn't, start it with the command provided in the setup instructions.

2. **Head to the Playground**

   Next, open your web browser and go to:
   http://localhost:8050/message_history/playground

   You'll land on the playground page, where you can start interacting with the Message History chain. 
   Just a heads-up, you'll need the server to be live and reachable at `http://localhost:8050` for this to work.

## Running the RAG Vector Store Chain

To get the RAG Vector Store chain up and running, follow these steps:

1. **Start the Server**

   Make sure your server is up and running. If not, start it with the command provided in the setup instructions.

2. **Head to the Playground**

   Pop open your web browser and navigate to:
   http://localhost:8050/rag_vector_store/playground

   You'll land in the playground, ready to interact with the RAG Vector Store chain. Remember, your server needs to be live and accessible at `http://localhost:8050` for this to work.

   This RAG uses the content we ingested above, which is an article on Leonard Bernstein found here: https://en.wikipedia.org/wiki/Leonard_Bernstein.

   Try asking: "Who was a famous American conductor?"

## Running the RAG Vector Store + Message History Chain

To get the message history chain up and running, just follow these simple steps:

1. **Start the Server**

   Make sure your server is up and running. If not, go ahead and start it with the command provided in the setup instructions.

2. **Head to the Playground**

   Launch your web browser and head over to:
   http://localhost:8050/message_history_vector_store/playground
   Here, you'll need to input a Session ID and a question into the playground.

   This step will bring you to the playground, where you can interact with the RAG Vector Store chain. Remember, your server needs to be live and reachable at `http://localhost:8050` for this to work.

   This RAG uses the content we ingested above, which is an article on Leonard Bernstein found here: https://en.wikipedia.org/wiki/Leonard_Bernstein.

   Give it a try by asking, "Who was a famous American conductor?" Then, dive into a conversation about Leonard Bernstein's life. You'll be able to view the message history and the summary in the [Zep web app's](https://app.getzep.com/) session details page.
