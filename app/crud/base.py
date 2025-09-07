from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


class CRUDBase:
    def __init__(self, model):
        self.model = model

    async def get_multi(self, session: AsyncSession):
        result = await session.execute(select(self.model))
        return result.scalars().all()

    async def get(self, obj_id: int, session: AsyncSession):
        result = await session.execute(
            select(self.model).where(self.model.id == obj_id)
        )
        return result.scalar_one_or_none()

    async def create(self, obj_in, session: AsyncSession):
        db_obj = self.model(**obj_in.dict())
        session.add(db_obj)
        await session.flush()
        await session.refresh(db_obj)
        return db_obj

    async def update(self, db_obj, obj_in, session: AsyncSession):
        for key, value in obj_in.dict(exclude_unset=True).items():
            setattr(db_obj, key, value)
        await session.flush()
        await session.refresh(db_obj)
        return db_obj

    async def remove(self, db_obj, session: AsyncSession):
        await session.delete(db_obj)
        await session.flush()
        return db_obj