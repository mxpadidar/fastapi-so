from dataclasses import dataclass

from account.entities.user import User
from account.repositories.user_repo import UserRepo
from account.services.auth_service import AuthService
from core.errors import ConflictError, ValidationError
from core.helpers import validate_email


@dataclass
class HandleRegistrationParams:
    email: str
    first_name: str
    last_name: str
    password: str
    password_confirm: str

    def __post_init__(self) -> None:
        self.email = validate_email(self.email)


def handle_registration(data: HandleRegistrationParams, user_repo: UserRepo, auth_service: AuthService) -> User:
    if data.password != data.password_confirm:
        raise ValidationError("Passwords do not match")

    if user_repo.get(email=data.email):
        raise ConflictError("User already exists")

    user = User(
        email=data.email,
        first_name=data.first_name,
        last_name=data.last_name,
        password=auth_service.get_password_hash(data.password),
    )

    user_repo.add(user)
    user_repo.commit(user)

    return user
