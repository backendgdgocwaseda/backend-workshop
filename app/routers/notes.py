from fastapi import APIRouter, HTTPException, status

from app import store

# Once you define your Note schemas in app/schemas/note.py, import them here:
# from app.schemas.note import Note, NoteCreate

router = APIRouter(
    prefix="/notes",
    tags=["Notes"],
)


# ===========================================================================
# PART 3 CHALLENGE: Build the Notes CRUD API from scratch!
# ===========================================================================
# Using what you learned in Parts 1 & 2, implement all 5 CRUD endpoints on `@router`
# using `store.notes_db` and `store.next_note_id()` (remember: because `prefix="/notes"`
# is set above, use `""` for `/notes` and `"/{note_id}"` for `/notes/{note_id}`):
#
#   - GET    /notes            -> list all notes (200 OK)
#   - GET    /notes/{note_id}  -> get one note by ID (200 OK / 404 Not Found)
#   - POST   /notes            -> create a new note (201 Created)
#   - PUT    /notes/{note_id}  -> update an existing note (200 OK / 404 Not Found)
#   - DELETE /notes/{note_id}  -> delete a note (204 No Content / 404 Not Found)
#
# Don't forget to register `notes.router` in `app/main.py`!
