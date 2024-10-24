from fastapi import Depends, Request

from account.adapters.orm_repos import UserOrmRepo
from account.domain.entities import User
from account.service_layer import errors, utils
from core import settings
from core.database import get_db


def get_current_user(request: Request, db=Depends(get_db)) -> User:
    user_repo = UserOrmRepo(db)
    token = utils.authorization_header_parser(request.headers.get("Authorization"))
    token_parser = utils.token_parser_closure(**settings.TOKEN_CONFIG)
    user_id = token_parser(token)
    user = user_repo.get(id=user_id)
    if not user:
        raise errors.UnAuthenticatedError("User not found")

    return user
