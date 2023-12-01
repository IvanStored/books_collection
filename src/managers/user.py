import uuid
from typing import Optional

from fastapi import Request
from fastapi_users import BaseUserManager, UUIDIDMixin, models
from sqlalchemy.ext.asyncio import AsyncSession

from starlette.responses import Response

from src.config import SECRET
from src.managers.base_manager import BaseManager
from src.models.user import User
from loguru import logger


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID], BaseManager):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET
    model = User

    session: AsyncSession = None

    async def on_after_register(
        self, user: User, request: Optional[Request] = None
    ) -> None:
        logger.success(f"User {user.id} has registered.")

    async def on_after_login(
        self,
        user: models.UP,
        request: Optional[Request] = None,
        response: Optional[Response] = None,
    ) -> None:
        logger.success(f"User {user.email} has been login")

    async def save_changes(self, user: User):
        self.session.add(user)
        await self.session.commit()
