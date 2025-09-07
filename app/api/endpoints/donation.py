from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import DonationCreate, DonationDB, DonationUserResponse
from app.core.db import get_async_session
from app.core.user import current_user, current_superuser
from app.crud.donation import donation_crud
from app.crud.charity_project import charity_project_crud
from app.services.investment import invest_money

router = APIRouter()


@router.get('/', response_model=list[DonationDB])
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session),
    user: dict = Depends(current_superuser)
):
    return await donation_crud.get_multi(session)


@router.post('/', response_model=DonationUserResponse)
async def create_donation(
    donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: dict = Depends(current_user)
):
    new_donation = await donation_crud.create(donation, user.id, session)
    projects = await charity_project_crud.get_unfinished_ordered(session)
    invest_money(new_donation, projects)
    await session.commit()
    await session.refresh(new_donation)
    return new_donation


@router.get('/my', response_model=list[DonationUserResponse])
async def get_my_donations(
    session: AsyncSession = Depends(get_async_session),
    user: dict = Depends(current_user)
):
    return await donation_crud.get_by_user(user.id, session)
