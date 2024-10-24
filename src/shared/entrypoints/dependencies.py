from core import settings
from shared.adapters.minio_storage import MinioStorage
from shared.service_layer.storage import Storage


def get_storage() -> Storage:
    return MinioStorage(**settings.MINIO_CONFIG)
