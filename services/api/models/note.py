# models/note.py (le modèle de données, équivalent d'une @Entity en JPA)
from sqlalchemy import Column, String, DateTime
from core.database import Base
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