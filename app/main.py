from fastapi import FastAPI

from app.api.routes import sale_items, sales, sellers, targets
from app.core.config import settings
from app.core.lifespan import lifespan

app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(sellers.router, prefix="/sellers", tags=["Sellers"])
app.include_router(sales.router, prefix="/sales", tags=["Sales"])
app.include_router(sale_items.router, prefix="/sale-items", tags=["Sale Items"])
app.include_router(targets.router, prefix="/targets", tags=["Targets"])
