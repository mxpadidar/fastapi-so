from typing import TypedDict, Unpack

from shared.domain.entities.file import File
from shared.domain.enums import FileType
from shared.service_layer.repositories import FileRepo
from shared.service_layer.storage import Storage
from shared.service_layer.types import FilenameGeneratorFunc, MimeTypeDetectorFunc


class HandlerParams(TypedDict):
    file_type: FileType
    name: str
    file_bytes: bytes


def handle_file_upload(
    file_repo: FileRepo,
    storage: Storage,
    filename_generator: FilenameGeneratorFunc,
    mime_type_detector: MimeTypeDetectorFunc,
    **params: Unpack[HandlerParams],
) -> File:
    file = File(
        file_type=params["file_type"],
        name=filename_generator(params["name"]),
        size=len(params["file_bytes"]),
        mime_type=mime_type_detector(params["file_bytes"]),
    )

    file_url = storage.upload(file, params["file_bytes"])
    file.url = file_url
    file_repo.persist(file)

    return file
