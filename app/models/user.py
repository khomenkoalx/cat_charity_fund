from sqlalchemy import Column, Integer, String
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'user'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(
        String(length=320),
        unique=True,
        index=True,
        nullable=False
    )
    hashed_password: str = Column(String(length=1024), nullable=False)
