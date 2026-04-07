from datetime import datetime

from sqlalchemy.engine import Engine

from app.db.repositories.sale_repo import SaleRepository
from app.schemas.sale import SaleCreate, SaleUpdate


class SaleService:

    def __init__(self, engine: Engine) -> None:
        self.repo = SaleRepository(engine)

    def list_sales(self) -> list[dict]:
        return self.repo.get_all()

    def get_sale(self, sale_id: int) -> dict | None:
        return self.repo.get_by_id(sale_id)

    def list_by_seller(self, seller_id: int) -> list[dict]:
        return self.repo.get_by_seller(seller_id)

    def create_sale(self, payload: SaleCreate) -> dict:
        data = payload.model_dump()
        data["created_at"] = datetime.now()
        return self.repo.create(data)

    def update_sale(self, sale_id: int, payload: SaleUpdate) -> dict | None:
        data = payload.model_dump(exclude_none=True)
        if not data:
            return self.repo.get_by_id(sale_id)
        return self.repo.update(sale_id, data)
