import uuid
from fastapi import APIRouter, Depends

from src.schemas.book import BookRead, BookList, BookUpdate
from src.services.book_service import BookService

from src.utils.dependencies import (
    get_book_service,
    super_user,
)

books_router = APIRouter(
    prefix="/books", tags=["books"], dependencies=[Depends(super_user)]
)


@books_router.post("/add_book/{isbn_number}", response_model=BookRead)
async def add_book(
    isbn_number: int, service: BookService = Depends(get_book_service)
):
    return await service.add_new_book(isbn_number=isbn_number)


@books_router.get("/get_by_uuid/{uuid}", response_model=BookRead)
async def get_book_by_uuid(
    uuid_: uuid.UUID,
    service: BookService = Depends(get_book_service),
):
    return await service.get_one_by_uuid(uuid_number=uuid_)


@books_router.get(
    "/all_books",
    response_model=BookList,
)
async def get_all_books(service: BookService = Depends(get_book_service)):
    return {"books": await service.get_all_books()}


@books_router.patch("/update_book/{uuid_}", response_model=BookRead)
async def update_book(
    uuid_: uuid.UUID,
    new_data: BookUpdate,
    service: BookService = Depends(get_book_service),
):
    return await service.update_book(
        uuid_number=uuid_, new_data=new_data.model_dump(exclude_none=True)
    )


@books_router.delete("/delete_book/{uuid_}", response_model=BookRead)
async def delete_book(
    uuid_: uuid.UUID,
    service: BookService = Depends(get_book_service),
):
    return await service.delete_book(uuid_number=uuid_)
