from todo_api.schemas import UserPublic

# CREATE USER


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


# LIST USER


def test_list_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.status_code == 200
    assert response.json() == {'users': [user_schema]}


# UPDATE USER


def test_update_user(client, user, token):
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
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
        'id': user.id,
    }


def test_update_user_returns_401_when_token_invalid(client, user):
    response = client.put(
        '/users/9999',
        json={
            'username': 'peter',
            'email': 'peter@parker.com',
            'password': 'spiderman',
        },
    )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Not authenticated'}


def test_update_user_with_wrong_auth(client, user, user2, token):
    response = client.put(
        f'/users/{user2.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'miles',
            'email': 'miles@morales.com',
            'password': 'spidey',
        },
    )
    assert response.status_code == 403
    assert response.json() == {'detail': 'Not enough permissions'}


# DELETE USER


def test_delete_user(client, user, token):
    response = client.delete(
        f'/users/{user.id}', headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted'}


def test_delete_user_returns_401_when_token_invalid(client, user):
    response = client.delete('/users/9999')
    assert response.status_code == 401
    assert response.json() == {'detail': 'Not authenticated'}


def test_delete_user_with_wrong_auth(client, user, user2, token):
    response = client.delete(
        f'/users/{user2.id}', headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == 403
    assert response.json() == {'detail': 'Not enough permissions'}
