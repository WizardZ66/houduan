from fastapi.testclient import TestClient

from manage.main import app

client = TestClient(app)

def test_register():
    response = client.post(
        "/auth/register",
        json={"username": "testuser", "password": "testpassword"}
    )
    assert response.status_code == 200
    assert "message" in response.json()

def test_login():
    response = client.post(
        "/auth/login",
        json={"username": "testuser", "password": "testpassword"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "token_type" in response.json()