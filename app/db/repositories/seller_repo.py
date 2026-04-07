from sqlalchemy import delete, insert, select, update
from sqlalchemy.engine import Engine

from app.db.metadata import sellers_table


class SellerRepository:

    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def get_all(self) -> list[dict]:
        with self.engine.connect() as conn:
            rows = conn.execute(select(sellers_table)).mappings().all()
            return [dict(r) for r in rows]

    def get_by_id(self, seller_id: int) -> dict | None:
        with self.engine.connect() as conn:
            row = conn.execute(
                select(sellers_table).where(sellers_table.c.id == seller_id)
            ).mappings().first()
            return dict(row) if row else None

    def create(self, data: dict) -> dict | None:
        with self.engine.begin() as conn:
            result = conn.execute(insert(sellers_table).values(**data))
            inserted_id = result.lastrowid
            row = conn.execute(
                select(sellers_table).where(sellers_table.c.id == inserted_id)
            ).mappings().first()
            return dict(row) if row else None

    def update(self, seller_id: int, data: dict) -> dict | None:
        with self.engine.begin() as conn:
            conn.execute(
                update(sellers_table)
                .where(sellers_table.c.id == seller_id)
                .values(**data)
            )
            row = conn.execute(
                select(sellers_table).where(sellers_table.c.id == seller_id)
            ).mappings().first()
            return dict(row) if row else None

    def delete(self, seller_id: int) -> bool:
        with self.engine.begin() as conn:
            result = conn.execute(
                delete(sellers_table).where(sellers_table.c.id == seller_id)
            )
            return result.rowcount > 0
