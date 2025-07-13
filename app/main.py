from fastapi import FastAPI
from app.api.routers import main_router
from app.core.constants import APP_NAME, APP_DESCRIPTION, APP_VERSION

app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=APP_VERSION
)

app.include_router(main_router)
