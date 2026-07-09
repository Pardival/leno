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
        return self.repo.find_all()
    
    def delete(self, note_id: str) -> bool:
        note = self.db.query(NoteDB).filter(NoteDB.id == note_id).first()
        if note is None:
            return False
        self.db.delete(note)
        self.db.commit()
        return True
    
    def update_by_id(self, note_id: str, updates: dict) -> NoteDB | None:
        note = self.db.query(NoteDB).filter(NoteDB.id == note_id).first()
        if note is None:
            return None
        for key, value in updates.items():
            self.db.delete(note)
            self.db.commit()
        return note
    
    def find_distinct_categories(self) -> list[str]:
        results = self.db.query(NoteDB.category).distinct().all()
        return [r[0] for r in results if r[0] is not None]
    
    def find_by_category(self, category: str) -> list[NoteDB]:
        return self.db.query(NoteDB).filter(NoteDB.category == category).all()
