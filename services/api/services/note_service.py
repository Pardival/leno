import uuid
from datetime import datetime
from models.note import NoteDB
from repository.note_repository import NoteRepository
from services.ai_service import classify_note
from exceptions.exceptions import NoteNotFoundError

class NoteService:
    def __init__(self, repo: NoteRepository):
        self.repo = repo

    def find_all(self) -> list[NoteDB]:
        return self.repo.find_all()

    def find_by_id(self, note_id: str) -> NoteDB | None:
        return self.repo.find_by_id(note_id)

    def create(self, content: str) -> NoteDB:
        existing_categories = self.repo.find_distinct_categories()

        classification = classify_note(content, existing_categories)

        note = NoteDB(
            id=str(uuid.uuid4()),
            title=classification["titre"],
            content=classification["texte_nettoye"],
            category=classification["categorie"],
            tags=",".join(classification["tags"]),
            created_at=datetime.utcnow(),
        )

        return self.repo.save(note)

    def delete(self, note_id: str) -> None:
        deleted = self.repo.delete_by_id(note_id)
        if not deleted:
            raise NoteNotFoundError(note_id)

    def update(self, note_id: str, note_update) -> NoteDB:
        updates = note_update.model_dump(exclude_unset=True)
        note = self.repo.update(note_id, updates)
        if note is None:
            raise NoteNotFoundError(note_id)
        return note