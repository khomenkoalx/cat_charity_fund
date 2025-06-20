from sqlalchemy import Column, Integer, Text, ForeignKey
from app.models.base import BaseCharity

class Donation(BaseCharity):
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    comment = Column(Text, nullable=True)
