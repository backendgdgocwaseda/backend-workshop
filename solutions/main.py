from fastapi import FastAPI

from solutions.routers import notes, todos

app = FastAPI(
    title="Todo & Notes API (Complete Solution)",
    description="GDGoC Backend Workshop: Complete CRUD Todos + Notes APIRouter",
    version="0.1.0",
)


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the FastAPI Workshop! Visit /docs to get started."}


app.include_router(todos.router)
app.include_router(notes.router)
