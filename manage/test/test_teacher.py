from fastapi.testclient import TestClient

from manage.main import app

client = TestClient(app)

def test_create_teacher():
    response = client.post(
        "/teachers/teachers",
        json={
            "name": "Test Teacher",
            "gender": "Male",
            "ethnicity": "Han",
            "position": "Professor",
            "political_affiliation": "Member of the Communist Party of China",
            "email": "test.teacher@example.com",
            "phone_number": "1234567890",
            "wechat_id": "test_wechat",
            "qq_number": "123456789",
            "awards": "Best Teacher Award"
        }
    )
    assert response.status_code == 200
    assert "id" in response.json()

def test_read_teachers():
    response = client.get("/teachers/teachers")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_teacher():
    response = client.get("/teachers/teachers/1")
    assert response.status_code == 200
    assert "name" in response.json()