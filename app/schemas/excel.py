from pydantic import BaseModel
from typing import Literal, TypeVar, Generic, Any
from pydantic import BaseModel, model_validator
T = TypeVar('T')

class ExcelSchemaColumn(BaseModel):
    type: str
    primary: bool = False
    unique: bool = False
    default: Any = None
    nullable: bool = True

class ExcelSchema(BaseModel):
    table: str
    columns: dict[str,ExcelSchemaColumn] = []

class ExcelStdResponse(BaseModel,Generic[T]):
    status: Literal['success','error']
    message: str
    data: list[T] | None = None

# - Requests

class ExcelExecute(BaseModel):
    query: str

    @model_validator(mode='after')
    def validate_query(self) -> 'ExcelExecute':
        """Validate if query is a non-empty valid string"""
        if  len(self.query.strip()) == 0:
            raise ValueError('query must be a non-empty string')
        return self

class ExcelSearch(BaseModel):
    headers: list[list[str]]
    filters: list[list[str]] | None = None
    relationships: list[list[str]] | None = None

class ExcelUpdate(BaseModel):
    data: list[list[Any]]
    filters: list[list[str]] | None = None
    relationships: list[list[str]] | None = None

class ExcelCalculate(BaseModel):
    headers: list[list[str]]
    filters: list[list[str]] | None = None
    relationships: list[list[str]] | None = None
    grup_by: list[list[str]] | None = None
    calculations: list[list[str]] | None = None