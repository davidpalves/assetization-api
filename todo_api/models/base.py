import datetime

from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, mapped_column
from typing_extensions import Annotated

timestamp = Annotated[
    datetime.datetime,
    mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP()),
]

update_timestamp = Annotated[
    datetime.datetime,
    mapped_column(
        nullable=False,
        server_default=func.CURRENT_TIMESTAMP(),
        onupdate=func.CURRENT_TIMESTAMP(),
    ),
]


class Base(DeclarativeBase):
    pass
