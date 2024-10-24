from enum import StrEnum, auto


class FileType(StrEnum):
    USER_AVATAR = auto()


class FileBucket(StrEnum):
    PICTURES = "pictures"
    DOCUMENT = auto()
    AUDIO = auto()
    VIDEO = auto()
