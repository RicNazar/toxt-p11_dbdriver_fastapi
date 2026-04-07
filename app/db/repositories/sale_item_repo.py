from sqlalchemy import delete, insert, select
from sqlalchemy.engine import Engine

from app.db.metadata import sale_items_table


class SaleItemRepository:

    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def get_by_sale(self, sale_id: int) -> list[dict]:
        with self.engine.connect() as conn:
            rows = conn.execute(
                select(sale_items_table).where(sale_items_table.c.sale_id == sale_id)
            ).mappings().all()
            return [dict(r) for r in rows]

    def create(self, data: dict) -> dict | None:
        with self.engine.begin() as conn:
            result = conn.execute(insert(sale_items_table).values(**data))
            inserted_id = result.lastrowid
            row = conn.execute(
                select(sale_items_table).where(sale_items_table.c.id == inserted_id)
            ).mappings().first()
            return dict(row) if row else None

    def delete(self, item_id: int) -> bool:
        with self.engine.begin() as conn:
            result = conn.execute(
                delete(sale_items_table).where(sale_items_table.c.id == item_id)
            )
            return result.rowcount > 0
