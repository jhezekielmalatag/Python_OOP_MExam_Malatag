class ReadingList:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        if not title.strip():
            raise ValueError("Book title cannot be blank")
        self.books.append(title)

    def count(self):
        return len(self.books)

    def titles(self):
        return self.books.copy()

if __name__ == "__main__":
    personal = ReadingList()
    team = ReadingList()
    personal.add_book("Python Basics")
    personal.add_book("OOP")
    team.add_book("Testing")
    external = personal.titles()
    external.append("Outside")
    print(personal.count())
    print(team.count())