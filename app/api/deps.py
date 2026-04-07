from typing import Annotated

from fastapi import Depends, Request
from sqlalchemy.engine import Engine

from app.core.security import verify_token
from app.services.sale_item_service import SaleItemService
from app.services.sale_service import SaleService
from app.services.seller_service import SellerService
from app.services.target_service import TargetService

# Auth
AuthDep = Annotated[str, Depends(verify_token)]


# Engine from app.state (set during lifespan)
def get_engine(request: Request) -> Engine:
    return request.app.state.engine


EngineDep = Annotated[Engine, Depends(get_engine)]


# Service factories
def get_seller_service(engine: EngineDep) -> SellerService:
    return SellerService(engine)


def get_sale_service(engine: EngineDep) -> SaleService:
    return SaleService(engine)


def get_sale_item_service(engine: EngineDep) -> SaleItemService:
    return SaleItemService(engine)


def get_target_service(engine: EngineDep) -> TargetService:
    return TargetService(engine)


SellerServiceDep = Annotated[SellerService, Depends(get_seller_service)]
SaleServiceDep = Annotated[SaleService, Depends(get_sale_service)]
SaleItemServiceDep = Annotated[SaleItemService, Depends(get_sale_item_service)]
TargetServiceDep = Annotated[TargetService, Depends(get_target_service)]
