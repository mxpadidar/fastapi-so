from core.abstracts.abstract_entity import AbstractEntity


class User(AbstractEntity):
    id: int
    email: str
    first_name: str
    last_name: str
    password: str
    is_active: bool

    def __init__(self, email: str, password: str, first_name: str, last_name: str, is_active: bool = True) -> None:
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = is_active

    def to_dict(self, **kwargs) -> dict:
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_active": self.is_active,
            **kwargs,
        }
