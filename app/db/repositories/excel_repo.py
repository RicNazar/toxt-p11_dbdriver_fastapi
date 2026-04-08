from sqlalchemy.engine import Engine
from typing import Any
from app.schemas.excel import ExcelSchema
from app.db.metadata import metadata
from pyeasymatrixdb import DbDriver

class ExcelRepository:

    def __init__(self, engine: Engine) -> None:
        self.engine = engine
        self.driver = DbDriver(metadata,engine)

    def get_schema(self) -> list[ExcelSchema]:
        return self.driver.get_schema()

    def execute_query(self, query: str) -> list[list[Any]]:
        return self.driver.execute(query)

    def search(self,headers:list[list[str]],filters:list[list[str]],relationships:list[list[str]]):
        self.driver.Pesquisar.reset()
        if headers:
            self.driver.Pesquisar.define_header(headers)
        if filters:
            self.driver.Pesquisar.define_filter(filters)
        if relationships:
            self.driver.Pesquisar.define_relationships(relationships)
        return self.driver.Pesquisar.execute()

    def update(self, data:list[list[Any]],filters:list[list[str]],relationships:list[list[str]]):
        self.driver.Atualizar.reset()
        if filters:
            self.driver.Atualizar.define_filter(filters)
        if relationships:
            self.driver.Atualizar.define_relationships(relationships)
        if data:
            self.driver.Atualizar.define_data(data)
        return self.driver.Atualizar.execute()

    def calculate(self, params):
        pass