from fastapi import APIRouter, HTTPException, status

from app.api.deps import AuthDep
from app.schemas.sale_item import SaleItemCreate, SaleItemOut
from app.services.sale_item_service import SaleItemService

router = APIRouter()


@router.get("/sale/{sale_id}", response_model=list[SaleItemOut])
def list_items_by_sale(sale_id: int, token: AuthDep):
    return SaleItemService.list_by_sale(sale_id)


@router.post("/", response_model=SaleItemOut, status_code=status.HTTP_201_CREATED)
def create_item(payload: SaleItemCreate, token: AuthDep):
    return SaleItemService.create_item(payload)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int, token: AuthDep):
    if not SaleItemService.delete_item(item_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
