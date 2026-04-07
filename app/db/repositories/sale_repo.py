from sqlalchemy import insert, select, update
from sqlalchemy.engine import Engine

from app.db.metadata import sales_table


class SaleRepository:

    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def get_all(self) -> list[dict]:
        with self.engine.connect() as conn:
            rows = conn.execute(select(sales_table)).mappings().all()
            return [dict(r) for r in rows]

    def get_by_id(self, sale_id: int) -> dict | None:
        with self.engine.connect() as conn:
            row = conn.execute(
                select(sales_table).where(sales_table.c.id == sale_id)
            ).mappings().first()
            return dict(row) if row else None

    def get_by_seller(self, seller_id: int) -> list[dict]:
        with self.engine.connect() as conn:
            rows = conn.execute(
                select(sales_table).where(sales_table.c.seller_id == seller_id)
            ).mappings().all()
            return [dict(r) for r in rows]

    def create(self, data: dict) -> dict | None:
        with self.engine.begin() as conn:
            result = conn.execute(insert(sales_table).values(**data))
            inserted_id = result.lastrowid
            row = conn.execute(
                select(sales_table).where(sales_table.c.id == inserted_id)
            ).mappings().first()
            return dict(row) if row else None

    def update(self, sale_id: int, data: dict) -> dict | None:
        with self.engine.begin() as conn:
            conn.execute(
                update(sales_table)
                .where(sales_table.c.id == sale_id)
                .values(**data)
            )
            row = conn.execute(
                select(sales_table).where(sales_table.c.id == sale_id)
            ).mappings().first()
            return dict(row) if row else None
