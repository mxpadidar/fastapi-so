from fastapi import Depends, Request

from account.repositories.user_repo import UserRepo
from account.services.auth_service import AuthService
from core import settings
from core.database import get_db


def get_user_repo(db=Depends(get_db)) -> UserRepo:
    return UserRepo(db)


def get_auth_service():
    return AuthService(**settings.AUTH_CONFIG)


def get_current_user(
    request: Request,
    auth_service: AuthService = Depends(get_auth_service),
    user_repo: UserRepo = Depends(get_user_repo),
):
    token = auth_service.get_bearer_token(request.headers.get("Authorization", ""))
    user_id = auth_service.decode_token(token)
    user = user_repo.get_or_raise_not_found(id=user_id)
    return user
