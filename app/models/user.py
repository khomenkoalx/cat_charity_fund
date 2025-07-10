from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from app.core.db import Base  # твоя базовая модель с declarative_base()

class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"  # или "users" — как в твоей базе данных

    id: Mapped[int] = Column(Integer, primary_key=True)
    email: Mapped[str] = Column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = Column(String(length=1024), nullable=False)