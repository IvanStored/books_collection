import uuid

from fastapi import APIRouter, Request, Depends
from fastapi_users import FastAPIUsers
from starlette import status
from starlette.responses import RedirectResponse
from starlette.templating import _TemplateResponse  # noqa

from src.config import templates
from src.managers.user import (
    get_user_manager,
    auth_backend,
    current_active_user,
)
from src.models.user import User
from src.schemas.user import UserRead, UserCreate, UserUpdate

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)
auth_router = APIRouter()


@auth_router.get("/login")
async def login_page(request: Request) -> _TemplateResponse:
    return templates.TemplateResponse(
        "index.html", context={"request": request}
    )


@auth_router.get("/index", response_model=None)
async def main_page(
    request: Request, user: User = Depends(current_active_user)
) -> _TemplateResponse | RedirectResponse:
    if not user:
        return RedirectResponse(
            url=request.url_for("login_page"),
            status_code=status.HTTP_303_SEE_OTHER,
        )
    return templates.TemplateResponse(
        "check_me.html", context={"request": request, "current_user": user}
    )


auth_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
auth_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
auth_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

auth_router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
