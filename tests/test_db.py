from sqlalchemy import select
from sqlalchemy.orm import Session

from todo_api.models import Todo, User


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
