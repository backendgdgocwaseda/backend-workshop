"""Simple in-memory dictionary store (easy to swap for a real database later)."""

todos_db: dict[int, dict] = {
    1: {
        "id": 1,
        "title": "Learn FastAPI basics",
        "description": "Explore the interactive Swagger UI at /docs",
        "completed": True,
    },
    2: {
        "id": 2,
        "title": "Build a CRUD API",
        "description": "Implement GET, POST, PUT, and DELETE endpoints",
        "completed": False,
    },
}
_next_todo_id: int = 3


def next_todo_id() -> int:
    global _next_todo_id
    current = _next_todo_id
    _next_todo_id += 1
    return current


notes_db: dict[int, dict] = {
    1: {
        "id": 1,
        "title": "FastAPI Routing",
        "content": "Use APIRouter to split endpoints across multiple files.",
        "pinned": True,
    },
}
_next_note_id: int = 2


def next_note_id() -> int:
    global _next_note_id
    current = _next_note_id
    _next_note_id += 1
    return current
