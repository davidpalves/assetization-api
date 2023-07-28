from fastapi.testclient import TestClient

from fast_api.app import app

client = TestClient(app)


def test_root_must_return_200_and_hello_world():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Olar, FastAPI!'}
