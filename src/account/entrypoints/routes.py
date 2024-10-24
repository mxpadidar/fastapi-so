from fastapi import APIRouter, Depends

from account.adapters.orm_repos import UserOrmRepo
from account.domain.entities.user import User
from account.entrypoints import dependencies, schemas
from account.service_layer import handlers, utils
from core import settings
from core.database import get_db
from core.helpers import validate_email

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.post("/registration", response_model=schemas.UserResponse)
def registration(request_body: schemas.RegistrationRequest, db=Depends(get_db)):
    user = handlers.handle_registration(
        user_repo=UserOrmRepo(db),
        email_validator=validate_email,
        password_hasher=utils.password_hashing_func_closure(settings.PASSWORD_SALT),
        **request_body.model_dump(),
    )

    return user.to_dict()


@router.post("/login", response_model=schemas.TokenResponse)
def login(request_body: schemas.LoginRequest, db=Depends(get_db)):
    token = handlers.handle_login(
        user_repo=UserOrmRepo(db),
        password_verifier=utils.verify_password,
        token_generator=utils.token_generator_closure(**settings.TOKEN_CONFIG),
        email_validator=validate_email,
        **request_body.model_dump(),
    )
    return token.to_dict()


@router.get("/me", response_model=schemas.UserResponse)
def get_me(user: User = Depends(dependencies.get_current_user)):
    return user.to_dict()
