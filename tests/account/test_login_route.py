from fastapi.testclient import TestClient

from account.entities.user import User


def test_login_route_success(client: TestClient, user: User):
    response = client.post(
        "/accounts/login",
        json={"email": user.email, "password": "password"},
    )
    assert response.status_code == 200

    response_data = response.json()
    assert response_data.get("access_token") is not None


def test_login_route_invalid_email(client: TestClient):
    response = client.post(
        "/accounts/login",
        json={"email": "invalid_email", "password": "password"},
    )
    assert response.status_code == 422


def test_login_route_missing_email(client: TestClient):
    response = client.post(
        "/accounts/login",
        json={"password": "password"},
    )
    assert response.status_code == 422
