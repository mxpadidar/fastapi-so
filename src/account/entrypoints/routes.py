from fastapi import APIRouter, Depends

from account.entities.user import User
from account.entrypoints import dependencies, schemas
from account.handlers import login_handler, registration_handler

router = APIRouter(prefix="/accounts", tags=["Accounts"])


@router.post("/registration", response_model=schemas.UserResponse)
def registration(
    params: registration_handler.HandleRegistrationParams,
    user_repo=Depends(dependencies.get_user_repo),
    auth_service=Depends(dependencies.get_auth_service),
):
    user = registration_handler.handle_registration(params, user_repo, auth_service)
    return user.to_dict()


@router.post("/login", response_model=schemas.TokenResponse)
def login(
    params: login_handler.HandleLoginParams,
    user_repo=Depends(dependencies.get_user_repo),
    auth_service=Depends(dependencies.get_auth_service),
):
    token = login_handler.handle_login(params, user_repo, auth_service)
    return token.to_dict()


@router.get("/me", response_model=schemas.UserResponse)
def get_me(user: User = Depends(dependencies.get_current_user)):
    return user.to_dict()
