import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """Provide a sync `TestClient` for the FastAPI app.

    Using `TestClient` keeps tests synchronous and avoids compatibility issues
    with the installed `httpx` version.
    """
    with TestClient(app) as c:
        yield c
