import uuid
from typing import Any

from sqlalchemy import insert, select, update, delete, Result, Sequence
from sqlalchemy.ext.asyncio import AsyncSession


class BaseManager:
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_uuid(self, uuid_: uuid.UUID) -> Result:
        query = select(self.model).where(self.model.id == uuid_)
        res = await self.session.execute(statement=query)
        return res.scalar_one()

    async def list(self) -> Sequence:
        query = select(self.model)
        res = await self.session.execute(statement=query)

        return res.scalars().all()

    async def create_instance(self, instance_data: dict) -> Any:
        query = (
            insert(self.model).values(**instance_data).returning(self.model)
        )
        res = await self.session.execute(statement=query)
        return res.scalar_one()

    async def update_instance(
        self, uuid_: uuid.UUID, new_data: dict
    ) -> Result:
        query = (
            update(self.model)
            .where(self.model.id == uuid_)
            .values(**new_data)
            .returning(self.model)
        )

        res = await self.session.execute(statement=query)

        return res.scalar_one()

    async def delete_instance(self, uuid_: uuid.UUID) -> Result:
        query = (
            delete(self.model)
            .where(self.model.id == uuid_)
            .returning(self.model)
        )

        res = await self.session.execute(statement=query)

        return res.scalar_one()
