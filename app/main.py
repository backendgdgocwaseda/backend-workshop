from fastapi import FastAPI

from app.routers import todos

# Part 3 (Routing): Uncomment the line below when you build the Notes router
# from app.routers import notes

app = FastAPI(
    title="Todo & Notes API",
    description="GDGoC Backend Workshop: Intro to FastAPI CRUD & Routing",
    version="0.1.0",
)


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the FastAPI Workshop! Visit /docs to get started."}


# Part 2: Todos router is already wired up — implement its endpoints in app/routers/todos.py
app.include_router(todos.router)

# Part 3 (Routing): Uncomment the line below to register your new Notes router
# app.include_router(notes.router)
