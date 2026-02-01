class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Имя книги не может быть пустым.")
        self._name = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Имя автора не может быть пустым.")
        self._author = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Длительность должна быть положительным числом.")
        self._duration = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

book1 = PaperBook("Преступление и наказание", "Федор Достоевский", 1866)
book2 = AudioBook("Дюна", "Френк Герберт", 1965)

print(book1)
print(repr(book1))
print(book2)
print(repr(book2))
