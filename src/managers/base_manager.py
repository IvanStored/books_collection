import uuid

from pydantic import BaseModel
from sqlalchemy import insert, select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.book import BookUpdate


class BaseManager:
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_uuid(self, uuid_: uuid.UUID):
        query = select(self.model).where(self.model.id == uuid_)
        res = await self.session.execute(statement=query)
        return res.scalar_one()

    async def list(self):
        query = select(self.model)
        res = await self.session.execute(statement=query)

        return res.scalars().all()

    async def add(self, instance_data: BaseModel):
        query = (
            insert(self.model)
            .values(**instance_data.__dict__)
            .returning(self.model)
        )
        res = await self.session.execute(statement=query)
        return res.scalar_one()

    async def update(self, uuid_: uuid.UUID, new_data: BookUpdate):
        query = (
            update(self.model)
            .where(self.model.id == uuid_)
            .values(**new_data.__dict__)
            .returning(self.model)
        )

        res = await self.session.execute(statement=query)

        return res.scalar_one()

    async def delete(self, uuid_: uuid.UUID):
        query = (
            delete(self.model)
            .where(self.model.id == uuid_)
            .returning(self.model)
        )

        res = await self.session.execute(statement=query)

        return res.scalar_one()
