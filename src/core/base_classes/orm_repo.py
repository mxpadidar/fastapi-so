from sqlalchemy.orm import Query, Session

from core.base_classes.abstract_entity import AbstractEntity
from core.base_classes.abstract_repo import AbstractRepo


class ORMRepo[T: AbstractEntity](AbstractRepo[T]):
    """
    This class is a SQLAlchemy implementation of the AbstractRepo interface.
    It implements the AbstractRepo interface and is designed to work with SQLAlchemy ORM entities.
    """

    def __init__(self, db: Session):
        self.db = db

    @property
    def query(self) -> Query:
        return self.db.query(self.entity)

    def get(self, **kwargs) -> T | None:
        return self.query.filter_by(**kwargs).first()

    def add(self, entity: T) -> None:
        self.db.add(entity)

    def delete(self, entity: T) -> None:
        self.db.delete(entity)
        self.commit()

    def commit(self, entity: T | None = None) -> None:
        self.db.commit()
        if entity:
            self.db.refresh(entity)
