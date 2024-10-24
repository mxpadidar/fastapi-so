import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv(BASE_DIR / ".env")


APP_ENV = os.getenv("APP_ENV", "dev")
APP_NAME = os.getenv("APP_NAME", "Scaffold")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")

ALLOWED_ORIGINS = ["http://localhost:*"]

PASSWORD_SALT = os.getenv("PASSWORD_SALT", "salt")

SECRET_KEY = os.getenv("SECRET_KEY", "secret-key")

JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_ACCESS_EXP_MIN = int(os.getenv("JWT_ACCESS_EXP_MIN", "60"))
JWT_REFRESH_EXP_DAY = int(os.getenv("JWT_REFRESH_EXP_DAY", "7"))

DB_DRIVER = os.getenv("DB_DRIVER", "postgresql+psycopg")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
DB_NAME = os.getenv("POSTGRES_DB", "postgres")


MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "localhost:9000")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "minio")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "minio123")

DATABASE_CONFIG = {
    "driver": DB_DRIVER,
    "host": DB_HOST,
    "port": DB_PORT,
    "user": DB_USER,
    "password": DB_PASSWORD,
    "db": DB_NAME,
}


TOKEN_CONFIG = {
    "secret_key": SECRET_KEY,
    "algorithm": JWT_ALGORITHM,
    "access_exp_min": JWT_ACCESS_EXP_MIN,
    "refresh_exp_day": JWT_REFRESH_EXP_DAY,
}

MINIO_CONFIG = {
    "endpoint": MINIO_ENDPOINT,
    "access_key": MINIO_ACCESS_KEY,
    "secret_key": MINIO_SECRET_KEY,
}
