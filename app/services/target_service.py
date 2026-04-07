from app.db.repositories.target_repo import TargetRepository
from app.schemas.target import TargetCreate, TargetUpdate
from app.utils.helpers import safe_pct


class TargetService:

    @staticmethod
    def list_targets() -> list[dict]:
        return TargetRepository.get_all()

    @staticmethod
    def get_target(target_id: int) -> dict | None:
        return TargetRepository.get_by_id(target_id)

    @staticmethod
    def list_by_seller(seller_id: int) -> list[dict]:
        return TargetRepository.get_by_seller(seller_id)

    @staticmethod
    def create_target(payload: TargetCreate) -> dict:
        return TargetRepository.create(payload.model_dump())

    @staticmethod
    def update_target(target_id: int, payload: TargetUpdate) -> dict | None:
        data = payload.model_dump(exclude_none=True)
        if not data:
            return TargetRepository.get_by_id(target_id)
        return TargetRepository.update(target_id, data)

    @staticmethod
    def get_achievement(target_id: int) -> dict | None:
        row = TargetRepository.get_by_id(target_id)
        if not row:
            return None
        return {
            **row,
            "achievement_pct": safe_pct(row["achieved_amount"], row["target_amount"]),
        }
