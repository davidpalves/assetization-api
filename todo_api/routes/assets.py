from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from todo_api.database import get_session
from todo_api.models.assets import Asset
from todo_api.models.users import User
from todo_api.schemas import (
    AssetCreationResponse,
    AssetPublic,
    AssetRegisterAction,
    AssetSchema,
    AssetUpdate,
    ListAssets,
    Message,
)
from todo_api.security import get_current_user

CurrentUser = Annotated[User, Depends(get_current_user)]
Session = Annotated[Session, Depends(get_session)]


router = APIRouter(prefix='/assets', tags=['assets'])


@router.post('/', response_model=AssetCreationResponse, status_code=201)
def create_asset(
    asset: AssetSchema,
    user: CurrentUser,
    session: Session,
):
    db_asset: Asset = Asset(
        name=asset.name,
        description=asset.description,
        type=asset.type,
        salvage_price=asset.salvage_price,
        purchase_price=asset.purchase_price,
        lifespan_in_years=asset.lifespan_in_years,
        user_id=user.id,
    )
    session.add(db_asset)
    session.commit()
    session.refresh(db_asset)

    return db_asset


@router.get('/', response_model=ListAssets)
def list_assets(
    session: Session,
    user: CurrentUser,
    name: str = Query(None),
    description: str = Query(None),
    type: str = Query(None),
    offset: int = Query(None),
    limit: int = Query(None),
):
    query = select(Asset).where(Asset.user_id == user.id)

    if name:
        query = query.filter(Asset.name.contains(name))

    if description:
        query = query.filter(Asset.description.contains(description))

    if type:
        query = query.filter(Asset.type == type)

    assets = session.scalars(query.offset(offset).limit(limit)).all()

    return {'assets': assets}


@router.patch('/{asset_id}', response_model=AssetPublic)
def patch_asset(
    asset_id: int, session: Session, user: CurrentUser, asset: AssetUpdate
):
    db_asset = session.scalar(
        select(Asset).where(Asset.user_id == user.id, Asset.id == asset_id)
    )

    if not db_asset:
        raise HTTPException(status_code=404, detail='Asset not found.')

    for key, value in asset.model_dump(exclude_unset=True).items():
        setattr(db_asset, key, value)

    session.add(db_asset)
    session.commit()
    session.refresh(db_asset)

    return db_asset


@router.delete('/{asset_id}', response_model=Message)
def delete_asset(asset_id: int, session: Session, user: CurrentUser):
    asset = session.scalar(
        select(Asset).where(Asset.user_id == user.id, Asset.id == asset_id)
    )

    if not asset:
        raise HTTPException(status_code=404, detail='Asset not found.')

    session.delete(asset)
    session.commit()

    return {'detail': 'Asset has been deleted successfully.'}


@router.post('/{asset_id}/register_action', response_model=AssetPublic)
def register_asset_action(
    asset_id: int,
    session: Session,
    user: CurrentUser,
    asset: AssetRegisterAction,
):
    db_asset = session.scalar(
        select(Asset).where(Asset.user_id == user.id, Asset.id == asset_id)
    )

    if not db_asset:
        raise HTTPException(status_code=404, detail='Asset not found.')

    db_asset.register_usage(action=asset.action)

    session.add(db_asset)
    session.commit()
    session.refresh(db_asset)

    return db_asset
