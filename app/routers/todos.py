from fastapi import APIRouter, HTTPException, status

from app import store

# Once you complete Part 1 (app/schemas/todo.py), uncomment this import:
# from app.schemas.todo import Todo, TodoCreate

router = APIRouter(
    prefix="/todos",
    tags=["Todos"],
)


# ===========================================================================
# PART 2: Guided CRUD API (Todos)
# ===========================================================================

# --- Step 2: READ (GET) ----------------------------------------------------
# TODO (Step 2a): Create `GET /todos` using `@router.get("", response_model=list[Todo])`
#   - Return all todos from `store.todos_db` as a list (`list(store.todos_db.values())`).


# TODO (Step 2b): Create `GET /todos/{todo_id}` using `@router.get("/{todo_id}", response_model=Todo)`
#   - Accept `todo_id: int` as a path parameter.
#   - If `todo_id` is not in `store.todos_db`, raise:
#       HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
#   - Otherwise, return `store.todos_db[todo_id]`.


# --- Step 3: CREATE (POST) -------------------------------------------------
# TODO (Step 3): Create `POST /todos` using:
#   `@router.post("", response_model=Todo, status_code=status.HTTP_201_CREATED)`
#   - Accept `todo: TodoCreate` as the request body.
#   - Get a new ID via `todo_id = store.next_todo_id()`.
#   - Store `new_todo = {"id": todo_id, **todo.model_dump()}` in `store.todos_db[todo_id]`.
#   - Return `new_todo`.


# --- Step 4: UPDATE (PUT) --------------------------------------------------
# TODO (Step 4): Create `PUT /todos/{todo_id}` using `@router.put("/{todo_id}", response_model=Todo)`
#   - Accept `todo_id: int` and `todo: TodoCreate`.
#   - If `todo_id` is not in `store.todos_db`, raise a 404 HTTPException.
#   - Replace `store.todos_db[todo_id]` with `{"id": todo_id, **todo.model_dump()}`.
#   - Return the updated todo.


# --- Step 5: DELETE (DELETE) -----------------------------------------------
# TODO (Step 5): Create `DELETE /todos/{todo_id}` using:
#   `@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)`
#   - Accept `todo_id: int`.
#   - If `todo_id` is not in `store.todos_db`, raise a 404 HTTPException.
#   - Remove it with `del store.todos_db[todo_id]` and return `None`.
