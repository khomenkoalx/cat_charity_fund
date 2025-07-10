# donation.py
from sqlalchemy import Column, Text, Integer, ForeignKey
from app.models.base import AbstractBaseModel

class Donation(AbstractBaseModel):
    __tablename__ = "donation"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    comment = Column(Text, nullable=True)
