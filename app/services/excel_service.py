from sqlalchemy.engine import Engine
from typing import Any
from app.db.repositories.excel_repo import ExcelRepository
from app.schemas.excel import ExcelSchema, ExcelExecute, ExcelSearch, ExcelUpdate, ExcelCalculate


class ExcelService:

    def __init__(self, engine: Engine) -> None:
        self.repo = ExcelRepository(engine)

    def schema(self) -> list[ExcelSchema]:
        return self.repo.get_schema()

    def execute_query(self, query: ExcelExecute) -> list[list[Any]]:
        return self.repo.execute_query(query.query)

    def search(self, params: ExcelSearch) -> list[list[Any]]:
        return self.repo.search(params.headers, params.filters, params.relationships, params.approximate)

    def update(self, params: ExcelUpdate) -> list[Any]:
        return self.repo.update(params.data,params.filters,params.relationships)

    def calculate(self, params: ExcelCalculate) -> list[list[Any]]:
        return []