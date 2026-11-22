from fastapi import APIRouter, HTTPException, status

from solutions import store
from solutions.schemas.todo import Todo, TodoCreate

router = APIRouter(
    prefix="/todos",
    tags=["Todos"],
)


@router.get("", response_model=list[Todo])
async def list_todos():
    return list(store.todos_db.values())


@router.get("/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    if todo_id not in store.todos_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found",
        )
    return store.todos_db[todo_id]


@router.post("", response_model=Todo, status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoCreate):
    todo_id = store.next_todo_id()
    new_todo = {"id": todo_id, **todo.model_dump()}
    store.todos_db[todo_id] = new_todo
    return new_todo


@router.put("/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo: TodoCreate):
    if todo_id not in store.todos_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found",
        )
    updated_todo = {"id": todo_id, **todo.model_dump()}
    store.todos_db[todo_id] = updated_todo
    return updated_todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: int):
    if todo_id not in store.todos_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo not found",
        )
    del store.todos_db[todo_id]
    return None
