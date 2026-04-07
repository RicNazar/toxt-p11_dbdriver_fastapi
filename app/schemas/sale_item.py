from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, model_validator


class SaleItemCreate(BaseModel):
    sale_id: int
    product_name: str
    quantity: int
    unit_price: Decimal
    total_price: Optional[Decimal] = None

    @model_validator(mode="after")
    def compute_total_price(self) -> "SaleItemCreate":
        if self.total_price is None:
            self.total_price = Decimal(self.quantity) * self.unit_price
        return self


class SaleItemOut(BaseModel):
    id: int
    sale_id: int
    product_name: str
    quantity: int
    unit_price: Decimal
    total_price: Decimal

    model_config = {"from_attributes": True}
