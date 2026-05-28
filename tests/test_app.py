import pytest


def test_root_redirect(client):
    # Arrange: `client` fixture provides a TestClient
    # Act: request root without following redirects
    response = client.get("/", follow_redirects=False)
    # Assert: server redirects to the static index page
    assert response.status_code in (302, 307)
    assert response.headers.get("location") == "/static/index.html"


def test_get_activities(client):
    # Arrange: `client` fixture
    # Act: call the activities endpoint
    response = client.get("/activities")
    # Assert: returns 200 and a JSON list
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
