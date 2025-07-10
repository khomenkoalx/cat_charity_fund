# abstract_base.py
from sqlalchemy import Column, DateTime, Boolean, Integer
from datetime import datetime
from app.core.db import Base

class AbstractBaseModel(Base):
    __abstract__ = True

    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.utcnow)
    close_date = Column(DateTime, nullable=True)
