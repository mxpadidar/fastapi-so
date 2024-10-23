from fastapi.testclient import TestClient

from account.entities.user import User
from account.services.auth_service import AuthService

URL = "/accounts/me"


def test_get_me_success(client: TestClient, auth_service: AuthService, user: User):
    tokens = auth_service.generate_tokens(user.id)
    response = client.get(URL, headers={"Authorization": f"Bearer {tokens.access_token}"})
    assert response.status_code == 200


def test_get_me_without_token(client: TestClient):
    response = client.get(URL)
    assert response.status_code == 401


def test_get_me_with_invalid_token(client: TestClient):
    response = client.get(URL, headers={"Authorization": "Bearer invalid_token"})
    assert response.status_code == 401
