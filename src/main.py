import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi.requests import Request
from starlette import status


from src.routers.auth import auth_router
from src.routers.book import books_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(books_router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root(request: Request):
    return RedirectResponse(
        url=request.url_for("login_page"),
        status_code=status.HTTP_303_SEE_OTHER,
    )


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run("src.main:app")
