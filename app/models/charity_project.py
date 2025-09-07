from sqlalchemy import Column, String, Text
from app.models.base import BaseModel


class CharityProject(BaseModel):
    __tablename__ = 'charity_project'

    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        base_repr = super().__repr__()
        return f'{base_repr[:-1]}, name="{self.name}")>'