from fastapi import APIRouter, status
from typing import List
from app.schemas import DonationCreate, DonationRead

router = APIRouter()

@router.get('/', response_model=List[DonationRead], tags=['Donations'])
async def get_all_donations():
    return []

@router.post('/', response_model=DonationRead, response_model_exclude_none=True)
async def create_donation(donation: DonationCreate):
    return donation
