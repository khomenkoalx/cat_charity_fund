from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import DATABASE_URL


class PreBase:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()



Base = declarative_base(cls=PreBase)
engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession)
