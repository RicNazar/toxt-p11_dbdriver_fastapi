from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.engine import engine
from app.db.metadata import metadata


@asynccontextmanager
async def lifespan(app: FastAPI):
    metadata.create_all(engine)
    yield
    engine.dispose()
