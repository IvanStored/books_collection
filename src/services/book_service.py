from uuid import UUID

from src.managers.book_manager import BookManager
from src.schemas.book import BookRead, BookUpdate
from src.utils.scraper import scraper


class BookService:
    def __init__(self, book_manager: BookManager):
        self.manager = book_manager

    async def add_new_book(self, isbn_number: int) -> BookRead:
        book = scraper.find_book(isbn_number=isbn_number)
        return await self.manager.add(book)

    async def update_book(self, uuid_number: UUID, new_data: BookUpdate):
        return await self.manager.update(uuid_=uuid_number, new_data=new_data)

    async def delete_book(self, uuid_number: UUID):
        return await self.manager.delete(uuid_=uuid_number)

    async def get_one_by_uuid(self, uuid_number: UUID):
        return await self.manager.get_by_uuid(uuid_=uuid_number)

    async def get_all_books(self):
        return await self.manager.list()
