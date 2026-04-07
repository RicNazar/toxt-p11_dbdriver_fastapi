from fastapi import APIRouter, HTTPException, status

from app.api.deps import AuthDep, SellerServiceDep
from app.schemas.seller import SellerCreate, SellerOut, SellerUpdate

router = APIRouter()


@router.get("/", response_model=list[SellerOut])
def list_sellers(token: AuthDep, svc: SellerServiceDep):
    return svc.list_sellers()


@router.get("/{seller_id}", response_model=SellerOut)
def get_seller(seller_id: int, token: AuthDep, svc: SellerServiceDep):
    seller = svc.get_seller(seller_id)
    if not seller:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seller not found")
    return seller


@router.post("/", response_model=SellerOut, status_code=status.HTTP_201_CREATED)
def create_seller(payload: SellerCreate, token: AuthDep, svc: SellerServiceDep):
    return svc.create_seller(payload)


@router.patch("/{seller_id}", response_model=SellerOut)
def update_seller(seller_id: int, payload: SellerUpdate, token: AuthDep, svc: SellerServiceDep):
    seller = svc.update_seller(seller_id, payload)
    if not seller:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seller not found")
    return seller


@router.delete("/{seller_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_seller(seller_id: int, token: AuthDep, svc: SellerServiceDep):
    if not svc.delete_seller(seller_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Seller not found")

