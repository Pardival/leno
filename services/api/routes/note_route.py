from fastapi import APIRouter, Depends, HTTPException
from dependencies import get_note_repository, get_note_service
from repository.note_repository import NoteRepository
from services.note_service import NoteService

from models.note import NoteDB, NoteCreate, NoteOut

router = APIRouter(prefix="/notes", tags=["notes"])

@router.get("/", response_model=list[NoteOut])
def list_notes(service: NoteService = Depends(get_note_service)):
    return service.find_all()

@router.get("/{note_id}", response_model=NoteOut)
def get_note(note_id: str, service: NoteService = Depends(get_note_service)):
    note = service.find_by_id(note_id)
    return note

@router.post("/", response_model=NoteOut)
def create_note(content: str, service: NoteService = Depends(get_note_service)):
    return service.create(content)

@router.post("/audio")
def create_note_by_audio():
    return {"post audio"}

@router.patch("/{item_id}")
def patch_note(note_id: str, service: NoteService = Depends(get_note_service)):
    return {"patch notes item_id"}

@router.delete("/{item_id}")
def delete_note(note_id: str, service: NoteService = Depends(get_note_service)):
    return service.delete_note(note_id)

@router.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}