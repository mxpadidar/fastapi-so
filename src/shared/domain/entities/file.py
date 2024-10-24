from datetime import datetime

from core.base_classes.abstract_entity import AbstractEntity
from shared.domain.enums import FileBucket, FileType

FILE_TYPE_BUCKET_MAP = {
    FileType.USER_AVATAR: FileBucket.PICTURES,
}


class File(AbstractEntity):
    id: int
    bucket: FileBucket
    file_type: FileType
    name: str
    size: int
    mime_type: str
    is_used: bool
    metadata: dict | None
    url: str
    created_at: datetime

    def __init__(
        self,
        file_type: FileType,
        name: str,
        size: int,
        mime_type: str,
        is_used: bool = False,
        metadata: dict | None = None,
    ) -> None:
        self.bucket = FILE_TYPE_BUCKET_MAP[file_type]
        self.file_type = file_type
        self.name = name
        self.size = size
        self.mime_type = mime_type
        self.is_used = is_used
        self.metadata = metadata

    @property
    def path(self) -> str:
        return f"{self.file_type}/{self.name}"

    def to_dict(self, **kwargs) -> dict:
        return {
            "id": self.id,
            "file_type": self.file_type,
            "name": self.name,
            "size": self.size,
            "mime_type": self.mime_type,
            "metadata": self.metadata,
            "url": self.url,
            "created_at": self.created_at,
            **kwargs,
        }
