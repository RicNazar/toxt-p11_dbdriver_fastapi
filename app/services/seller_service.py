from datetime import datetime

from app.db.repositories.seller_repo import SellerRepository
from app.schemas.seller import SellerCreate, SellerUpdate


class SellerService:

    @staticmethod
    def list_sellers() -> list[dict]:
        return SellerRepository.get_all()

    @staticmethod
    def get_seller(seller_id: int) -> dict | None:
        return SellerRepository.get_by_id(seller_id)

    @staticmethod
    def create_seller(payload: SellerCreate) -> dict:
        data = payload.model_dump()
        data["created_at"] = datetime.now()
        return SellerRepository.create(data)

    @staticmethod
    def update_seller(seller_id: int, payload: SellerUpdate) -> dict | None:
        data = payload.model_dump(exclude_none=True)
        if not data:
            return SellerRepository.get_by_id(seller_id)
        return SellerRepository.update(seller_id, data)

    @staticmethod
    def delete_seller(seller_id: int) -> bool:
        return SellerRepository.delete(seller_id)
