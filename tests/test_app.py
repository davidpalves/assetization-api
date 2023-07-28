from fastapi.testclient import TestClient

from fast_api.app import app

client = TestClient(app)


def test_root_must_return_200_and_hello_world():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Olar, FastAPI!'}


def test_create_user():
    response = client.post(
        '/users/',
        json={
            'username': 'miles',
            'email': 'miles@morales.com',
            'password': 'spidey',
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        'id': 1,
        'username': 'miles',
        'email': 'miles@morales.com',
    }


def test_list_users():
    response = client.get('/users/')
    assert response.status_code == 200
    assert response.json() == {
        'users': [{'username': 'miles', 'email': 'miles@morales.com', 'id': 1}]
    }


def test_update_user():
    response = client.put(
        '/users/1',
        json={
            'username': 'peter',
            'email': 'peter@parker.com',
            'password': 'spiderman',
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        'username': 'peter',
        'email': 'peter@parker.com',
        'id': 1,
    }


def test_delete_user():
    response = client.delete('/users/1')
    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}
