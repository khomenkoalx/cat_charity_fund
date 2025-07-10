# charity_project.py
from sqlalchemy import Column, String, Text, Integer
from datetime import datetime
from app.models.base import AbstractBaseModel

class CharityProject(AbstractBaseModel):
    __tablename__ = "charity_project"  

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
