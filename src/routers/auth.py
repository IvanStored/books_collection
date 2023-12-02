from fastapi import APIRouter, Request, Depends
from starlette import status
from starlette.responses import RedirectResponse, HTMLResponse

from src.config import templates

from src.models.user import User
from src.schemas.user import UserRead, UserCreate
from src.utils.dependencies import current_user, fastapi_users, auth_backend

auth_router = APIRouter()


@auth_router.get("/login")
async def login_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "index.html", context={"request": request}
    )


@auth_router.get("/register_page")
async def register_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "register_page.html", context={"request": request}
    )


@auth_router.get("/index", response_model=None)
async def main_page(
    request: Request, user: User = Depends(current_user)
) -> HTMLResponse | RedirectResponse:
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
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
