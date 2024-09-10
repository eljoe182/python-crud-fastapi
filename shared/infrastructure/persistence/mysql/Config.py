from app.config import environment as env


class MySQLConfig:
    def __init__(self):
        host = env.DATABASE.get('HOST')
        port = env.DATABASE.get('PORT')
        user = env.DATABASE.get('USER')
        password = env.DATABASE.get('PASSWORD')
        database = env.DATABASE.get('DATABASE')
        self._CONNECTION_STRING = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

    def get_connection_string(self):
        return self._CONNECTION_STRING
