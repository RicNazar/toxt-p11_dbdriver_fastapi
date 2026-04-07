from fastapi import APIRouter, HTTPException, status

from app.api.deps import AuthDep
from app.schemas.sale import SaleCreate, SaleOut, SaleUpdate
from app.services.sale_service import SaleService

router = APIRouter()


@router.get("/", response_model=list[SaleOut])
def list_sales(token: AuthDep):
    return SaleService.list_sales()


# More specific route must come before /{sale_id} to avoid path conflicts
@router.get("/seller/{seller_id}", response_model=list[SaleOut])
def list_sales_by_seller(seller_id: int, token: AuthDep):
    return SaleService.list_by_seller(seller_id)


@router.get("/{sale_id}", response_model=SaleOut)
def get_sale(sale_id: int, token: AuthDep):
    sale = SaleService.get_sale(sale_id)
    if not sale:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sale not found")
    return sale


@router.post("/", response_model=SaleOut, status_code=status.HTTP_201_CREATED)
def create_sale(payload: SaleCreate, token: AuthDep):
    return SaleService.create_sale(payload)


@router.patch("/{sale_id}", response_model=SaleOut)
def update_sale(sale_id: int, payload: SaleUpdate, token: AuthDep):
    sale = SaleService.update_sale(sale_id, payload)
    if not sale:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sale not found")
    return sale
