from typing import Type

from account.domain.entities.user import User
from core.base_classes.abstract_repo import AbstractRepo


class UserRepo(AbstractRepo["User"]):

    @property
    def entity(self) -> Type["User"]:
        return User
