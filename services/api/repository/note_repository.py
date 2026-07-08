from sqlalchemy.orm import Session
from models.note import NoteDB

class NoteRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, note: NoteDB) -> NoteDB:
        self.db.add(note)
        self.db.commit()
        self.db.refresh(note)
        return note

    def find_by_id(self, note_id: str) -> NoteDB | None:
        return self.db.query(NoteDB).filter(NoteDB.id == note_id).first()

    def find_all(self) -> list[NoteDB]:
        return self.db.query(NoteDB).all()