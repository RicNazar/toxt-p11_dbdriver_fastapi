from typing import Annotated, Generator

from fastapi import Depends, Request
from sqlalchemy import Connection

from app.core.security import verify_token
from app.services.excel_service import ExcelService

# Auth
AuthDep = Annotated[str, Depends(verify_token)]


# Engine from app.state (set during lifespan)
def get_connection(request: Request) -> Generator[Connection, None, None]:
    with request.app.state.engine.connect() as connection:
            yield connection

def get_transaction(request: Request) -> Generator[Connection, None, None]:
    with request.app.state.engine.begin() as connection:
        yield connection
