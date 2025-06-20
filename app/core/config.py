# core/config.py
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    description: str
    app_author: str
    database_url: str = 'postgres://login:password@127.0.0.1:5432/room_reservation'
    path: str
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'

settings = Settings()
