from sqlalchemy import insert, select, update
from sqlalchemy.engine import Engine

from app.db.metadata import targets_table


class TargetRepository:

    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def get_all(self) -> list[dict]:
        with self.engine.connect() as conn:
            rows = conn.execute(select(targets_table)).mappings().all()
            return [dict(r) for r in rows]

    def get_by_id(self, target_id: int) -> dict | None:
        with self.engine.connect() as conn:
            row = conn.execute(
                select(targets_table).where(targets_table.c.id == target_id)
            ).mappings().first()
            return dict(row) if row else None

    def get_by_seller(self, seller_id: int) -> list[dict]:
        with self.engine.connect() as conn:
            rows = conn.execute(
                select(targets_table).where(targets_table.c.seller_id == seller_id)
            ).mappings().all()
            return [dict(r) for r in rows]

    def create(self, data: dict) -> dict | None:
        with self.engine.begin() as conn:
            result = conn.execute(insert(targets_table).values(**data))
            inserted_id = result.lastrowid
            row = conn.execute(
                select(targets_table).where(targets_table.c.id == inserted_id)
            ).mappings().first()
            return dict(row) if row else None

    def update(self, target_id: int, data: dict) -> dict | None:
        with self.engine.begin() as conn:
            conn.execute(
                update(targets_table)
                .where(targets_table.c.id == target_id)
                .values(**data)
            )
            row = conn.execute(
                select(targets_table).where(targets_table.c.id == target_id)
            ).mappings().first()
            return dict(row) if row else None
