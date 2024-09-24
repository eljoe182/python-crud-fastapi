from shared.infrastructure.observability.logger import LoggerObserver
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float, Boolean
from shared.infrastructure.persistence.mysql import MySQLClient


class ProductEntity:
    def __init__(self, client: MySQLClient):
        self.engine = client.get_engine()
        self.metadata = client.get_metadata()
        self.logger = LoggerObserver(__name__)

    def get_table(self):
        return Table(
            "products",
            self.metadata,
            Column("id", Integer, primary_key=True),
            Column("name", String(255), nullable=False),
            Column("description", String(255), nullable=True, default=""),
            Column("price", Float, nullable=True, default=0.0),
            Column("is_active", Boolean, nullable=True, default=False),
        )

    def create_table(self):
        self.logger.info("Creating table products")
        self.get_table().create(self.engine, checkfirst=True)
        self.metadata.create_all(self.engine)
