from typing import TypedDict, Unpack

from account.domain.entities.user import User
from account.service_layer.repositories import UserRepo
from account.service_layer.types import PasswordHashingFunc
from core.errors import ConflictError, ValidationError
from core.types import EmailValidatorFunc


class HandlerParams(TypedDict):
    email: str
    first_name: str
    last_name: str
    password: str
    password_confirm: str


def handle_registration(
    user_repo: UserRepo,
    password_hasher: PasswordHashingFunc,
    email_validator: EmailValidatorFunc,
    **params: Unpack[HandlerParams]
) -> User:
    if params["password"] != params["password_confirm"]:
        raise ValidationError("Passwords do not match")

    email = email_validator(params["email"])

    if user_repo.get(email=params["email"]):
        raise ConflictError("User already exists")

    user = User(
        email=email,
        fname=params["first_name"],
        lname=params["last_name"],
        password_hash=password_hasher(params["password"]),
    )

    user_repo.persist(user)

    return user
