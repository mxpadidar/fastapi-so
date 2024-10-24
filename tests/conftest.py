import pytest
from fastapi.testclient import TestClient

from account.domain.entities.user import User
from account.orm.mappers import start_mappers
from account.repositories.user_repo import UserRepo
from account.service_layer.auth_service import AuthService
from core import settings
from core.database import session_maker
from main import app

start_mappers()


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(autouse=True)
def setup():
    yield


@pytest.fixture
def db():
    db = session_maker()
    yield db
    db.close()


@pytest.fixture
def auth_service():
    return AuthService(**settings.AUTH_CONFIG)


@pytest.fixture
def user_repo(db):
    return UserRepo(db)


@pytest.fixture
def user(user_repo: UserRepo, auth_service: AuthService):
    user = User(
        email="test_user@mail.com",
        password_hash=auth_service.get_password_hash("password"),
        first_name="firstName",
        last_name="lastName",
    )
    user_repo.add(user)
    user_repo.commit()

    yield user

    user_repo.delete(user)
