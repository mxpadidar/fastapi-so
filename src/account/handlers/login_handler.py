from dataclasses import dataclass

from account.repositories.user_repo import UserRepo
from account.services.auth_service import AuthService, Token
from core.errors import UnAuthenticatedError
from core.helpers import validate_email


@dataclass
class HandleLoginParams:
    email: str
    password: str

    def __post_init__(self) -> None:
        self.email = validate_email(self.email)


def handle_login(params: HandleLoginParams, user_repo: UserRepo, auth_service: AuthService) -> Token:
    user = user_repo.get(email=params.email)

    if not user:
        raise UnAuthenticatedError("User not found")

    if not auth_service.verify_password(params.password, user.password):
        raise UnAuthenticatedError("Incorrect password")

    return auth_service.generate_tokens(user.id)
