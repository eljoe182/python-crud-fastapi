from .Config import MySQLConfig
from sqlalchemy import create_engine, MetaData


class MySQLClient:
    def __init__(self, config: MySQLConfig):
        self.config = config

    def get_metadata(self):
        return MetaData()

    def get_engine(self):
        return create_engine(self.config.get_connection_string())
