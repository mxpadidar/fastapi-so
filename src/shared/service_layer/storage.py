from abc import ABC, abstractmethod

from shared.domain.entities.file import File


class Storage(ABC):

    @abstractmethod
    def upload(self, file: File, file_bytes: bytes) -> str:
        raise NotImplementedError

    @abstractmethod
    def download(self, file: File) -> bytes:
        raise NotImplementedError

    @abstractmethod
    def delete(self, file: File) -> None:
        raise NotImplementedError
