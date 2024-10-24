from typing import TypedDict, Unpack

from account.domain import errors
from account.service_layer import dtos, repositories, types
from core.types import EmailValidatorFunc


class HandlerParams(TypedDict):
    email: str
    password: str


def handle_login(
    user_repo: repositories.UserRepo,
    token_generator: types.TokenGeneratorFunc,
    password_verifier: types.PasswordVerifierFunc,
    email_validator: EmailValidatorFunc,
    **params: Unpack[HandlerParams],
) -> dtos.TokenDto:
    email = email_validator(params["email"])
    user = user_repo.get(email=email)

    if not user:
        raise errors.UnAuthenticatedError("User not found")

    if not password_verifier(params["password"], user.password_hash):
        raise errors.UnAuthenticatedError("Incorrect password")

    return token_generator(user.id)
