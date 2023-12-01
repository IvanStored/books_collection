import http
from uuid import UUID

from fastapi import HTTPException
from sqlalchemy.exc import NoResultFound

from src.managers.book_manager import BookManager
from src.models.book import Book
from src.utils.scraper import scraper


class BookService:
    def __init__(self, book_manager: BookManager):
        self.manager = book_manager

    async def __check_existing(self, uuid_):
        try:
            return await self.manager.get_by_uuid(uuid_=uuid_)
        except NoResultFound:
            raise HTTPException(
                status_code=http.HTTPStatus.NOT_FOUND,
                detail=f"Book {uuid_} was not found",
            )

    async def add_new_book(self, isbn_number: int) -> Book:
        book = scraper.find_book(isbn_number=isbn_number)
        return await self.manager.create_instance(book)

    async def update_book(self, uuid_number: UUID, new_data: dict):
        await self.__check_existing(uuid_=uuid_number)
        return await self.manager.update_instance(
            uuid_=uuid_number, new_data=new_data
        )

    async def delete_book(self, uuid_number: UUID):
        await self.__check_existing(uuid_=uuid_number)
        return await self.manager.delete_instance(uuid_=uuid_number)

    async def get_one_by_uuid(self, uuid_number: UUID):
        book = await self.__check_existing(uuid_=uuid_number)
        return book

    async def get_all_books(self):
        return await self.manager.list()
