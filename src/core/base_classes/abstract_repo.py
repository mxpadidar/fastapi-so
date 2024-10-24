from abc import ABC, abstractmethod
from typing import Type

from core.base_classes.abstract_entity import AbstractEntity
from core.errors import NotFoundError


class AbstractRepo[T: AbstractEntity](ABC):
    """
    Abstract base class for a repository that manages entities of type T.
    """

    @property
    @abstractmethod
    def entity(self) -> Type[T]:
        """
        Returns the type of the entity managed by the repository.
        """

        raise NotImplementedError

    def persist(self, entity: T) -> T:
        """
        Adds a new entity to the repository and commits the transaction.
        """

        self.add(entity)
        self.commit(entity)
        return entity

    @abstractmethod
    def add(self, entity: T) -> None:
        """
        Adds a new entity to the repository.
        """

        raise NotImplementedError

    @abstractmethod
    def commit(self, entity: T | None = None) -> None:
        """
        Commits the current transaction.
        If an entity is provided, it refreshes the entity with the latest data.
        """

        raise NotImplementedError

    @abstractmethod
    def delete(self, entity: T) -> None:
        """
        Deletes an entity from the repository.
        """

        raise NotImplementedError

    @abstractmethod
    def get(self, **kwargs) -> T | None:
        """
        Retrieves an entity based on the provided keyword arguments.

        Returns:
            T | None: The retrieved entity, or None if no entity is found.
        """

        raise NotImplementedError

    def get_or_raise_not_found(self, **kwargs) -> T:
        """
        Retrieves an entity based on the provided keyword arguments.
        Raises a NotFoundError if no entity is found.

        Returns:
            T: The retrieved entity.
        """

        entity = self.get(**kwargs)
        if entity is None:
            raise NotFoundError(self.entity.to_str())
        return entity
