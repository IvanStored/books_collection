from fastapi import HTTPException

from src.managers.user import UserManager
from src.models.book import Book
from src.models.user import User
from src.schemas.book import BookRead


class UserService:
    def __init__(self, user_manager: UserManager):
        self.manager = user_manager

    @staticmethod
    def _find_book(books, isbn_number):
        for book in books:
            if book.isbn_number == isbn_number:
                return book
        raise HTTPException(
            status_code=404, detail="Book not found in your favourite"
        )

    async def delete_from_favourite(
        self, user: User, isbn_number: int
    ) -> None:
        existing_books = user.books
        book = self._find_book(books=existing_books, isbn_number=isbn_number)

        user.books.remove(book)
        await self.manager.save_changes(user)

    async def to_favourite(self, user: User, book: Book) -> None:
        for book in user.books:
            self._validate_existing(existing_book=book, book=book)
        user.books.append(book)
        await self.manager.save_changes(user)

    @staticmethod
    def get_users_books(user: User) -> list[BookRead]:
        return [BookRead(**book.__dict__) for book in user.books]

    @staticmethod
    def _validate_existing(existing_book: Book, book: Book) -> None:
        if book.isbn_number == existing_book.isbn_number:
            raise HTTPException(status_code=400, detail="Already exists")
