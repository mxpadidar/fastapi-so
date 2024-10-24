from datetime import UTC, datetime, timedelta
from typing import TypedDict, Unpack

import jwt

from account.domain import errors
from account.service_layer import types
from account.service_layer.dtos import TokenDto


class TokenConfig(TypedDict):
    secret_key: str
    algorithm: str
    access_exp_min: int
    refresh_exp_day: int


def token_parser_closure(**config: Unpack[TokenConfig]) -> types.TokenParserFunc:

    def parse_token(token: str) -> int:
        try:
            payload: dict = jwt.decode(token, config["secret_key"], algorithms=[config["algorithm"]])
            return payload["sub"]
        except (
            jwt.ExpiredSignatureError,
            jwt.InvalidSignatureError,
            jwt.InvalidTokenError,
        ):
            raise errors.UnAuthenticatedError("Invalid token.")

    return parse_token


def token_generator_closure(**config: Unpack[TokenConfig]) -> types.TokenGeneratorFunc:
    """
    Generate access and refresh tokens.
    """

    def generate_token(user_id: int) -> TokenDto:
        access_payload = {
            "sub": user_id,
            "type": "access",
            "exp": (datetime.now(tz=UTC) + timedelta(minutes=config["access_exp_min"])).timestamp(),
        }

        refresh_payload = {
            "sub": user_id,
            "type": "refresh",
            "exp": (datetime.now(tz=UTC) + timedelta(days=config["refresh_exp_day"])).timestamp(),
        }

        return TokenDto(
            access_token=jwt.encode(access_payload, config["secret_key"], algorithm=config["algorithm"]),
            refresh_token=jwt.encode(refresh_payload, config["secret_key"], algorithm=config["algorithm"]),
            token_type="bearer",
        )

    return generate_token


def authorization_header_parser(authorization_header: str | None) -> str:
    """
    Parse the bearer token from the authorization header.
    """

    if not authorization_header:
        raise errors.UnAuthenticatedError("Missing authorization header.")

    parts = authorization_header.split()

    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise errors.UnAuthenticatedError("Invalid authorization header format.")

    return parts[1]
