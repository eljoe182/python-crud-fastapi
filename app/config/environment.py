import os
from dotenv import load_dotenv

load_dotenv()

DATABASE = {
    "HOST": os.getenv("DB_HOST"),
    "PORT": os.getenv("DB_PORT"),
    "USER": os.getenv("DB_USER"),
    "PASSWORD": os.getenv("DB_PASSWORD"),
    "DATABASE": os.getenv("DB_DATABASE"),
}
