import os
from pathlib import Path

from dotenv import load_dotenv

_config_dir = Path(__file__).resolve().parent
PROJECT_ROOT = _config_dir.parents[1]
ENV_FILE = PROJECT_ROOT / ".env"

load_dotenv(ENV_FILE, override=True)

# Same directory as this module (app/config); kept for callers that need a string path.
base_dir = str(_config_dir)

PORT = int(os.getenv("PORT", 3000))

DATABASE = {
    "HOST": os.getenv("DB_HOST", "localhost"),
    "PORT": os.getenv("DB_PORT", 3306),
    "USER": os.getenv("DB_USER", "root"),
    "PASSWORD": os.getenv("DB_PASSWORD", "root"),
    "DATABASE": os.getenv("DB_DATABASE", "python-crud"),
}
