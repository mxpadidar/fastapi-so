from dataclasses import asdict, dataclass
from typing import Type


@dataclass
class BaseDto[T]:

    def to_dict(self, **kwargs) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls: Type[T], **kwargs) -> T:
        return cls(**kwargs)
