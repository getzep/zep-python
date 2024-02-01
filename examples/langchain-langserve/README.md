# langserve-sample

## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management.

Follow these steps to install the project:

1. **Install Poetry**

   If you haven't installed Poetry yet, you can do so by following the instructions on the [official Poetry website](https://python-poetry.org/docs/#installation).

2. **Activate the Poetry environment**

    Use the following command to create a new virtual environment for the project:
    ```bash
    poetry shell
    ```

3. **Install environment dependencies**

    Use the following command to install the projects dependencies
    ```bash
    poetry install
    ```


## Setting Environment Variables

Environment variables are used to configure the application. Some of these are required for the application to run, while others are optional and can be used to enable additional features or change the default behavior.

1. **Required Variables**

   These variables must be set for the application to run:

   ```shell
   export OPENAI_API_KEY=<your-openai-api-key>
   export ZEP_API_KEY=<your-zep-project-api-key>
   ```

2. **Optional Variables**

   These variables are not required, but can be set to enable langserve:

   ```shell
   export LANGCHAIN_TRACING_V2=true
   export LANGCHAIN_API_KEY=<your-langchain-api-key>
   export LANGCHAIN_PROJECT=<your-project-name>  # If not specified, defaults to "default"
   ```

## Data Ingestion

The ingest.py script is used to create collections and populate them with documents from the article. To run this script, use the following command:

```
python app/ingest.py
```

## Starting the Server

To start the server, navigate to the application directory and run the following command:

```python
python app/server.py
```

This will start the server and listen for incoming connections.

## Running the Message History Chain

The `memory.py` script is used to create a session and populate it with a series of messages.

1. **Execute the script**

   ```bash
   python ../chat_history/memory.py
   ```

2. **Copy the Session ID**
   After running the script, you'll see an output similar to the following:

   ```bash
   ---Add Memory for Session: 0d1c45eaa52b4a2ba51988329c07e2eb
   ```
   The alphanumeric string after "Session:" is your Session ID. You'll need to copy this for future use.

   You will use this Session Id in your langserve playground.


## Running the Message History Chain

To run the message history chain, follow these steps:

1. **Start the server**

   Ensure that your server is running. If it's not, start it using the appropriate command.

2. **Navigate to the Playground**

   Open your web browser and navigate to the following URL:
   http://localhost:8050/message_history/playground

   This will take you to the playground where you can interact with the message history chain.
   Please note that you need to have the server running and accessible at `localhost:8050` for this to work.

## Running the RAG Vector Store Chain

To run the message history chain, follow these steps:

1. **Start the server**

   Ensure that your server is running. If it's not, start it using the appropriate command.

2. **Navigate to the Playground**

   Open your web browser and navigate to the following URL:
   http://localhost:8050/rag_vector_store/playground

   This will take you to the playground where you can interact with the RAG Vector Store chain.
   Please note that you need to have the server running and accessible at `localhost:8050` for this to work.

