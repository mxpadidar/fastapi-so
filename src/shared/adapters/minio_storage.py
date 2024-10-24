from io import BytesIO
from typing import TypedDict, Unpack

from minio import Minio, S3Error

from shared.domain.entities.file import File
from shared.service_layer.storage import Storage


class MinioConfig(TypedDict):
    endpoint: str
    access_key: str
    secret_key: str


class MinioStorage(Storage):

    _client: Minio | None = None

    def __init__(self, **config: Unpack[MinioConfig]) -> None:
        self._endpoint = config["endpoint"]
        self._access_key = config["access_key"]
        self._secret_key = config["secret_key"]

    @property
    def client(self) -> Minio:
        if self._client is None:
            try:
                client = Minio(
                    endpoint=self._endpoint,
                    access_key=self._access_key,
                    secret_key=self._secret_key,
                    secure=False,
                )
            except S3Error as error:
                raise error

            self._client = client
        return self._client

    def upload(self, file: File, file_bytes: bytes) -> str:
        self._ensure_bucket_exists(file.bucket)
        try:
            self.client.put_object(
                bucket_name=file.bucket,
                object_name=file.path,
                data=BytesIO(file_bytes),
                length=file.size,
            )
        except S3Error as error:
            raise error
        return self._get_url(file)

    def download(self, file: File) -> bytes:
        try:
            result = self.client.get_object(bucket_name=file.bucket, object_name=file.path)
            return result.read()
        except S3Error as error:
            raise error

    def delete(self, file: File) -> None:
        try:
            self.client.remove_object(bucket_name=file.bucket, object_name=file.path)
        except S3Error as error:
            raise error

    def _ensure_bucket_exists(self, bucket: str) -> None:
        try:
            bucket_exist = self.client.bucket_exists(bucket_name=bucket)
        except S3Error as error:
            raise error
        if bucket_exist:
            return
        self.client.make_bucket(bucket)

    def _get_url(self, file: File) -> str:
        return f"{self._endpoint}/{file.bucket}/{file.path}"
        # return self.client.presigned_get_object(bucket_name=bucket, object_name=file_name)
