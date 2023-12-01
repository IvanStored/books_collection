from fastapi import APIRouter, Depends

from src.models.user import User
from src.schemas.book import BookList
from src.schemas.user import UserRead, UserUpdate
from src.services.book_service import BookService
from src.services.user_service import UserService
from src.utils.dependencies import (
    fastapi_users,
    get_book_service,
    current_user,
    get_user_service,
)

user_router = APIRouter(prefix="/users", tags=["users"])

user_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
)


@user_router.get("/books/", response_model=BookList)
async def users_books(
    user: User = Depends(current_user),
    user_service: UserService = Depends(get_user_service),
) -> BookList:
    books = user_service.get_users_books(user=user)
    return BookList(books=books)


@user_router.patch("/add_book_to_favourite/{isbn}", response_model=None)
async def add_book_to_favourite(
    isbn: int,
    book_service: BookService = Depends(get_book_service),
    user: User = Depends(current_user),
    user_service: UserService = Depends(get_user_service),
):
    book = await book_service.add_new_book(isbn_number=isbn)

    await user_service.to_favourite(user=user, book=book)
    books = user_service.get_users_books(user=user)

    return BookList(books=books)


@user_router.delete("/delete_from_favourite/{isbn}", response_model=BookList)
async def delete_from_favourite(
    isbn: int,
    user=Depends(current_user),
    user_service: UserService = Depends(get_user_service),
) -> BookList:
    await user_service.delete_from_favourite(user=user, isbn_number=isbn)
    books = user_service.get_users_books(user=user)

    return BookList(books=books)
