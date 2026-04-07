from typing import Annotated

from fastapi import Depends, Request
from sqlalchemy.engine import Engine

from app.core.security import verify_token
from app.services.excel_service import ExcelService


# Auth
AuthDep = Annotated[str, Depends(verify_token)]


# Engine from app.state (set during lifespan)
def get_engine(request: Request) -> Engine:
    return request.app.state.engine


EngineDep = Annotated[Engine, Depends(get_engine)]


# Service factories
def get_excel_service(engine: EngineDep) -> ExcelService:
    return ExcelService(engine)

ExcelDep = Annotated[ExcelService, Depends(get_excel_service)]
