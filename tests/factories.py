import datetime

import factory
import factory.fuzzy

from todo_api.models.assets import Asset, AssetsActions, AssetsTypes
from todo_api.models.todos import Todo, TodoState
from todo_api.models.users import User

start_date = datetime.datetime(2021, 8, 3, tzinfo=datetime.timezone.utc)


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'test{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@test.com')
    password = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')


class TodoFactory(factory.Factory):
    class Meta:
        model = Todo

    title = factory.Faker('text')
    description = factory.Faker('text')
    state = factory.fuzzy.FuzzyChoice(TodoState)
    user_id = 1


class AssetFactory(factory.Factory):
    class Meta:
        model = Asset

    name = factory.Faker('name')
    description = factory.Faker('text')
    type = factory.fuzzy.FuzzyChoice(AssetsTypes)
    salvage_price = factory.fuzzy.FuzzyFloat(50, 1000)
    purchase_price = factory.fuzzy.FuzzyFloat(500, 10000)
    lifespan_in_years = factory.fuzzy.FuzzyInteger(3, 10)
    created_at = factory.fuzzy.FuzzyDateTime(start_dt=start_date)
    updated_at = factory.fuzzy.FuzzyDateTime(start_dt=start_date)
    last_action = factory.fuzzy.FuzzyChoice(AssetsActions)
    last_action_at = factory.fuzzy.FuzzyDateTime(start_dt=start_date)
    user_id = 1
