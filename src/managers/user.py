import uuid
from typing import Optional, Dict, Any

from fastapi import Request
from fastapi_users import BaseUserManager, UUIDIDMixin, models

from starlette.responses import Response

from src.config import SECRET
from src.models.user import User
from loguru import logger


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(
        self, user: User, request: Optional[Request] = None
    ) -> None:
        logger.success(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ) -> None:
        logger.info(
            f"User {user.id} has forgot their password. Reset token: {token}"
        )

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ) -> None:
        logger.info(
            f"Verification requested for user {user.id}. Verification token: {token}"
        )

    async def on_after_update(
        self,
        user: models.UP,
        update_dict: Dict[str, Any],
        request: Optional[Request] = None,
    ) -> None:
        logger.success(f"User {user.id} has been updated to {user.email}")

    async def on_after_login(
        self,
        user: models.UP,
        request: Optional[Request] = None,
        response: Optional[Response] = None,
    ) -> None:
        logger.success(f"User {user.email} has been login")
