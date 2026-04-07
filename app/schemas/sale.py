from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class SaleCreate(BaseModel):
    seller_id: int
    customer_name: str
    total_amount: Decimal
    sale_date: date
    status: str = "open"


class SaleUpdate(BaseModel):
    customer_name: Optional[str] = None
    total_amount: Optional[Decimal] = None
    sale_date: Optional[date] = None
    status: Optional[str] = None


class SaleOut(BaseModel):
    id: int
    seller_id: int
    customer_name: str
    total_amount: Decimal
    sale_date: date
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}
