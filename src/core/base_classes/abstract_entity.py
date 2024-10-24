from abc import ABC, abstractmethod


class AbstractEntity[T](ABC):

    @abstractmethod
    def to_dict(self, **kwargs) -> dict:
        raise NotImplementedError

    @classmethod
    def from_dict(cls, **kwargs) -> T:
        raise NotImplementedError

    @classmethod
    def to_str(cls) -> str:
        return cls.__name__
