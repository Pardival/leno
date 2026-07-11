# models/note.py (le modèle de données, équivalent d'une @Entity en JPA)
from sqlalchemy import Column, String, DateTime
from core.database import Base
from pydantic import BaseModel, ConfigDict
import uuid
from datetime import datetime

class NoteDB(Base):
    __tablename__ = "notes"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String)
    content = Column(String)
    category = Column(String)
    tags = Column(String)  # stocké en JSON stringifié, ou table séparée si tu veux du relationnel propre
    audio_path = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


# Schémas Pydantic (entrée/sortie API), distincts du modèle SQLAlchemy ci-dessus
class NoteCreate(BaseModel):
    title: str
    content: str
    category: str | None = None
    tags: str | None = None
    audio_path: str | None = None


class NoteUpdate(BaseModel):
    title: str | None = None
    content: str | None = None
    category: str | None = None
    tags: str | None = None
    audio_path: str | None = None


class NoteOut(NoteCreate):
    model_config = ConfigDict(from_attributes=True)

    id: str
    created_at: datetime