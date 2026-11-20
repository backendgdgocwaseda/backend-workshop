from pydantic import BaseModel

# ===========================================================================
# PART 1: Define Pydantic Models for Todos (Input & Output)
# ===========================================================================
# TODO (Step 1a): Create a `TodoCreate` model inheriting from `BaseModel`
# (used for POST and PUT requests):
#   - title: str
#   - description: str | None = None
#   - completed: bool = False
#
# TODO (Step 1b): Create a `Todo` model inheriting from `TodoCreate`
# (used for API responses — includes the server-assigned ID):
#   - id: int
