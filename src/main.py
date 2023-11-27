import loguru
import uvicorn
from fastapi import FastAPI
from src.config import settings

from src.routers.auth import user_router

app = FastAPI()

app.include_router(user_router)


@app.get("/")
async def root():
    return {"message": settings.DB_HOST, "rul": settings.DB_NAME}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run("src.main:app")
