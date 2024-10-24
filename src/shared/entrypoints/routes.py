from fastapi import APIRouter, Depends, File, Form, UploadFile

from core.database import get_db
from shared.adapters.orm_repos import FileOrmRepo
from shared.domain.enums import FileType
from shared.entrypoints.dependencies import get_storage
from shared.entrypoints.schemas import FileResponse
from shared.service_layer import handlers, utils

router = APIRouter()


@router.post("/files/upload", response_model=FileResponse)
def upload_file(
    upload_file: UploadFile = File(...),
    file_type: FileType = Form(...),
    db=Depends(get_db),
    storage=Depends(get_storage),
):
    file = handlers.handle_file_upload(
        file_repo=FileOrmRepo(db),
        storage=storage,
        mime_type_detector=utils.get_file_mime_type,
        filename_generator=utils.generate_unique_filename,
        file_type=file_type,
        name=upload_file.filename,  # type: ignore
        file_bytes=upload_file.file.read(),
    )

    return file.to_dict()
