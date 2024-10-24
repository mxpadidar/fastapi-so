import pytest
from fastapi import Request

from account.domain.entities.user import User
from account.entrypoints.dependencies import get_current_user
from account.repositories.user_repo import UserRepo
from account.service_layer.auth_service import AuthService
from core.errors import UnAuthenticatedError


def test_get_current_user_success(user_repo: UserRepo, auth_service: AuthService, user: User):
    tokens = auth_service.generate_tokens(user.id)
    auth_header = f"Bearer {tokens.access_token}"
    request = Request(scope={"type": "http", "headers": [(b"authorization", auth_header.encode())]})
    current_user = get_current_user(request, auth_service=auth_service, user_repo=user_repo)
    assert current_user.id == user.id


def test_get_current_user_with_invalid_token(user_repo: UserRepo, auth_service: AuthService):
    request = Request(scope={"type": "http", "headers": [(b"authorization", b"Bearer invalid_token")]})
    with pytest.raises(UnAuthenticatedError):
        get_current_user(request, auth_service=auth_service, user_repo=user_repo)


def test_get_current_user_with_no_authorization_header(user_repo: UserRepo, auth_service: AuthService):
    request = Request(scope={"type": "http", "headers": []})
    with pytest.raises(UnAuthenticatedError):
        get_current_user(request, auth_service=auth_service, user_repo=user_repo)


def test_get_current_user_with_invalid_authorization_header(user_repo: UserRepo, auth_service: AuthService):
    request = Request(scope={"type": "http", "headers": [(b"authorization", b"invalid_header")]})
    with pytest.raises(UnAuthenticatedError):
        get_current_user(request, auth_service=auth_service, user_repo=user_repo)
