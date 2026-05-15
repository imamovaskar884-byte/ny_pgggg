class Book:
    __slots__ = ('title', 'author')

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"Книга: '{self.title}', Автор: {self.author}")

b = Book("Мастер и Маргарита", "Михаил Булгаков")
b.info()
