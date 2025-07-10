from fastapi import FastAPI
from app.api.routers import main_router

app = FastAPI(title="QRKot")

app.include_router(main_router)