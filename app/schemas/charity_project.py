from pydantic import BaseModel, Field, constr
from typing import Optional
from datetime import datetime


class CharityProjectCreate(BaseModel):
    name: constr(min_length=1, max_length=100)
    description: constr(min_length=1)
    full_amount: int = Field(..., gt=0)


class CharityProjectUpdate(BaseModel):
    name: Optional[constr(min_length=1, max_length=100)] = None
    description: Optional[constr(min_length=1)] = None
    full_amount: Optional[int] = Field(None, gt=0)


class CharityProjectDB(BaseModel):
    name: str
    description: str
    full_amount: int
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
