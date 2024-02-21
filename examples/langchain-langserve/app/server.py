from dotenv import find_dotenv, load_dotenv

load_dotenv(dotenv_path=find_dotenv())

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from message_history_chain import chain as message_history_chain
from message_history_vector_store_chain import (
    chain as message_history_vector_store_chain,
)
from rag_vector_store_chain import chain as rag_vector_store_chain
from classification_chain import chain as classification_chain
from real_world_classification import chain as real_world_classification_chain
app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


add_routes(app, message_history_chain, path="/message_history")
add_routes(app, rag_vector_store_chain, path="/rag_vector_store")
add_routes(
    app, message_history_vector_store_chain, path="/message_history_vector_store"
)
add_routes(app, classification_chain, path="/classification")
add_routes(app, real_world_classification_chain, path="/real_world_classification")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8050)
