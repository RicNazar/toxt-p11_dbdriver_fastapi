from sqlalchemy.engine import Engine

from app.db.repositories.target_repo import TargetRepository
from app.schemas.target import TargetCreate, TargetUpdate
from app.utils.helpers import safe_pct


class TargetService:

    def __init__(self, engine: Engine) -> None:
        self.repo = TargetRepository(engine)

    def list_targets(self) -> list[dict]:
        return self.repo.get_all()

    def get_target(self, target_id: int) -> dict | None:
        return self.repo.get_by_id(target_id)

    def list_by_seller(self, seller_id: int) -> list[dict]:
        return self.repo.get_by_seller(seller_id)

    def create_target(self, payload: TargetCreate) -> dict:
        return self.repo.create(payload.model_dump())

    def update_target(self, target_id: int, payload: TargetUpdate) -> dict | None:
        data = payload.model_dump(exclude_none=True)
        if not data:
            return self.repo.get_by_id(target_id)
        return self.repo.update(target_id, data)

    def get_achievement(self, target_id: int) -> dict | None:
        row = self.repo.get_by_id(target_id)
        if not row:
            return None
        return {
            **row,
            "achievement_pct": safe_pct(row["achieved_amount"], row["target_amount"]),
        }
