from fastapi import APIRouter, Depends, HTTPException
from pydantic import parse_obj_as
from typing import List
from uuid import UUID

from schemas.publishing_houses import PublishingHouseBase, PublishingHouseUpdate
from repo.publishing_houses_repo import PublishingHouseRepo

router = APIRouter(prefix='/publishing_houses', tags=['publishing_houses'])


@router.get('/', response_model=List[PublishingHouseBase])
async def list_publishing_houses(
        offset: int = 0,
        limit: int = 100,
        publishing_house_repo:
        PublishingHouseRepo = Depends(),
):
    query = await publishing_house_repo.get_all(offset=offset, limit=limit)
    return parse_obj_as(List[PublishingHouseBase], query)


@router.get("/{publishing_house_id}", response_model=PublishingHouseBase)
async def get_publishing_house(
        publishing_house_id: UUID,
        publishing_house_repo: PublishingHouseRepo = Depends(),
):
    query = await publishing_house_repo.find_publishing_house(uuid=publishing_house_id)
    if not query:
        raise HTTPException(status_code=404, detail=f'publishing_house {publishing_house_id} not found')
    return PublishingHouseBase.from_orm(query)


@router.get("/get_by_bame/{publishing_house_name}", response_model=List[PublishingHouseBase])
async def get_publishing_house_by_name(name: str, publishing_house_repo: PublishingHouseRepo = Depends()):
    query = await publishing_house_repo.find_publishing_house_by_name(name=name)
    return parse_obj_as(List[PublishingHouseBase], query)


@router.post('/', response_model=List[PublishingHouseBase])
async def create_publishing_house(
        publishing_house: PublishingHouseBase,
        publishing_house_repo: PublishingHouseRepo = Depends(),
):
    if await publishing_house_repo.find_publishing_house(publishing_house.id):
        raise HTTPException(status_code=404, detail=f'publishing_house with {publishing_house.id} already exists')
    query = await publishing_house_repo.create_publishing_house(publishing_house)
    return parse_obj_as(List[PublishingHouseBase], query)


@router.delete('/{publishing_house_id}', response_model=List[PublishingHouseBase])
async def delete(publishing_house_id: UUID,  publishing_house_repo: PublishingHouseRepo = Depends()):
    if not await publishing_house_repo.find_publishing_house(publishing_house_id):
        raise HTTPException(status_code=404, detail=f'publishing_house {publishing_house_id} not found')
    query = await publishing_house_repo.delete_publishing_house(publishing_house_id)
    return parse_obj_as(List[PublishingHouseBase], query)


@router.put('/{publishing_house_id}', response_model=PublishingHouseBase)
async def update(
        publishing_house_id: UUID, 
        publishing_house: PublishingHouseUpdate,
        publishing_house_repo: PublishingHouseRepo = Depends(),
):
    if not await publishing_house_repo.find_publishing_house(publishing_house_id):
        raise HTTPException(status_code=404, detail=f'publishing_house {publishing_house_id} not found')
    return await publishing_house_repo.update_publishing_house(
        uuid=publishing_house_id,
        publishing_house=publishing_house,
    )