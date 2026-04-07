from contextlib import asynccontextmanager
from pyeasymatrixdb import DbDriver
from fastapi import FastAPI

from app.db.engine import engine
from app.db.metadata import metadata


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.engine = engine
    app.state.metadata = metadata
    app.state.db_driver = DbDriver(metadata,engine)
    metadata.create_all(engine)
    yield
    engine.dispose()
    app.state.db_driver = None