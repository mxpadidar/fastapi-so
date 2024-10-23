import pytest
from fastapi.testclient import TestClient

from account.repositories.user_repo import UserRepo

URL = "/accounts/registration"
DATA = {
    "email": "test_registration_route@mail.com",
    "first_name": "first_name",
    "last_name": "last_name",
    "password": "password",
    "password_confirm": "password",
}


@pytest.fixture(autouse=True)
def clean_up(user_repo: UserRepo):
    yield
    user = user_repo.get(email=DATA["email"])
    if user:
        user_repo.delete(user)


def test_registration_route_success(client: TestClient, user_repo: UserRepo):

    response = client.post(URL, json=DATA)

    assert response.status_code == 200

    response_data = response.json()
    assert response_data.get("id") is not None
    assert response_data.get("email") == DATA["email"]

    # Check that the user was created
    user = user_repo.get(email=DATA["email"])
    assert user is not None
    assert user.id == response_data["id"]


def test_registration_route_passwords_do_not_match(client: TestClient):
    response = client.post(URL, json={**DATA, "password_confirm": "WRONG_PASSWORD"})
    assert response.status_code == 422


def test_registration_route_user_already_exists(client: TestClient):

    response = client.post(URL, json=DATA)
    assert response.status_code == 200

    response = client.post(URL, json=DATA)
    assert response.status_code == 409


def test_registration_route_missing_data(client: TestClient):
    response = client.post(URL, json={k: v for k, v in DATA.items() if k != "email"})
    assert response.status_code == 422


def test_registration_route_invalid_email(client: TestClient):
    DATA["email"] = "invalid_email"
    response = client.post(URL, json=DATA)
    assert response.status_code == 422
