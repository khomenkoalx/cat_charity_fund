from pydantic import BaseModel, Field, PositiveInt, constr
from typing import Optional
from datetime import datetime

class CharityProjectBase(BaseModel):
    name: constr(strip_whitespace=True, min_length=1, max_length=100)
    description: constr(strip_whitespace=True, min_length=1)
    full_amount: PositiveInt

class CharityProjectCreate(CharityProjectBase):
    pass

class CharityProjectUpdate(BaseModel):
    name: Optional[constr(strip_whitespace=True, min_length=1, max_length=100)]
    description: Optional[constr(strip_whitespace=True, min_length=1)]
    full_amount: Optional[PositiveInt]

class CharityProjectRead(CharityProjectBase):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
