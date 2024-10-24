from account.domain.enums import UserGender
from core.base_classes.abstract_entity import AbstractEntity


class User(AbstractEntity):
    id: int
    email: str
    password_hash: str
    fname: str | None
    lname: str | None
    gender: UserGender | None
    is_active: bool

    def __init__(
        self,
        email: str,
        password_hash: str,
        gender: UserGender | None = None,
        fname: str | None = None,
        lname: str | None = None,
        is_active: bool = True,
    ) -> None:
        self.email = email
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.is_active = is_active
        self.password_hash = password_hash

    @property
    def name(self) -> str:
        return f"{self.fname} {self.lname}"

    def to_dict(self, **kwargs) -> dict:
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.fname,
            "last_name": self.lname,
            "is_active": self.is_active,
            **kwargs,
        }
