from datetime import datetime

from app.db.repositories.sale_repo import SaleRepository
from app.schemas.sale import SaleCreate, SaleUpdate


class SaleService:

    @staticmethod
    def list_sales() -> list[dict]:
        return SaleRepository.get_all()

    @staticmethod
    def get_sale(sale_id: int) -> dict | None:
        return SaleRepository.get_by_id(sale_id)

    @staticmethod
    def list_by_seller(seller_id: int) -> list[dict]:
        return SaleRepository.get_by_seller(seller_id)

    @staticmethod
    def create_sale(payload: SaleCreate) -> dict:
        data = payload.model_dump()
        data["created_at"] = datetime.now()
        return SaleRepository.create(data)

    @staticmethod
    def update_sale(sale_id: int, payload: SaleUpdate) -> dict | None:
        data = payload.model_dump(exclude_none=True)
        if not data:
            return SaleRepository.get_by_id(sale_id)
        return SaleRepository.update(sale_id, data)
