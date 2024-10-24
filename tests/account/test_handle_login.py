import pytest

from account.domain.entities.user import User
from account.handlers.login_handler import HandleLoginParams, handle_login
from account.repositories.user_repo import UserRepo
from account.service_layer.auth_service import AuthService
from core.errors import UnAuthenticatedError


def test_handle_login_success(user_repo: UserRepo, auth_service: AuthService, user: User):
    params = HandleLoginParams(email=user.email, password="password")
    token = handle_login(params, user_repo, auth_service)
    assert token.access_token


def test_handle_login_with_invalid_email(user_repo: UserRepo, auth_service: AuthService):
    params = HandleLoginParams(email="invalid@mail.com", password="password")
    with pytest.raises(UnAuthenticatedError):
        handle_login(params, user_repo, auth_service)


def test_handle_login_with_invalid_password(user_repo: UserRepo, auth_service: AuthService, user: User):
    params = HandleLoginParams(email=user.email, password="invalid password")
    with pytest.raises(UnAuthenticatedError):
        handle_login(params, user_repo, auth_service)
