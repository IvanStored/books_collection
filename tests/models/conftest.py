import datetime

import pytest

from src.managers.book_manager import BookManager
from src.models.book import Book
from src.services.book_service import BookService


@pytest.fixture(scope="session")
def book_payload():
    return {
        "title": "test",
        "author": "test_author",
        "number_of_pages": 123,
        "annotation": "wqewqe",
        "cover": "qweqw",
        "isbn_number": 1321,
    }


@pytest.fixture(scope="session")
def book_payload_with_publish_date():
    return {
        "title": "test_with_publish",
        "author": "test_author_with_publish",
        "number_of_pages": 123,
        "annotation": "wqewqe",
        "cover": "qweqw",
        "isbn_number": 1321,
        "publish_date": datetime.datetime.now(),
    }


@pytest.fixture(scope="session")
def get_book_service(get_test_session):
    manager = BookManager(session=get_test_session)
    service = BookService(book_manager=manager)
    return service


@pytest.fixture(scope="session")
async def create_book(book_payload, get_book_service):
    service = get_book_service
    book = await service.manager.create_instance(instance_data=book_payload)
    return book


@pytest.fixture(scope="session")
async def create_book_with_publish_date(
    book_payload_with_publish_date, get_book_service
):
    service = get_book_service
    book = await service.manager.create_instance(
        instance_data=book_payload_with_publish_date
    )
    return book


@pytest.fixture(scope="session")
async def update_publish_date(create_book_with_publish_date, get_book_service):
    book = create_book_with_publish_date
    service = get_book_service
    book = await service.update_book(
        uuid_number=book.id, new_data={"publish_date": datetime.datetime.now()}
    )
    return book


@pytest.fixture(scope="session")
async def update_number_of_pages(
    create_book_with_publish_date, get_book_service
):
    book = create_book_with_publish_date
    service = get_book_service
    book = await service.update_book(
        uuid_number=book.id, new_data={"number_of_pages": 321}
    )
    return book
