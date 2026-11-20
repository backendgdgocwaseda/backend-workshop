from pydantic import BaseModel

# ===========================================================================
# PART 3 CHALLENGE: Define Pydantic Models for Notes from scratch!
# ===========================================================================
# Using the same Input & Output pattern from Part 1 (`app/schemas/todo.py`), define:
#   - `NoteCreate(BaseModel)`: title (str), content (str), pinned (bool = False)
#   - `Note(NoteCreate)`: id (int)
