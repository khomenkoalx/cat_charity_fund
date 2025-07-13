from sqlalchemy import Column, Integer, DateTime, Boolean
from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr
from app.core.db import Base


class BaseModel(Base):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    create_date = Column(DateTime, default=datetime.utcnow)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)
    close_date = Column(DateTime)
