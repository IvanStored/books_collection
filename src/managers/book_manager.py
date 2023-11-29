from src.managers.base_manager import BaseManager
from src.models.book import Book


class BookManager(BaseManager):
    model = Book
