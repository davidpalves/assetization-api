import datetime
from enum import Enum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing_extensions import Annotated

from todo_api.models.base import Base, timestamp, update_timestamp
from todo_api.models.users import User

last_action_timestamp = Annotated[
    datetime.datetime,
    mapped_column(nullable=True),
]


class AssetsTypes(str, Enum):
    washing_machine = 'washing machine'
    lamp = 'lamp'
    dish_washer = 'dish washer'


class AssetsActions(str, Enum):
    turn_on = 'turn on'
    turn_off = 'turn off'
    regular_use = 'regular use'
    economic_use = 'economic use'
    intense_use = 'intense use'


class Asset(Base):
    __tablename__ = 'assets'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str] = mapped_column(nullable=True)
    type: Mapped[AssetsTypes]
    salvage_price: Mapped[float] = mapped_column(nullable=False)
    purchase_price: Mapped[float] = mapped_column(nullable=False)
    last_action: Mapped[AssetsActions] = mapped_column(nullable=True)
    last_action_at: Mapped[last_action_timestamp]
    usage_time: Mapped[int] = mapped_column(nullable=True)
    lifespan_in_years: Mapped[int] = mapped_column(nullable=False)
    created_at: Mapped[timestamp]
    updated_at: Mapped[update_timestamp]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    user: Mapped[User] = relationship(back_populates='assets')

    @property
    def depreciation_per_year(self) -> float:
        cost = None
        if self.depreciable_cost and self.lifespan_in_years:
            cost = self.depreciable_cost / self.lifespan_in_years
        return cost if cost else 0

    @property
    def depreciable_cost(self) -> float:
        cost = None
        if self.purchase_price and self.salvage_price:
            cost = self.purchase_price - self.salvage_price
        return cost if cost else 0

    def register_usage(self, action: AssetsActions):
        last_action_at = (
            self.last_action_at
            if self.last_action_at
            else datetime.datetime.now()
        )
        if (
            action == AssetsActions.turn_off
            and self.last_action != AssetsActions.turn_off
        ):
            result = datetime.datetime.utcnow() - last_action_at
            self.usage_time = result.days

        self.last_action = action
        self.last_action_at = datetime.datetime.utcnow()
