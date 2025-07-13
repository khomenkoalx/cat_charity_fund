from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import (
    CharityProjectCreate, CharityProjectUpdate,
    CharityProjectDB
)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.core.constants import (
    ALLOWED_FIELDS, ERROR_PROJECT_NOT_FOUND,
    ERROR_PROJECT_PATCH_FORBIDDEN_FIELDS
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
    return await charity_project_crud.create(project, session)


@router.patch('/{project_id}', response_model=CharityProjectDB)
async def update_project(
    project_id: int,
    obj_in: CharityProjectUpdate,
    request: Request,
    session: AsyncSession = Depends(get_async_session),
    user: dict = Depends(current_superuser)
):
    body = await request.json()
    extra_fields = set(body.keys()) - ALLOWED_FIELDS
    if extra_fields:
        raise HTTPException(
            status_code=422,
            detail=ERROR_PROJECT_PATCH_FORBIDDEN_FIELDS + ', '.join(
                extra_fields
            )
        )
    db_obj = await charity_project_crud.get(project_id, session)
    if not db_obj:
        raise HTTPException(status_code=404, detail=ERROR_PROJECT_NOT_FOUND)
    return await charity_project_crud.update(db_obj, obj_in, session)


@router.delete('/{project_id}', response_model=CharityProjectDB)
async def delete_project(
    project_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: dict = Depends(current_superuser)
):
    db_obj = await charity_project_crud.get(project_id, session)
    if not db_obj:
        raise HTTPException(status_code=404, detail=ERROR_PROJECT_NOT_FOUND)
    return await charity_project_crud.remove(db_obj, session)