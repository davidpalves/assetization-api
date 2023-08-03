from tests.factories import AssetFactory
from todo_api.models.assets import AssetsTypes


def test_create_asset(client, token):
    response = client.post(
        '/assets/',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'name': 'Asset',
            'description': 'description',
            'type': 'washing machine',
            'salvage_price': 200,
            'purchase_price': 3400,
            'lifespan_in_years': 10,
        },
    )
    assert response.status_code == 201

    assert response.json() == {
        'name': 'Asset',
        'description': 'description',
        'type': 'washing machine',
        'salvage_price': 200,
        'purchase_price': 3400,
        'lifespan_in_years': 10,
    }


def test_list_assets(session, client, user, token):
    session.bulk_save_objects(AssetFactory.create_batch(5, user_id=user.id))
    session.commit()

    response = client.get(
        '/assets/',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == 200
    assert len(response.json()['assets']) == 5


def test_list_assets_pagination(session, user, client, token):
    session.bulk_save_objects(AssetFactory.create_batch(5, user_id=user.id))
    session.commit()

    response = client.get(
        '/assets/?offset=1&limit=2',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert len(response.json()['assets']) == 2


def test_list_assets_filter_title(session, user, client, token):
    session.bulk_save_objects(
        AssetFactory.create_batch(5, user_id=user.id, name='Test asset 1')
    )
    session.commit()

    response = client.get(
        '/assets/?name=Test asset 1',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert len(response.json()['assets']) == 5


def test_list_assets_filter_description(session, user, client, token):
    session.bulk_save_objects(
        AssetFactory.create_batch(
            5, user_id=user.id, description='description'
        )
    )
    session.commit()

    response = client.get(
        '/assets/?description=desc',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert len(response.json()['assets']) == 5


def test_list_assets_filter_type(session, user, client, token):
    session.bulk_save_objects(
        AssetFactory.create_batch(5, user_id=user.id, type=AssetsTypes.lamp)
    )
    session.commit()
    response = client.get(
        '/assets/?type=lamp',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert len(response.json()['assets']) == 5


def test_patch_asset_error(client, token):
    response = client.patch(
        '/assets/10',
        json={},
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == 404
    assert response.json() == {'detail': 'Asset not found.'}


def test_patch_asset(session, client, user, token):
    asset = AssetFactory(user_id=user.id)

    session.add(asset)
    session.commit()

    response = client.patch(
        f'/assets/{asset.id}',
        json={'name': 'spiderweb'},
        headers={'Authorization': f'Bearer {token}'},
    )
    assert response.status_code == 200
    assert response.json()['name'] == 'spiderweb'


def test_delete_asset(session, client, user, token):
    asset = AssetFactory(id=1, user_id=user.id)

    session.add(asset)
    session.commit()

    response = client.delete(
        f'/assets/{asset.id}', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 200
    assert response.json() == {
        'detail': 'Asset has been deleted successfully.'
    }


def test_delete_todo_error(client, token):
    response = client.delete(
        f'/assets/{10}', headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 404
    assert response.json() == {'detail': 'Asset not found.'}
