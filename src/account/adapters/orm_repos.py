from account.service_layer.repositories.user_repo import UserRepo
from core.base_classes.orm_repo import ORMRepo


class UserOrmRepo(ORMRepo, UserRepo): ...
