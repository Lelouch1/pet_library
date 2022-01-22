from fastapi import APIRouter, Depends, HTTPException
from pydantic import parse_obj_as
from typing import List
from uuid import UUID

from schemas.genres_schema import GenreBase, GenreUpdate
from repo.genres_repo import GenreRepo

router = APIRouter(prefix="/genres", tags=["genres"])


@router.get('/', response_model=List[GenreBase])
async def list_genres(offset:int = 0, limit:int = 100, genre_repo: GenreRepo = Depends()):
    query = await genre_repo.get_all(offset=offset, limit=limit)
    return parse_obj_as(List[GenreBase], query)


@router.get("/{genre_id}", response_model=GenreBase)
async def get_genre(genre_id: UUID,  genre_repo: GenreRepo = Depends()):
    query = await genre_repo.find_genre(uuid=genre_id)
    if not query:
        raise HTTPException(status_code=404, detail=f'genre {genre_id} not found')
    return GenreBase.from_orm(query)


@router.get("/get_by_bame/{genre_name}", response_model=List[GenreBase])
async def get_genre_by_name(name: str, genre_repo: GenreRepo = Depends()):
    query = await genre_repo.find_genre_by_name(name=name)
    return parse_obj_as(List[GenreBase], query)


@router.post('/', response_model=List[GenreBase])
async def create_genre(genre: GenreBase, genre_repo: GenreRepo = Depends()):
    if await genre_repo.find_genre(genre.id):
        raise HTTPException(status_code=404, detail=f'genre with {genre.id} already exists')
    query = await genre_repo.create_genre(genre)
    return parse_obj_as(List[GenreBase], query)


@router.delete('/{genre_id}', response_model=List[GenreBase])
async def delete(genre_id: UUID,  genre_repo: GenreRepo = Depends()):
    if not await genre_repo.find_genre(genre_id):
        raise HTTPException(status_code=404, detail=f'genre {genre_id} not found')
    query = await genre_repo.delete_genre(genre_id)
    return parse_obj_as(List[GenreBase], query)


@router.put('/{genre_id}', response_model=GenreBase)
async def update(genre_id: UUID, genre: GenreUpdate, genre_repo: GenreRepo = Depends()):
    if not await genre_repo.find_genre(genre_id):
        raise HTTPException(status_code=404, detail=f'genre {genre_id} not found')
    return await genre_repo.update_genre(uuid=genre_id, genre=genre)