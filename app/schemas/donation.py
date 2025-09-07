from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class DonationCreate(BaseModel):
    full_amount: int = Field(..., gt=0)
    comment: Optional[str] = Field(None)


class DonationDB(BaseModel):
    full_amount: int
    comment: Optional[str]
    id: int
    create_date: datetime
    user_id: int
    invested_amount: int
    fully_invested: bool
    close_date: Optional[datetime]

    class Config:
        orm_mode = True


class DonationUserResponse(BaseModel):
    full_amount: int
    comment: Optional[str]
    id: int
    create_date: datetime

    class Config:
        orm_mode = True
