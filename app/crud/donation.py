from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.donation import Donation
from app.schemas.donation import DonationCreate
from app.services.investment import invest_money
from .base import CRUDBase


class CRUDDonation(CRUDBase):
    def __init__(self):
        super().__init__(Donation)

    async def get_by_user(self, user_id: int, session: AsyncSession):
        result = await session.execute(
            select(self.model).where(self.model.user_id == user_id)
        )
        return result.scalars().all()

    async def create(
        self,
        obj_in: DonationCreate,
        user_id: int,
        session: AsyncSession
    ):
        new_donation = self.model(user_id=user_id, **obj_in.dict())
        session.add(new_donation)
        await session.flush()
        await invest_money(session)
        await session.refresh(new_donation)
        return new_donation


donation_crud = CRUDDonation()
