from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_get_all_courses():
    response = client.get("/api/courses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_course():
    response = client.get("/api/courses/C001")
    assert response.status_code == 200


def test_create_course():
    response = client.post(
        "/api/courses",
        json={
            "course_id": "C999",
            "title": "New Course",
            "description": "Testing"
        }
    )
    assert response.status_code == 200