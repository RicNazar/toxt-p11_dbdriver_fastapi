from sqlalchemy.engine import Engine

from app.db.repositories.sale_item_repo import SaleItemRepository
from app.schemas.sale_item import SaleItemCreate


class SaleItemService:

    def __init__(self, engine: Engine) -> None:
        self.repo = SaleItemRepository(engine)

    def list_by_sale(self, sale_id: int) -> list[dict]:
        return self.repo.get_by_sale(sale_id)

    def create_item(self, payload: SaleItemCreate) -> dict:
        return self.repo.create(payload.model_dump())

    def delete_item(self, item_id: int) -> bool:
        return self.repo.delete(item_id)
