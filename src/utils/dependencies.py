import uuid

from fastapi import Depends
from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (
    CookieTransport,
    JWTStrategy,
    AuthenticationBackend,
)
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from src.config import SECRET
from src.database.db import get_async_session, get_user_db
from src.managers.book_manager import BookManager
from src.managers.user import UserManager
from src.models.user import User
from src.services.book_service import BookService


def get_book_service(session: AsyncSession = Depends(get_async_session)):
    manager = BookManager(session=session)
    return BookService(book_manager=manager)


async def get_user_manager(
    user_db: SQLAlchemyUserDatabase = Depends(get_user_db),
):
    yield UserManager(user_db)


cookie_transport = CookieTransport(cookie_name="qweqwrt", cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="cookie",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])


current_user = fastapi_users.authenticator.current_user(active=True)
