# Backend Workshop: Intro to FastAPI

Build a RESTful **CRUD API** from scratch using **FastAPI**, **Pydantic**, **APIRouter**, and interactive **Swagger UI**.

## Prerequisites

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

### macOS/Linux:
1. **Copy and paste this command into your terminal:**

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
    or if you have Homebrew:

    ```bash
    brew install uv
    ```

2. **Restart your terminal.**

3. **Check if your installation succeeded:**
    ```bash
    uv --version
    ```

### Windows:
1. **Copy and paste this command into your PowerShell:**
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
2. **Restart your terminal.**
3. **Check if your installation succeeded:**
    ```powershell
    uv --version
    ```

## Setup

Clone the repository inside your desired directory and install the exact locked dependencies from `uv.lock`:

```bash
git clone https://github.com/backendgdgocwaseda/backend-workshop.git
cd backend-workshop/
uv sync --locked
```

## Running the Application

### Development Server (with auto-reload)

```bash
uv run fastapi dev app/main.py
```

Once running, the interactive API documentation is available at:

* **API Endpoint:** http://localhost:8000
* **Swagger UI:** http://localhost:8000/docs

---

## Project Structure

```text
backend-workshop/
├── app/
│   ├── __init__.py
│   ├── main.py              # App instantiation, metadata, and router registration
│   ├── store.py             # Simple in-memory dict store (easy to swap for a DB later)
│   ├── schemas/
│   │   ├── todo.py          # Part 1: Pydantic v2 input/output contracts (guided)
│   │   └── note.py          # Part 3: Pydantic v2 contracts for Notes (from scratch)
│   └── routers/
│       ├── todos.py         # Part 2: Guided APIRouter CRUD endpoints for /todos
│       └── notes.py         # Part 3: Build-from-scratch APIRouter CRUD endpoints for /notes
└── pyproject.toml
```

---

## Workshop Roadmap

This hands-on session is divided into **three parts**:

1. **Part 1 — Pydantic Models (`app/schemas/todo.py`):** Define request and response schemas for automatic validation and docs.
2. **Part 2 — Guided CRUD API (`app/routers/todos.py`):** Build `GET`, `POST`, `PUT`, and `DELETE` endpoints for `/todos` step by step.
3. **Part 3 — Routing with `APIRouter` & Build-From-Scratch Challenge (`app/schemas/note.py`, `app/routers/notes.py`, `app/main.py`):** Register a new router and build a complete `/notes` CRUD API from scratch.

Every time you save a file, the dev server automatically reloads—just refresh http://localhost:8000/docs to test your changes!

---

## Step 0: Verify Your Server

1. Run `uv run fastapi dev app/main.py`.
2. Visit http://localhost:8000/docs.
3. Click **`GET /`** -> **Try it out** -> **Execute** and confirm you get a `200 OK` response.

---

## Part 1: Pydantic Models (`app/schemas/todo.py`)

### Step 1: Define Your Schemas
FastAPI uses **Pydantic** models to validate incoming JSON, serialize responses, and auto-generate Swagger UI docs.

Open `app/schemas/todo.py` and define two models (input and output):
- `TodoCreate(BaseModel)` — used for `POST` and `PUT` request bodies:
  - `title: str`
  - `description: str | None = None`
  - `completed: bool = False`
- `Todo(TodoCreate)` — used for API responses:
  - `id: int`

> **Why two models?** Clients should not choose the `id` when creating or updating a todo—the server owns and assigns it.

---

## Part 2: Guided CRUD API — Todos (`app/routers/todos.py`)

`app/main.py` already mounts `todos.router` (`prefix="/todos"`). Open `app/routers/todos.py`, uncomment `from app.schemas.todo import Todo, TodoCreate`, and implement these endpoints:

| Operation | HTTP Method | Endpoint | Success Status | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Read (All)** | `GET` | `/todos` | `200 OK` | List all todos |
| **Read (One)** | `GET` | `/todos/{todo_id}` | `200 OK` | Get a single todo by ID (or `404`) |
| **Create** | `POST` | `/todos` | `201 Created` | Create a new todo |
| **Update** | `PUT` | `/todos/{todo_id}` | `200 OK` | Update an existing todo (or `404`) |
| **Delete** | `DELETE` | `/todos/{todo_id}` | `204 No Content` | Delete a todo (or `404`) |

### Step 2: Read Todos (`GET`)
1. **`@router.get("", response_model=list[Todo])`**:
   - Return `list(store.todos_db.values())`.
2. **`@router.get("/{todo_id}", response_model=Todo)`**:
   - Accept `todo_id: int` as a path parameter.
   - If `todo_id not in store.todos_db`, raise `HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")`.
   - Otherwise, return `store.todos_db[todo_id]`.

**Try it out in Swagger UI:**
- `GET /todos` -> returns the 2 pre-seeded todos.
- `GET /todos/1` -> `200 OK`.
- `GET /todos/999` -> `404 Not Found`.
- `GET /todos/abc` -> `422 Unprocessable Entity` (automatic type validation!).

### Step 3: Create a Todo (`POST`)
Create **`@router.post("", response_model=Todo, status_code=status.HTTP_201_CREATED)`**:
- Accept `todo: TodoCreate` as the request body.
- Generate an ID with `todo_id = store.next_todo_id()`.
- Store `new_todo = {"id": todo_id, **todo.model_dump()}` in `store.todos_db[todo_id]` and return `new_todo`.

**Try it out in Swagger UI:**
- Send `{"title": "Finish workshop"}` -> observe `201 Created` with `id: 3` and default `completed: false`.
- Send `{}` (missing `title`) -> observe automatic `422` validation error.

### Step 4: Update a Todo (`PUT`)
Create **`@router.put("/{todo_id}", response_model=Todo)`**:
- Accept `todo_id: int` and `todo: TodoCreate`.
- Raise `404` if `todo_id not in store.todos_db`.
- Replace `store.todos_db[todo_id]` with `{"id": todo_id, **todo.model_dump()}` and return it.

**Try it out in Swagger UI:**
- Send `{"title": "Build a CRUD API", "description": "Done!", "completed": true}` to `PUT /todos/2`, then call `GET /todos/2` to verify.
- Try updating `PUT /todos/999` -> observe `404 Not Found`.

### Step 5: Delete a Todo (`DELETE`)
Create **`@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)`**:
- Accept `todo_id: int`.
- Raise `404` if `todo_id not in store.todos_db`.
- Delete with `del store.todos_db[todo_id]` and return `None`.

**Try it out in Swagger UI:**
- Delete todo `1` -> observe `204 No Content`.
- Delete todo `1` again -> observe `404 Not Found`.

---

## Part 3: Routing with `APIRouter` — Your Turn! (`/notes`)

Notice how clean `app/main.py` stays when each resource lives in its own schema + router file:

```python
# app/main.py
from app.routers import notes, todos

app.include_router(todos.router)
app.include_router(notes.router)
```

### Step 6: Build the `/notes` CRUD API from Scratch
Now it's your turn to repeat the pattern end-to-end:

1. **Schemas (`app/schemas/note.py`):** Define `NoteCreate` (`title: str`, `content: str`, `pinned: bool = False`) and `Note(NoteCreate)` (`id: int`).
2. **Router (`app/routers/notes.py`):** Implement all 5 CRUD endpoints on `@router` using `store.notes_db` and `store.next_note_id()`:
   - `GET /notes` (`200 OK`)
   - `GET /notes/{note_id}` (`200 OK` / `404 Not Found`)
   - `POST /notes` (`201 Created`)
   - `PUT /notes/{note_id}` (`200 OK` / `404 Not Found`)
   - `DELETE /notes/{note_id}` (`204 No Content` / `404 Not Found`)
3. **Register (`app/main.py`):** Uncomment `from app.routers import notes` and `app.include_router(notes.router)`.
4. **Verify:** Refresh http://localhost:8000/docs — you should see a new **Notes** section alongside **Todos**! Test every endpoint.
