# Пример1: Итератор для библиотеки книг

class Book:
    """Класс книги"""
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f"'{self.title}' - {self.author} ({self.year})"


class BookCollection:
    """Коллекция книг с разными способами хранения"""
    def __init__(self):
        self._books = []
    
    def add_book(self, book: Book):
        """Добавить книгу в коллекцию"""
        self._books.append(book)
    
    def __iter__(self):
        """Возвращает итератор по коллекции"""
        return BookIterator(self._books)
    
    def get_reverse_iterator(self):
        """Получить итератор в обратном порядке"""
        return ReverseBookIterator(self._books)
    
    def get_author_iterator(self, author: str):
        """Получить итератор по книгам определенного автора"""
        return AuthorBookIterator(self._books, author)
    
    def get_year_iterator(self, start_year: int, end_year: int):
        """Получить итератор по книгам определенного периода"""
        return YearBookIterator(self._books, start_year, end_year)


class BookIterator:
    def __init__(self, books: list):
        self._books = books
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self) -> Book:
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        raise StopIteration


class ReverseBookIterator(BookIterator):
    """Итератор книг в обратном порядке"""
    def __init__(self, books: list):
        super().__init__(books)
        self._index = len(books) - 1
    
    def __next__(self) -> Book:
        if self._index >= 0:
            book = self._books[self._index]
            self._index -= 1
            return book
        raise StopIteration


class AuthorBookIterator(BookIterator):
    """Итератор книг определенного автора"""
    def __init__(self, books: list, author: str):
        super().__init__(books)
        self._author = author
        self._filter_books()
    
    def _filter_books(self):
        """Отфильтровать книги по автору"""
        self._books = [book for book in self._books if book.author == self._author]
        self._index = 0


class YearBookIterator(BookIterator):
    """Итератор книг определенного периода"""
    def __init__(self, books: list, start_year: int, end_year: int):
        super().__init__(books)
        self._start_year = start_year
        self._end_year = end_year
        self._filter_books()
    
    def _filter_books(self):
        """Отфильтравать книги по году издания"""
        filtered = []
        for book in self._books:
            if self._start_year <= book.year <= self._end_year:
                filtered.append(book)
        self._books = filtered
        self._index = 0


#пример2: Итератор для обхода дерева
class TreeNode:
    """Узел дерева"""
    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, node):
        self.children.append(node)


class TreeIterator:
    """Итератор для обхода дерева в глубину"""
    def __init__(self, root: TreeNode):
        self._stack = [root]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self._stack:
            raise StopIteration
        
        node = self._stack.pop()
        for child in reversed(node.children):
            self._stack.append(child)
        
        return node.value


def test_iterator():
    """Тестирование паттерна Итератор"""
    print("Пример 1: Библиотека книг")
    print("-" * 40)
    
    library = BookCollection()
    
    library.

add_book(Book("Мастер и Маргарита", "Михаил Булгаков", 1967))
    library.add_book(Book("Преступление и наказание", "Федор Достоевский", 1866))
    library.add_book(Book("Война и мир", "Лев Толстой", 1869))
    library.add_book(Book("Анна Каренина", "Лев Толстой", 1877))
    library.add_book(Book("Отцы и дети", "Иван Тургенев", 1862))
    library.add_book(Book("1984", "Джордж Оруэлл", 1949))
    library.add_book(Book("Скотный двор", "Джордж Оруэлл", 1945))
    
    print("Все книги в библиотеке:")
    print("-" * 30)
    for book in library:
        print(f"  • {book}")
    
    print("\nКниги в обратном порядке:")
    print("-" * 30)
    for book in library.get_reverse_iterator():
        print(f"  • {book}")
    
    print("\nКниги Льва Толстого:")
    print("-" * 30)
    for book in library.get_author_iterator("Лев Толстой"):
        print(f"  • {book}")
    
    print("\nКниги XX века (1900-1999):")
    print("-" * 30)
    for book in library.get_year_iterator(1900, 1999):
        print(f"  • {book}")
    
    print("\n" + "=" * 40)
    print("Пример 2: Обход дерева")
    print("-" * 40)
    
    root = TreeNode("A")
    b = TreeNode("B")
    c = TreeNode("C")
    d = TreeNode("D")
    e = TreeNode("E")
    f = TreeNode("F")
    
    root.add_child(b)
    root.add_child(c)
    b.add_child(d)
    b.add_child(e)
    c.add_child(f)
    
    tree_iterator = TreeIterator(root)
    
    print("Обход дерева в глубину:")
    print("-" * 30)
    for node in tree_iterator:
        print(f"  Посетили узел: {node}")
    
    print("\nИспользование итератора напрямую:")
    print("-" * 30)
    iterator = iter(library)
    try:
        while True:
            book = next(iterator)
            print(f"  Текущая книга: {book}")
    except StopIteration:
        print("  Все книги просмотрены!")
