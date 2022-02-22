import datetime

avialable_id = 0


class Note:
    def __init__(self, text, tags=[]):
        self.text = text
        self.tags = tags

        self.creating_date = datetime.date.today()

        global avialable_id
        self.note_id = avialable_id
        avialable_id += 1

    def contains(self, search_text):
        return search_text in self.text or search_text in self.tags

    def __str__(self) -> str:
        return self.text
