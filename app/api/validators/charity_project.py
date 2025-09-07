from typing import Any
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.constants import (
    ERROR_PROJECT_EXISTS,
    ERROR_PROJECT_CLOSED_EDIT,
    ERROR_PROJECT_SUM_LESS_INVESTED,
)
from app.models.charity_project import CharityProject
from app.schemas.charity_project import (
    CharityProjectCreate, CharityProjectUpdate
)


def validate_patch_fields(
        body: dict[str, Any],
        allowed_fields: set[str],
        error_prefix: str
) -> None:
    extra_fields = set(body.keys()) - allowed_fields
    if extra_fields:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=error_prefix + ', '.join(extra_fields)
        )


def ensure_project_exists(db_obj: Any, not_found_message: str) -> None:
    if not db_obj:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=not_found_message
        )


async def ensure_project_create_valid(
        project: CharityProjectCreate,
        session: AsyncSession
) -> None:
    result = await session.execute(
        select(CharityProject).where(CharityProject.name == project.name)
    )
    if result.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ERROR_PROJECT_EXISTS
        )


async def ensure_project_update_valid(
        db_obj: CharityProject,
        obj_in: CharityProjectUpdate,
        session: AsyncSession
) -> None:
    if db_obj.fully_invested:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ERROR_PROJECT_CLOSED_EDIT
        )

    if obj_in.name:
        result = await session.execute(
            select(CharityProject).where(
                CharityProject.name == obj_in.name,
                CharityProject.id != db_obj.id,
            )
        )
        if result.scalar_one_or_none():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ERROR_PROJECT_EXISTS
            )

    if obj_in.full_amount is not None and (
        obj_in.full_amount < db_obj.invested_amount
    ):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ERROR_PROJECT_SUM_LESS_INVESTED
        )


def ensure_project_delete_valid(db_obj: CharityProject) -> None:
    if db_obj.invested_amount > 0 or db_obj.fully_invested:
        from app.core.constants import ERROR_PROJECT_DELETE_FORBIDDEN
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ERROR_PROJECT_DELETE_FORBIDDEN
        )
