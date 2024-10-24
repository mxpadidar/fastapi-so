from typing import TypedDict, Unpack

from account.service_layer import errors, repositories, types
from account.service_layer.dtos import TokenDto
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
) -> TokenDto:
    email = email_validator(params["email"])
    user = user_repo.get(email=email)

    if not user:
        raise errors.UnAuthenticatedError("User not found")

    if not password_verifier(params["password"], user.password_hash):
        raise errors.UnAuthenticatedError("Incorrect password")

    return token_generator(user.id)
