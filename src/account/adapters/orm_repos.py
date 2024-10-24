from account.service_layer.repositories import UserRepo
from core.base_classes.orm_repo import ORMRepo


class UserOrmRepo(ORMRepo, UserRepo): ...
