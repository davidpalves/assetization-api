import datetime

from pydantic import BaseModel

from todo_api.models.assets import AssetsActions, AssetsTypes


class AssetSchema(BaseModel):
    name: str
    description: str
    type: AssetsTypes
    salvage_price: float
    purchase_price: float
    lifespan_in_years: int


class AssetCreationResponse(BaseModel):
    name: str
    description: str
    type: AssetsTypes
    salvage_price: float
    purchase_price: float
    lifespan_in_years: int


class AssetPublic(BaseModel):
    name: str
    description: str
    type: AssetsTypes
    salvage_price: float
    purchase_price: float
    lifespan_in_years: int
    usage_time: int | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    last_action: AssetsActions | None
    last_action_at: datetime.datetime | None
    depreciation_per_year: float
    depreciable_cost: float


class ListAssets(BaseModel):
    assets: list[AssetPublic]


class AssetUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    type: AssetsTypes | None = None
    salvage_price: float | None = None
    purchase_price: float | None = None
    lifespan_in_years: int | None = None


class AssetRegisterAction(BaseModel):
    action: AssetsActions
