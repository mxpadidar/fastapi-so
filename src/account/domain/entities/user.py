from datetime import UTC, datetime

from account.domain.enums import UserGender
from core.base_classes.abstract_entity import AbstractEntity


class User(AbstractEntity):
    id: int
    email: str
    password_hash: str
    fname: str | None
    lname: str | None
    gender: UserGender | None
    registered_at: datetime
    deactivated_at: datetime | None
    avatar_file_id: int | None

    @property
    def name(self) -> str:
        return f"{self.fname} {self.lname}"

    @property
    def is_active(self) -> bool:
        return self.deactivated_at is None

    @property
    def avatar(self) -> dict | None:
        return {"id": self.avatar_file_id} if self.avatar_file_id else None

    def __init__(
        self,
        email: str,
        password_hash: str,
        gender: UserGender | None = None,
        fname: str | None = None,
        lname: str | None = None,
        avatar_file_id: int | None = None,
    ) -> None:
        self.email = email
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.password_hash = password_hash
        self.avatar_file_id = avatar_file_id

    def deactivate(self) -> None:
        self.deactivated_at = datetime.now(UTC)

    def to_dict(self, avatar: dict | None = None, **kwargs) -> dict:
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.fname,
            "last_name": self.lname,
            "is_active": self.deactivated_at is None,
            "avatar": avatar or self.avatar,
            **kwargs,
        }
