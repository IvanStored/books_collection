from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_async_session
from src.managers.book_manager import BookManager
from src.routers.auth import fastapi_users
from src.services.book_service import BookService


def get_book_service(session: AsyncSession = Depends(get_async_session)):
    manager = BookManager(session=session)
    return BookService(book_manager=manager)


current_user = fastapi_users.authenticator.current_user(active=True)
