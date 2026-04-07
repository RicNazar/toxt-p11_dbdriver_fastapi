from sqlalchemy import insert, select, update

from app.db.engine import engine
from app.db.metadata import sales_table


class SaleRepository:

    @staticmethod
    def get_all() -> list[dict]:
        with engine.connect() as conn:
            rows = conn.execute(select(sales_table)).mappings().all()
            return [dict(r) for r in rows]

    @staticmethod
    def get_by_id(sale_id: int) -> dict | None:
        with engine.connect() as conn:
            row = conn.execute(
                select(sales_table).where(sales_table.c.id == sale_id)
            ).mappings().first()
            return dict(row) if row else None

    @staticmethod
    def get_by_seller(seller_id: int) -> list[dict]:
        with engine.connect() as conn:
            rows = conn.execute(
                select(sales_table).where(sales_table.c.seller_id == seller_id)
            ).mappings().all()
            return [dict(r) for r in rows]

    @staticmethod
    def create(data: dict) -> dict | None:
        with engine.begin() as conn:
            result = conn.execute(insert(sales_table).values(**data))
            inserted_id = result.lastrowid
            row = conn.execute(
                select(sales_table).where(sales_table.c.id == inserted_id)
            ).mappings().first()
            return dict(row) if row else None

    @staticmethod
    def update(sale_id: int, data: dict) -> dict | None:
        with engine.begin() as conn:
            conn.execute(
                update(sales_table)
                .where(sales_table.c.id == sale_id)
                .values(**data)
            )
            row = conn.execute(
                select(sales_table).where(sales_table.c.id == sale_id)
            ).mappings().first()
            return dict(row) if row else None
