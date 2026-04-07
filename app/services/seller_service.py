from datetime import datetime

from sqlalchemy.engine import Engine

from app.db.repositories.seller_repo import SellerRepository
from app.schemas.seller import SellerCreate, SellerUpdate


class SellerService:

    def __init__(self, engine: Engine) -> None:
        self.repo = SellerRepository(engine)

    def list_sellers(self) -> list[dict]:
        return self.repo.get_all()

    def get_seller(self, seller_id: int) -> dict | None:
        return self.repo.get_by_id(seller_id)

    def create_seller(self, payload: SellerCreate) -> dict:
        data = payload.model_dump()
        data["created_at"] = datetime.now()
        return self.repo.create(data)

    def update_seller(self, seller_id: int, payload: SellerUpdate) -> dict | None:
        data = payload.model_dump(exclude_none=True)
        if not data:
            return self.repo.get_by_id(seller_id)
        return self.repo.update(seller_id, data)

    def delete_seller(self, seller_id: int) -> bool:
        return self.repo.delete(seller_id)
