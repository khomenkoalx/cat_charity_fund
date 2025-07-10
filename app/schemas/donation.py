from pydantic import BaseModel, condecimal, Field
from datetime import datetime
from typing import Optional

class DonationBase(BaseModel):
    amount: condecimal(gt=0, decimal_places=2)
    comment: Optional[str] = None

class DonationCreate(BaseModel):
    full_amount: int = Field(..., gt=0)
    comment: Optional[str]

class DonationRead(BaseModel):
    id: int
    full_amount: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    user_id: int
    charity_project_id: Optional[int]

    class Config:
        orm_mode = True
