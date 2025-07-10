from app.models import Donation
from app.schemas import DonationCreate, DonationUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

class CRUDDonation(CRUDBase):
    async def get_by_user(
        self, user_id: int, session: AsyncSession
    ) -> List[Donation]:
        result = await session.execute(
            select(self.model).where(self.model.user_id == user_id)
        )
        return result.scalars().all()

donation_crud = CRUDDonation(Donation)