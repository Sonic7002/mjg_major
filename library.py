# this file contains the library class resposible for all operations on the linked list
from models import Book

class Library:
    def __init__(self):
        """constructor for initialising the head of the linked list"""
        self.head = None

    def _find_by_id(self, book_id):
        """protected method to be used to find a book based on its id provoded"""
        current = self.head
        while current is not None:
            if current.ID == book_id:
                return current
            current = current.next
        return None

    def add_book(self, name, book_id, author, total):
        """adds a new book to the collection of books requires the parameters of the book"""
        if total <= 0:
            raise ValueError("Total books cannot be negative")
        if self._find_by_id(book_id) is not None:
            raise ValueError("Book already exists")
        if self.head is None:
            self.head = Book(name, book_id, author, total)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Book(name, book_id, author, total)

    def add_stock(self, book_id, added):
        """edit stock for a existing book collection"""
        if added <= 0:
            raise ValueError("Added stock must be positive")
        current = self._find_by_id(book_id)
        if current is None:
            raise ValueError("ID not found")
        current.total += added
        current.available += added

    def remove(self, book_id):
        """used to remove a collection of books from the existing collection based on book id"""
        if self.head is None:
            raise ValueError("No books are available")
        if self.head.ID == book_id:
            if self.head.total != self.head.available:
                raise ValueError("Cannot remove if copies are issued")
            self.head = self.head.next
            return
        prev = self.head
        current = self.head.next
        while current is not None:
            if current.ID == book_id:
                if current.total != current.available:
                    raise ValueError("Cannot remove if copies are issued")
                prev.next = current.next
                return
            prev = current
            current = current.next
        raise ValueError("Book ID not found")

    def search(self, key) -> list[dict]:
        """searches for a book based on the given key and returns matched results"""
        current = self.head
        result = []
        while current is not None:
            if (
                key.lower() in current.name.lower()
                or key.lower() in current.author.lower()
            ):
                result.append(
                    {"ID": current.ID, "name": current.name, "author": current.author}
                )
            current = current.next
        return result.copy()

    def issue_book(self, book_id):
        """issues a book based on id"""
        book = self._find_by_id(book_id)
        if book is None:
            raise ValueError("Book ID not found")
        if book.available == 0:
            raise ValueError("Book is out of stock")
        book.available -= 1

    def return_book(self, book_id):
        """returns a issued book"""
        book = self._find_by_id(book_id)
        if book is None:
            raise ValueError("Book ID not found")
        if book.available == book.total:
            raise ValueError("No book was issued")
        book.available += 1

    def list_books(self) -> list[dict]:
        """returns a list of all books"""
        books = []
        current = self.head
        while current is not None:
            books.append(
                {
                    "name": current.name,
                    "ID": current.ID,
                    "author": current.author,
                    "available": current.available,
                    "total": current.total,
                }
            )
            current = current.next
        return books