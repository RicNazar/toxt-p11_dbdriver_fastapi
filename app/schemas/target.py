from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, field_validator


class TargetCreate(BaseModel):
    seller_id: int
    month: int
    year: int
    target_amount: Decimal
    achieved_amount: Decimal = Decimal("0")

    @field_validator("month")
    @classmethod
    def validate_month(cls, v: int) -> int:
        if not 1 <= v <= 12:
            raise ValueError("month must be between 1 and 12")
        return v


class TargetUpdate(BaseModel):
    target_amount: Optional[Decimal] = None
    achieved_amount: Optional[Decimal] = None


class TargetOut(BaseModel):
    id: int
    seller_id: int
    month: int
    year: int
    target_amount: Decimal
    achieved_amount: Decimal

    model_config = {"from_attributes": True}


class TargetAchievement(TargetOut):
    achievement_pct: float
