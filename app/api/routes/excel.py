from fastapi import APIRouter, HTTPException, status
from typing import Any

from app.api.deps import AuthDep,ExcelDep
from app.schemas.excel import ExcelSchema,ExcelStdResponse,ExcelExecute,ExcelSearch,ExcelUpdate,ExcelCalculate

router = APIRouter()


@router.get("/schema", response_model=ExcelStdResponse[ExcelSchema])
def get_schema(token: AuthDep, svc: ExcelDep):
    response:ExcelStdResponse[ExcelSchema] = {
        "status": "success",
        "message": "Schema retrieved successfully",
        "data": svc.schema()
    }
    return response

@router.post("/execute",response_model=ExcelStdResponse[list[Any]])
def execute_query(token: AuthDep, svc: ExcelDep, payload: ExcelExecute):
    try:
        result = svc.execute_query(payload)
        result_ok: ExcelStdResponse[list[Any]] = {
            "status":"success",
            "message":"Query executed successfully",
            "data":result
        }
        return result_ok
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/search",response_model=ExcelStdResponse[list[Any]])
def search(token: AuthDep, svc: ExcelDep, payload: ExcelSearch):
    try:
        result = svc.search(payload)
        return ExcelStdResponse(status="success", message="Query executed successfully", data=result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/update",response_model=ExcelStdResponse[list[Any]])
def update(token: AuthDep, svc: ExcelDep, payload: ExcelUpdate):
    try:
        result = svc.update(payload)
        return ExcelStdResponse(status="success", message="Query executed successfully", data=result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post("/calculate",response_model=ExcelStdResponse[list[Any]])
def calculate(token: AuthDep, svc: ExcelDep, payload: ExcelCalculate):
    try:
        result = svc.calculate(payload)
        return ExcelStdResponse(status="success", message="Query executed successfully", data=result)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
