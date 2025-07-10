from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas import CharityProjectCreate, CharityProjectRead

router = APIRouter()

@router.get('/', response_model=List[CharityProjectRead], tags=['Charity Projects'])
async def get_all_projects():
    return []

@router.post('/', response_model=CharityProjectRead, status_code=status.HTTP_201_CREATED, tags=['Charity Projects'])
async def create_project(project: CharityProjectCreate):
    return project

@router.get('/{project_id}', response_model=CharityProjectRead, tags=['Charity Projects'])
async def get_project(project_id: int):

    return {}

@router.delete('/{project_id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Charity Projects'])
async def delete_project(project_id: int):
    return None