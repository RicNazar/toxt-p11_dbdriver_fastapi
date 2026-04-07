from sqlalchemy import delete, insert, select, update

from app.db.engine import engine
from app.db.metadata import sellers_table


class SellerRepository:

    @staticmethod
    def get_all() -> list[dict]:
        with engine.connect() as conn:
            rows = conn.execute(select(sellers_table)).mappings().all()
            return [dict(r) for r in rows]

    @staticmethod
    def get_by_id(seller_id: int) -> dict | None:
        with engine.connect() as conn:
            row = conn.execute(
                select(sellers_table).where(sellers_table.c.id == seller_id)
            ).mappings().first()
            return dict(row) if row else None

    @staticmethod
    def create(data: dict) -> dict | None:
        with engine.begin() as conn:
            result = conn.execute(insert(sellers_table).values(**data))
            inserted_id = result.lastrowid
            row = conn.execute(
                select(sellers_table).where(sellers_table.c.id == inserted_id)
            ).mappings().first()
            return dict(row) if row else None

    @staticmethod
    def update(seller_id: int, data: dict) -> dict | None:
        with engine.begin() as conn:
            conn.execute(
                update(sellers_table)
                .where(sellers_table.c.id == seller_id)
                .values(**data)
            )
            row = conn.execute(
                select(sellers_table).where(sellers_table.c.id == seller_id)
            ).mappings().first()
            return dict(row) if row else None

    @staticmethod
    def delete(seller_id: int) -> bool:
        with engine.begin() as conn:
            result = conn.execute(
                delete(sellers_table).where(sellers_table.c.id == seller_id)
            )
            return result.rowcount > 0
