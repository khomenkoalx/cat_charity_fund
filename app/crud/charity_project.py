from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.charity_project import CharityProject
from app.schemas.charity_project import (
    CharityProjectCreate, CharityProjectUpdate
)
from .base import CRUDBase


class CRUDCharityProject(CRUDBase):
    def __init__(self):
        super().__init__(CharityProject)

    async def create(
            self,
            obj_in: CharityProjectCreate,
            session: AsyncSession):
        return await super().create(obj_in, session)

    async def update(
        self,
        db_obj,
        obj_in: CharityProjectUpdate,
        session: AsyncSession
    ):
        return await super().update(db_obj, obj_in, session)

    async def remove(self, db_obj, session: AsyncSession):
        return await super().remove(db_obj, session)

    async def get_unfinished_ordered(self, session: AsyncSession):
        result = await session.execute(
            select(self.model).where(~self.model.fully_invested).order_by(
                self.model.create_date
            )
        )
        return result.scalars().all()


charity_project_crud = CRUDCharityProject()
