from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from todo_api.database import get_session
from todo_api.models.users import User
from todo_api.schemas import Message, UserList, UserPublic, UserSchema
from todo_api.security import get_current_user

Session = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]

router = APIRouter(prefix='/users', tags=['users'])


@router.post('/', response_model=UserPublic, status_code=201)
def create_user(user: UserSchema, session: Session):
    db_user = session.scalar(select(User).where(User.email == user.email))

    if db_user:
        raise HTTPException(
            status_code=400, detail='Username already registered'
        )

    db_user = User(
        username=user.username, password=user.password, email=user.email
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@router.get('/', response_model=UserList)
def list_users(session: Session, skip: int = 0, limit: int = 100):
    users = session.scalars(select(User).offset(skip).limit(limit)).all()
    return {'users': users}


@router.put('/{user_id}', response_model=UserPublic)
def update_user(
    user_id: int, user: UserSchema, session: Session, current_user: CurrentUser
):
    updatedUser = User(**user.model_dump())

    if current_user.id != user_id:
        raise HTTPException(status_code=403, detail='Not enough permissions')

    current_user.username = updatedUser.username
    current_user.email = updatedUser.email
    current_user.password = updatedUser.password

    try:
        session.commit()
        session.refresh(current_user)
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="""
            This email address is not available. Choose a different address.
            """,
        )

    return current_user


@router.delete('/{user_id}', response_model=Message)
def delete_user(
    user_id: int,
    session: Session,
    current_user: CurrentUser,
):
    if current_user.id != user_id:
        raise HTTPException(status_code=403, detail='Not enough permissions')

    session.delete(current_user)
    session.commit()

    return {'detail': 'User deleted'}
