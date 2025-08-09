# library_system.py

class Book:
    """Base class for all books."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class for electronic books."""
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class for printed books."""
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Library class demonstrating composition."""
    def __init__(self):
        self.books = []  # List to hold Book, EBook, and PrintBook instances

    def add_book(self, book: Book):
        """Add a book to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only Book or derived instances can be added to the library.")

    def list_books(self):
        """List all books in the library."""
        for book in self.books:
            print(book)
