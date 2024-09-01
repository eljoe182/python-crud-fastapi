from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float, Boolean
from config.database import metadata, engine

product_model = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("description", String(255)),
    Column("price", Float),
    Column("is_active", Boolean),
)

metadata.create_all(engine)
