import pytest
import json
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_root_url(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.data==  b'{"message":"Hello World"}\n'

def test_multiple_requests(client):
    for _ in range(5):
        response = client.get("/")
        assert response.status_code == 200
