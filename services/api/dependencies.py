from fastapi import Depends
from sqlalchemy.orm import Session
from core.database import get_db
from repository.note_repository import NoteRepository

def get_note_repository(db: Session = Depends(get_db)) -> NoteRepository:
    return NoteRepository(db)