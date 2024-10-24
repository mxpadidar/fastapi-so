from datetime import datetime, timedelta

import bcrypt
import jwt
import pytest
from freezegun import freeze_time

from account.service_layer.auth_service import AuthService
from core.errors import UnAuthenticatedError


def test_get_password_hash(auth_service: AuthService):
    password = "test_password"
    hashed_password = auth_service.get_password_hash(password)
    assert bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))


def test_verify_password(auth_service: AuthService):
    password = "test_password"
    hashed_password = auth_service.get_password_hash(password)
    assert auth_service.verify_password(password, hashed_password)
    assert not auth_service.verify_password("wrong_password", hashed_password)


def test_verify_password_wrong_password(auth_service: AuthService):
    password = "test_password"
    hashed_password = auth_service.get_password_hash(password)
    assert not auth_service.verify_password("wrong_password", hashed_password)


def test_get_bearer_token_success(auth_service: AuthService):
    token = "valid_token"
    auth_header = f"Bearer {token}"
    assert auth_service.get_bearer_token(auth_header) == token


def test_get_bearer_token_no_header(auth_service: AuthService):
    with pytest.raises(UnAuthenticatedError):
        auth_service.get_bearer_token(None)


def test_get_bearer_token_invalid_prefix(auth_service: AuthService):
    with pytest.raises(UnAuthenticatedError):
        auth_service.get_bearer_token("Basic token")


def test_get_bearer_token_invalid_format(auth_service: AuthService):
    with pytest.raises(UnAuthenticatedError):
        auth_service.get_bearer_token("Bearer")


def assert_token_payload(token, secret, algorithm, sub, token_type, exp_date):
    payload = jwt.decode(token, secret, algorithms=[algorithm])
    assert payload["sub"] == sub
    assert payload["type"] == token_type
    assert abs(payload["exp"] - exp_date.timestamp()) < 1  # Allow for small time differences


@freeze_time("2021-01-01")
def test_generate_access_token_payload(auth_service: AuthService):
    tokens = auth_service.generate_tokens(1)
    exp_date = datetime(2021, 1, 1) + timedelta(minutes=auth_service._access_exp_min)
    assert_token_payload(tokens.access_token, auth_service.secret, auth_service.algorithm, 1, "access", exp_date)


@freeze_time("2021-01-01")
def test_generate_refresh_token_payload(auth_service: AuthService):
    tokens = auth_service.generate_tokens(1)
    exp_date = datetime(2021, 1, 1) + timedelta(days=auth_service._refresh_exp_day)
    assert_token_payload(tokens.refresh_token, auth_service.secret, auth_service.algorithm, 1, "refresh", exp_date)


def test_decode_valid_access_token(auth_service: AuthService):
    tokens = auth_service.generate_tokens(1)
    id = auth_service.decode_token(tokens.access_token)
    assert id == 1


def test_decode_valid_refresh_token(auth_service: AuthService):
    tokens = auth_service.generate_tokens(1)
    id = auth_service.decode_token(tokens.refresh_token)
    assert id == 1


def test_decode_expired_token_raises_error(auth_service: AuthService):
    with freeze_time("2021-01-01"):
        tokens = auth_service.generate_tokens(1)

    # Move time forward to expire the token
    with freeze_time("2021-01-01 01:01"):
        with pytest.raises(UnAuthenticatedError):
            auth_service.decode_token(tokens.access_token)


def test_decode_invalid_token_raises_error(auth_service: AuthService):
    invalid_token = "invalid.token.here"
    with pytest.raises(UnAuthenticatedError):
        auth_service.decode_token(invalid_token)


def test_get_bearer_token_missing(auth_service: AuthService):
    missing_auth_header = None
    with pytest.raises(UnAuthenticatedError):
        auth_service.get_bearer_token(missing_auth_header)
