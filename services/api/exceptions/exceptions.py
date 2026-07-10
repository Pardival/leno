class NoteNotFoundError(Exception):
    def __init__(self, note_id: str):
        self.note_id = note_id
        super().__init__(f"Note {note_id} introuvable")