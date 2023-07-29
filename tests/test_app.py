from fast_api.schemas import UserPublic


def test_create_user(client):
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


def test_create_user_returns_400_when_user_already_exists(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'miles',
            'email': 'miles@morales.com',
            'password': 'spidey',
        },
    )

    assert response.status_code == 400
    assert response.json() == {'detail': 'Username already registered'}


def test_list_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.status_code == 200
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
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


def test_update_user_returns_404_when_user_does_not_exist(client, user):
    response = client.put(
        '/users/9999',
        json={
            'username': 'peter',
            'email': 'peter@parker.com',
            'password': 'spiderman',
        },
    )
    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client, user):
    response = client.delete('/users/1')
    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}


def test_delete_user_returns_404_when_user_does_not_exist(client, user):
    response = client.delete('/users/9999')
    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}
