from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, registry, sessionmaker

from core.settings import DATABASE as DB

conn_string = f"{DB['driver']}://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['db']}"

engine = create_engine(url=conn_string)

session_maker = sessionmaker(bind=engine)

mapper_registry = registry()


def get_db() -> Generator[Session]:
    db = session_maker()
    try:
        yield db
    finally:
        db.close()
