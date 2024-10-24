import pytest

from account.domain.entities.user import User
from account.handlers.registration_handler import (
    HandleRegistrationParams,
    handle_registration,
)
from account.repositories.user_repo import UserRepo
from account.service_layer.auth_service import AuthService
from core.errors import ConflictError, ValidationError


@pytest.fixture
def handle_registration_params():
    return HandleRegistrationParams(
        email="newTestUser@mail.com",
        first_name="newTestUserFirstName",
        last_name="newTestUserLastName",
        password="newTestUserPassword",
        password_confirm="newTestUserPassword",
    )


def test_handle_registration_success(
    user_repo: UserRepo, auth_service: AuthService, handle_registration_params: HandleRegistrationParams
):

    user = handle_registration(handle_registration_params, user_repo, auth_service)

    assert user.id
    assert user.email == handle_registration_params.email

    # Check if the user was added to the database
    user_in_db = user_repo.get(email=handle_registration_params.email)
    assert user_in_db
    assert user_in_db.id == user.id

    # Check if the password was hashed
    assert user_in_db.password != handle_registration_params.password

    # Check if the password was hashed correctly
    assert auth_service.verify_password(handle_registration_params.password, user_in_db.password)

    # Clean up
    user_repo.delete(user_in_db)


def test_handle_registration_passwords_do_not_match(
    user_repo: UserRepo, auth_service: AuthService, handle_registration_params: HandleRegistrationParams
):
    handle_registration_params.password_confirm = "passwordsDoNotMatch"

    with pytest.raises(ValidationError, match="Passwords do not match"):
        handle_registration(handle_registration_params, user_repo, auth_service)


def test_handle_registration_user_already_exists(
    user_repo: UserRepo, auth_service: AuthService, handle_registration_params: HandleRegistrationParams, user: User
):
    handle_registration_params.email = user.email

    with pytest.raises(ConflictError, match="User already exists"):
        handle_registration(handle_registration_params, user_repo, auth_service)
