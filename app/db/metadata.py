from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    MetaData,
    Numeric,
    String,
    Table,
    text,
)

metadata = MetaData()

sellers_table = Table(
    "sellers",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(100), nullable=False),
    Column("email", String(150), nullable=False, unique=True),
    Column("phone", String(20), nullable=True),
    Column("active", Boolean, nullable=False, server_default=text("true")),
    Column("created_at", DateTime, nullable=False),
)

sales_table = Table(
    "sales",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("seller_id", Integer, ForeignKey("sellers.id", ondelete="RESTRICT"), nullable=False),
    Column("customer_name", String(150), nullable=False),
    Column("total_amount", Numeric(12, 2), nullable=False),
    Column("sale_date", Date, nullable=False),
    Column("status", String(20), nullable=False, server_default=text("'open'")),
    Column("created_at", DateTime, nullable=False),
)

sale_items_table = Table(
    "sale_items",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("sale_id", Integer, ForeignKey("sales.id", ondelete="CASCADE"), nullable=False),
    Column("product_name", String(200), nullable=False),
    Column("quantity", Integer, nullable=False),
    Column("unit_price", Numeric(12, 2), nullable=False),
    Column("total_price", Numeric(12, 2), nullable=False),
)

targets_table = Table(
    "targets",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("seller_id", Integer, ForeignKey("sellers.id", ondelete="CASCADE"), nullable=False),
    Column("month", Integer, nullable=False),
    Column("year", Integer, nullable=False),
    Column("target_amount", Numeric(12, 2), nullable=False),
    Column("achieved_amount", Numeric(12, 2), nullable=False, server_default=text("0")),
)
