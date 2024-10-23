from abc import ABC, abstractmethod
from typing import Type

from sqlalchemy.orm import Query, Session

from core.abstracts.abstract_entity import AbstractEntity
from core.errors import NotFoundError


class AbstractRepo[T: AbstractEntity](ABC):

    def __init__(self, db: Session):
        self.db = db

    @property
    @abstractmethod
    def entity(self) -> Type[AbstractEntity]:
        raise NotImplementedError

    @property
    def query(self) -> Query:
        return self.db.query(self.entity)

    def add(self, entity: AbstractEntity) -> None:
        self.db.add(entity)

    def commit(self, entity: AbstractEntity | None = None) -> None:
        self.db.commit()
        if entity:
            self.db.refresh(entity)

    def get(self, **kwargs) -> T | None:
        return self.query.filter_by(**kwargs).first()

    def get_or_raise_not_found(self, **kwargs) -> T:
        entity = self.get(**kwargs)
        if entity is None:
            raise NotFoundError(self.entity.to_str())
        return entity

    def get_by_id(self, id: int) -> T | None:
        return self.query.filter_by(id=id).first()

    def delete(self, entity: AbstractEntity) -> None:
        self.db.delete(entity)
        self.commit()
