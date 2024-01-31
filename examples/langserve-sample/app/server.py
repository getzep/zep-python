from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from message_history import chain as message_history_chain
from rag_vector_store import chain as rag_vector_store_chain
app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
add_routes(app, message_history_chain, path="/message_history")
add_routes(app, rag_vector_store_chain, path="/rag_vector_store")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8050)
