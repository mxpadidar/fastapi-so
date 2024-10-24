from core.base_classes.orm_repo import ORMRepo
from shared.service_layer.repositories import FileRepo


class FileOrmRepo(ORMRepo, FileRepo): ...
