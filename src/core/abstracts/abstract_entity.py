from abc import ABC, abstractmethod
from typing import Type


class AbstractEntity(ABC):

    @abstractmethod
    def to_dict(self, **kwargs) -> dict:
        raise NotImplementedError

    @classmethod
    def from_dict(cls, **kwargs) -> Type["AbstractEntity"]:
        raise NotImplementedError

    @classmethod
    def to_str(cls) -> str:
        return cls.__name__
