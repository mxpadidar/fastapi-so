from typing import Type

from core.base_classes.abstract_repo import AbstractRepo
from shared.domain.entities import File


class FileRepo(AbstractRepo["File"]):

    @property
    def entity(self) -> Type["File"]:
        return File
