from __future__ import annotations

from typing import TYPE_CHECKING

from passlib.context import CryptContext
from sqlalchemy.orm import Mapped, mapped_column, relationship

from todo_api.models.base import Base, timestamp, updated_timestamp

if TYPE_CHECKING:
    from todo_api.models.todos import Todo


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class User(Base):
    def __init__(self, email: str, username: str, password: str):
        self.email = email
        self.username = username
        self.password = self.get_password_hash(password)

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    created_at: Mapped[timestamp]
    updated_at: Mapped[updated_timestamp]

    todos: Mapped[list[Todo]] = relationship(
        back_populates='user', cascade='all, delete-orphan'
    )

    def get_password_hash(self, password: str):
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)
