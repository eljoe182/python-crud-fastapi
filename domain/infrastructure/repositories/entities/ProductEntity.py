from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float, Boolean
from domain.infrastructure.persistence.mysql.Client import MySQLClient


class ProductEntity:
    def __init__(self, client: MySQLClient):
        self.engine = client.get_engine()
        self.metadata = client.get_metadata()

    def get_table(self):
        return Table(
            "products",
            self.metadata,
            Column("id", Integer, primary_key=True),
            Column("name", String(255)),
            Column("description", String(255)),
            Column("price", Float),
            Column("is_active", Boolean),
        )

    def create_table(self):
        self.metadata.create_all(self.engine)
