from fastapi import APIRouter, Depends, HTTPException
from pydantic import parse_obj_as
from typing import List
from uuid import UUID

from schemas.authors_schema import AuthorBase, AuthorUpdate, Author
from repo.authors_repo import AuthorRepo

router = APIRouter(prefix="/authors", tags=["authors"])


@router.get('/', response_model=List[AuthorBase])
async def list_authors(offset:int = 0, limit:int = 100, author_repo: AuthorRepo = Depends()):
    query = await author_repo.get_all(offset=offset, limit=limit)
    return parse_obj_as(List[AuthorBase], query)


@router.get("/{author_id}", response_model=AuthorBase)
async def get_author(author_id: UUID,  author_repo: AuthorRepo = Depends()):
    query = await author_repo.find_author(uuid=author_id)
    if not query:
        raise HTTPException(status_code=404, detail=f'author {author_id} not found')
    return AuthorBase.from_orm(query)


@router.get("/get_by_bame/{author_name}", response_model=List[AuthorBase])
async def get_author_by_name(name: str, author_repo: AuthorRepo = Depends()):
    query = await author_repo.find_author_by_name(name=name)
    return parse_obj_as(List[AuthorBase], query)


@router.post('/', response_model=List[AuthorBase])
async def create_author(author: AuthorBase, author_repo: AuthorRepo = Depends()):
    if await author_repo.find_author(author.id):
        raise HTTPException(status_code=404, detail=f'author with {author.id} already exists')
    query = await author_repo.create_author(author)
    return parse_obj_as(List[AuthorBase], query)


@router.delete('/{author_id}', response_model=List[AuthorBase])
async def delete(author_id: UUID,  author_repo: AuthorRepo = Depends()):
    if not await author_repo.find_author(author_id):
        raise HTTPException(status_code=404, detail=f'author {author_id} not found')
    query = await author_repo.delete_author(author_id)
    return parse_obj_as(List[AuthorBase], query)


@router.put('/{author_id}', response_model=AuthorBase)
async def update(author_id: UUID, author: AuthorUpdate, author_repo: AuthorRepo = Depends()):
    if not await author_repo.find_author(author_id):
        raise HTTPException(status_code=404, detail=f'author {author_id} not found')
    return await author_repo.update_author(uuid=author_id, author=author)



