from app.config import environment as env


class MySQLConfig:
    def __init__(self):
        self._CONNECTION_STRING = f"mysql+pymysql://{env.DATABASE.get('USER')}:{env.DATABASE.get('PASSWORD')}@{env.DATABASE.get('HOST')}:{env.DATABASE.get('PORT')}/{env.DATABASE.get('DATABASE')}"

    def get_connection_string(self):
        return self._CONNECTION_STRING
