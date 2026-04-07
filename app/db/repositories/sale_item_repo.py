from sqlalchemy import delete, insert, select

from app.db.engine import engine
from app.db.metadata import sale_items_table


class SaleItemRepository:

    @staticmethod
    def get_by_sale(sale_id: int) -> list[dict]:
        with engine.connect() as conn:
            rows = conn.execute(
                select(sale_items_table).where(sale_items_table.c.sale_id == sale_id)
            ).mappings().all()
            return [dict(r) for r in rows]

    @staticmethod
    def create(data: dict) -> dict | None:
        with engine.begin() as conn:
            result = conn.execute(insert(sale_items_table).values(**data))
            inserted_id = result.lastrowid
            row = conn.execute(
                select(sale_items_table).where(sale_items_table.c.id == inserted_id)
            ).mappings().first()
            return dict(row) if row else None

    @staticmethod
    def delete(item_id: int) -> bool:
        with engine.begin() as conn:
            result = conn.execute(
                delete(sale_items_table).where(sale_items_table.c.id == item_id)
            )
            return result.rowcount > 0
