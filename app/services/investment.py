from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime
from app.models import CharityProject, Donation


async def invest_money(session: AsyncSession):
    result = await session.execute(
        select(CharityProject).where(~CharityProject.fully_invested).order_by(
            CharityProject.create_date
        )
    )
    projects = result.scalars().all()

    result = await session.execute(
        select(Donation).where(~Donation.fully_invested).order_by(
            Donation.create_date
        )
    )
    donations = result.scalars().all()

    for project in projects:
        for donation in donations:
            if donation.fully_invested or project.fully_invested:
                continue

            available = donation.full_amount - donation.invested_amount
            needed = project.full_amount - project.invested_amount

            amount = min(available, needed)

            if amount > 0:
                donation.invested_amount += amount
                project.invested_amount += amount

                if donation.invested_amount == donation.full_amount:
                    donation.fully_invested = True
                    donation.close_date = datetime.utcnow()

                if project.invested_amount == project.full_amount:
                    project.fully_invested = True
                    project.close_date = datetime.utcnow()

    await session.commit()

    return projects, donations
