from fastapi import APIRouter, HTTPException, status

from solutions import store
from solutions.schemas.note import Note, NoteCreate

router = APIRouter(
    prefix="/notes",
    tags=["Notes"],
)


@router.get("", response_model=list[Note])
async def list_notes():
    return list(store.notes_db.values())


@router.get("/{note_id}", response_model=Note)
async def get_note(note_id: int):
    if note_id not in store.notes_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found",
        )
    return store.notes_db[note_id]


@router.post("", response_model=Note, status_code=status.HTTP_201_CREATED)
async def create_note(note: NoteCreate):
    note_id = store.next_note_id()
    new_note = {"id": note_id, **note.model_dump()}
    store.notes_db[note_id] = new_note
    return new_note


@router.put("/{note_id}", response_model=Note)
async def update_note(note_id: int, note: NoteCreate):
    if note_id not in store.notes_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found",
        )
    updated_note = {"id": note_id, **note.model_dump()}
    store.notes_db[note_id] = updated_note
    return updated_note


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(note_id: int):
    if note_id not in store.notes_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Note not found",
        )
    del store.notes_db[note_id]
    return None
