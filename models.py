# template for each node
from typing import Optional

class Book:
    def __init__(self, name, book_id, author, total):
        """constructor for initialising the attriburtes for each node on creation"""
        self.name = name
        self.ID = book_id
        self.author = author
        self.available = total
        self.total = total
        self.next: Optional["Book"] = None