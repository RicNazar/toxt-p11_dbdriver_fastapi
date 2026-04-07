from app.db.repositories.sale_item_repo import SaleItemRepository
from app.schemas.sale_item import SaleItemCreate


class SaleItemService:

    @staticmethod
    def list_by_sale(sale_id: int) -> list[dict]:
        return SaleItemRepository.get_by_sale(sale_id)

    @staticmethod
    def create_item(payload: SaleItemCreate) -> dict:
        return SaleItemRepository.create(payload.model_dump())

    @staticmethod
    def delete_item(item_id: int) -> bool:
        return SaleItemRepository.delete(item_id)
