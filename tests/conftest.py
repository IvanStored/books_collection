import asyncio
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from fastapi.testclient import TestClient

from src.config import settings
from src.database.db import get_async_session
from src.main import app
from src.models.base import BaseModel

DATABASE_URL = settings.get_test_db_url()

engine_test = create_async_engine(DATABASE_URL, poolclass=NullPool)

async_session_maker = async_sessionmaker(
    bind=engine_test, class_=AsyncSession, expire_on_commit=False
)
BaseModel.metadata.bind = engine_test


async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


app.dependency_overrides[
    get_async_session
] = override_get_async_session  # Noqa


@pytest.fixture(autouse=True, scope="session")
async def prepare_db():
    async with engine_test.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


client = TestClient(app)


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://127.0.0.1") as ac:
        yield ac
