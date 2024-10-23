from typing import Type

from account.entities.user import User
from core.abstracts.abstract_repo import AbstractRepo


class UserRepo(AbstractRepo[User]):

    @property
    def entity(self) -> Type[User]:
        return User
