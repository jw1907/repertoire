class Piece:
    def __init__(self, author, title, note) -> None:
        self.author = author
        self.title = title
        self.note = note

    def get_info(self) -> str:
        return ', '.join([self.author, self.title, self.note])

