from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class SellerCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None


class SellerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    active: Optional[bool] = None


class SellerOut(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str]
    active: bool
    created_at: datetime

    model_config = {"from_attributes": True}
