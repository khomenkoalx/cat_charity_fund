from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import (
    CharityProjectCreate, CharityProjectUpdate,
    CharityProjectDB
)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud
from app.core.constants import (
    ALLOWED_FIELDS, ERROR_PROJECT_NOT_FOUND,
    ERROR_PROJECT_PATCH_FORBIDDEN_FIELDS
)
from app.services.investment import invest_money
from app.api.validators.charity_project import (
    validate_patch_fields,
    ensure_project_exists,
    ensure_project_create_valid,
    ensure_project_update_valid,
    ensure_project_delete_valid,
)

router = APIRouter()


@router.get('/', response_model=list[CharityProjectDB])
async def get_projects(session: AsyncSession = Depends(get_async_session)):
    return await charity_project_crud.get_multi(session)


@router.post('/', response_model=CharityProjectDB)
async def create_project(
    project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session),
    user: dict = Depends(current_superuser)
):
    await ensure_project_create_valid(project, session)
    new_project = await charity_project_crud.create(project, session)
    donations = await donation_crud.get_unfinished_ordered(session)
    invest_money(new_project, donations)
    await session.commit()
    await session.refresh(new_project)
    return new_project


@router.patch('/{project_id}', response_model=CharityProjectDB)
async def update_project(
    project_id: int,
    obj_in: CharityProjectUpdate,
    request: Request,
    session: AsyncSession = Depends(get_async_session),
    user: dict = Depends(current_superuser)
):
    body = await request.json()
    validate_patch_fields(
        body,
        ALLOWED_FIELDS,
        ERROR_PROJECT_PATCH_FORBIDDEN_FIELDS
    )
    db_obj = await charity_project_crud.get(project_id, session)
    ensure_project_exists(db_obj, ERROR_PROJECT_NOT_FOUND)
    await ensure_project_update_valid(db_obj, obj_in, session)
    updated = await charity_project_crud.update(db_obj, obj_in, session)
    await session.commit()
    await session.refresh(updated)
    return updated


@router.delete('/{project_id}', response_model=CharityProjectDB)
async def delete_project(
    project_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: dict = Depends(current_superuser)
):
    db_obj = await charity_project_crud.get(project_id, session)
    ensure_project_exists(db_obj, ERROR_PROJECT_NOT_FOUND)
    ensure_project_delete_valid(db_obj)
    removed = await charity_project_crud.remove(db_obj, session)
    await session.commit()
    return removed
