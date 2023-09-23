import datetime
from typing import Optional

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
    id: int
    name: str
    description: str
    type: AssetsTypes
    salvage_price: float
    purchase_price: float
    lifespan_in_years: int
    usage_time: Optional[int]
    created_at: datetime.datetime
    updated_at: Optional[datetime.datetime]
    last_action: Optional[AssetsActions]
    last_action_at: Optional[datetime.datetime]
    depreciation_per_year: float
    depreciable_cost: float


class ListAssets(BaseModel):
    assets: list[AssetPublic]


class AssetUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[AssetsTypes] = None
    salvage_price: Optional[float] = None
    purchase_price: Optional[float] = None
    lifespan_in_years: Optional[int] = None


class AssetRegisterAction(BaseModel):
    action: AssetsActions
