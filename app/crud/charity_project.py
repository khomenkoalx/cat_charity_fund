from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from app.models.charity_project import CharityProject
from app.schemas.charity_project import (
    CharityProjectCreate, CharityProjectUpdate
)
from app.services.investment import invest_money
from app.core.constants import (
    ERROR_PROJECT_EXISTS, ERROR_PROJECT_CLOSED_EDIT,
    ERROR_PROJECT_SUM_LESS_INVESTED, ERROR_PROJECT_DELETE_FORBIDDEN
)
from .base import CRUDBase


class CRUDCharityProject(CRUDBase):
    def __init__(self):
        super().__init__(CharityProject)

    async def create(
            self,
            obj_in: CharityProjectCreate,
            session: AsyncSession):
        result = await session.execute(
            select(self.model).where(self.model.name == obj_in.name)
        )
        if result.scalar_one_or_none():
            raise HTTPException(status_code=400, detail=ERROR_PROJECT_EXISTS)
        new_project = await super().create(obj_in, session)
        await invest_money(session)
        await session.refresh(new_project)
        return new_project

    async def update(
        self,
        db_obj,
        obj_in: CharityProjectUpdate,
        session: AsyncSession
    ):
        if db_obj.fully_invested:
            raise HTTPException(
                status_code=400,
                detail=ERROR_PROJECT_CLOSED_EDIT
            )
        if obj_in.name:
            result = await session.execute(
                select(self.model).where(
                    self.model.name == obj_in.name,
                    self.model.id != db_obj.id
                )
            )
            if result.scalar_one_or_none():
                raise HTTPException(
                    status_code=400,
                    detail=ERROR_PROJECT_EXISTS)
        if obj_in.full_amount is not None and (
            obj_in.full_amount < db_obj.invested_amount
        ):
            raise HTTPException(
                status_code=400,
                detail=ERROR_PROJECT_SUM_LESS_INVESTED
            )
        return await super().update(db_obj, obj_in, session)

    async def remove(self, db_obj, session: AsyncSession):
        if db_obj.invested_amount > 0 or db_obj.fully_invested:
            raise HTTPException(
                status_code=400,
                detail=ERROR_PROJECT_DELETE_FORBIDDEN
            )
        return await super().remove(db_obj, session)


charity_project_crud = CRUDCharityProject()
