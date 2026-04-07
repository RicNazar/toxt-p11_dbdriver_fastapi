from sqlalchemy import create_engine

from app.core.config import settings

engine = create_engine(
    settings.db_url,
    pool_pre_ping=True,
    future=True,
    echo=settings.debug,
)
