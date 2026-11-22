from pydantic import BaseModel


class NoteCreate(BaseModel):
    title: str
    content: str
    pinned: bool = False


class Note(NoteCreate):
    id: int
