import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"API Flask DevSecOps" in response.data


def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data


def test_get_data_endpoint(client):
    response = client.get('/api/data')
    assert response.status_code == 200
    assert b"data" in response.data


def test_post_data_endpoint(client):
    response = client.post('/api/data', json={"test": "data"})
    assert response.status_code == 201
    assert b"received" in response.data
