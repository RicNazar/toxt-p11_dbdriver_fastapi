from sqlalchemy.engine import Engine
from typing import Any
from app.schemas.excel import ExcelSchema, ExcelSchemaColumn
from app.db.metadata import metadata
from pyeasymatrixdb import DbDriver

class ExcelRepository:

    def __init__(self, engine: Engine) -> None:
        self.engine = engine
        self.driver = DbDriver(metadata,engine)

    def get_schema(self) -> list[ExcelSchema]:
        sch = self.driver.get_schema()
        
        #Turn column definitions into ExcelSchemaColumn
        result: list[ExcelSchema] = []
        for table, columns in sch.items():
            #add table if necessary
            result.append(ExcelSchema(
                table=table,
                columns={col_name: ExcelSchemaColumn(
                    type=str(col_def['type']),
                    primary=col_def['primary'],
                    unique=col_def['unique'],
                    default=col_def['default'],
                    nullable=col_def['nullable']
                ) for col_name, col_def in columns.items()}
            ))
        return result

    def execute_query(self, query: str) -> list[list[Any]]:
        result = self.driver.execute(query)
        return result

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