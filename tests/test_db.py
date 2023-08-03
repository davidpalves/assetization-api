from sqlalchemy import select
from sqlalchemy.orm import Session

from todo_api.models.assets import Asset
from todo_api.models.todos import Todo
from todo_api.models.users import User


def test_create_user(session):
    new_user = User(
        username='miles', password='spidey', email='miles@morales.com'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'miles'))

    assert user.username == 'miles'


def test_create_todo(session: Session, user: User):
    todo = Todo(
        title='Test Todo',
        description='Test Desc',
        state='draft',
        user_id=user.id,
    )

    session.add(todo)
    session.commit()
    session.refresh(todo)

    user = session.scalar(select(User).where(User.id == user.id))

    assert todo in user.todos


def test_create_asset(session: Session, user: User):
    asset = Asset(
        name='Test Todo',
        description='Test Desc',
        type='lamp',
        salvage_price=500,
        purchase_price=20000,
        lifespan_in_years=15,
        user_id=user.id,
    )

    session.add(asset)
    session.commit()
    session.refresh(asset)

    user = session.scalar(select(User).where(User.id == user.id))

    assert asset in user.assets
