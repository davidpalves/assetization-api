from sqlalchemy import select

from fast_api.models import User


def test_create_user(session):
    new_user = User(
        username='miles', password='spidey', email='miles@morales.com'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'miles'))

    assert user.username == 'miles'
