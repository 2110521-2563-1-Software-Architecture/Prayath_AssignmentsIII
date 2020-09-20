from mvc.models.repositories.note_repository import NoteRepository

class MainController:
    def __init__(self):
        self.repository = NoteRepository()
    
    def get_all_notes(self):
        return self.repository.get_all_notes()

    def add_note(self, note: str):
        self.repository.add_note(note)

    def clear_all(self):
        self.repository.clear_all_notes()
