from fastapi import Depends
from sqlalchemy.orm import Session
from core.database import get_db
from repository.note_repository import NoteRepository
from services.note_service import NoteService


def get_note_repository(db: Session = Depends(get_db)) -> NoteRepository:
    return NoteRepository(db)

def get_note_service(repo: NoteRepository = Depends(get_note_repository)) -> NoteService:
    return NoteService(repo)