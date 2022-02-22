from ctypes.wintypes import tagSIZE
from typing import List
from note import Note

avialable_id = 0


class Notebook:
    def __init__(self, notes=[]):
        self.notes = notes

    def new_note(self, text, tags=[]):
        new_note = Note(text, tags)
        self.notes.append(new_note)

    def modify_note_text(self, note_id, text):
        self.find_note(note_id).text = text

    def modify_note_tags(self, note_id, tags):
        self.find_note(note_id).tags = tags

    def find_note(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        print("invalid note id:"+str(note_id))
        return None

    def find_text(self, text):
        for note in self.notes:
            if note.contains(text):
                return note


notebook = Notebook()
notebook.new_note("feeling happy", ["fun"])
notebook.modify_note_text(0, "feeling happy")
print("Search text 'happy': "+str(notebook.find_text("happy")))
print("Search tag 'fun': "+str(notebook.find_text("fun")))
