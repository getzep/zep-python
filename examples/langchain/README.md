# rag-conversation-zep

## Ingesting Documents into a Zep Collection

Run `python ingest.py` to ingest the test documents into a Zep Collection. Review the file to modify the Collection name and document source.

## Usage
Spin up a LangServe instance by running:

```shell
langchain serve
```

This will start the FastAPI app with a server is running locally at 
[http://localhost:8000](http://localhost:8000)

We can see all templates at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
We can access the playground at [http://127.0.0.1:8000/rag-conversation-zep/playground](http://127.0.0.1:8000/rag-conversation-zep/playground)