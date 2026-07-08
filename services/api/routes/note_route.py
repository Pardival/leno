# api/routes/notes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_note_repository
from repositories.note_repository import NoteRepository
from models.note import NoteDB

router = APIRouter(prefix="/notes", tags=["notes"])

@router.get("/")
def list_notes(repo: NoteRepository = Depends(get_note_repository)):
    return repo.find_all()

@router.get("/{note_id}")
def get_note(note_id: str, repo: NoteRepository = Depends(get_note_repository)):
    note = repo.find_by_id(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@router.post("/")
def create_note(toCreate : NoteDB, db: Session = Depends(get_note_repository)):
    repo = NoteRepository(db)
    # 1. Appeler le service OpenAI
    # 2. save dans un markdown
    # 3. save dans la bd
    return repo.save(toCreate)

@router.post("/audio")
def create_note_by_audio():
    return {"post audio"}

@router.patch("/{item_id}")
def patch_note():
    return {"patch notes item_id"}

@router.delete("/{item_id}")
def delete_note():
    return {"delete notes item_id"}

@router.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}