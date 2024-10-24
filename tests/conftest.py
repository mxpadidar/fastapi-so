import pytest
from fastapi.testclient import TestClient

from account.adapters.mappers import start_mappers
from account.service_layer.repositories import UserRepo
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
def user(user_repo: UserRepo): ...
