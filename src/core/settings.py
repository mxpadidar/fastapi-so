import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / ".env")


APP_ENV = os.getenv("APP_ENV", "dev")
APP_NAME = os.getenv("APP_NAME", "Scaffold")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")

ALLOWED_ORIGINS = ["http://localhost:*"]

DATABASE = {
    "driver": os.getenv("POSTGRES_DRIVER", "postgresql+psycopg"),
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "db": os.getenv("POSTGRES_DB", "postgres"),
    "user": os.getenv("POSTGRES_USER", "postgres"),
    "password": os.getenv("POSTGRES_PASSWORD", "postgres"),
    "port": int(os.getenv("POSTGRES_PORT", 5432)),
}

AUTH_CONFIG = {
    "secret": os.getenv("AUTH_SECRET", "AUTH_SECRET"),
    "algorithm": os.getenv("AUTH_ALGORITHM", "HS256"),
    "access_exp_min": int(os.getenv("AUTH_ACCESS_EXP_MIN", 60)),
    "refresh_exp_day": int(os.getenv("AUTH_REFRESH_EXP_DAY", 7)),
    "pass_salt": os.getenv("AUTH_PASS_SALT", "salt"),
}
