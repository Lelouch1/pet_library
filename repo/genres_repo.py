from typing import List
from uuid import UUID
from fastapi.params import Depends
from sqlalchemy.orm import Session

from models.genres import genre_table
from db.base import get_db
from schemas.genres_schema import GenreBase, GenreUpdate


class GenreRepo:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        self.table = genre_table

    async def get_all(self, offset: int = 0, limit: int = 100) -> GenreBase:
        return self.db.query(self.table).offset(offset).limit(limit).all()

    async def create_genre(self, genre: GenreBase) -> GenreBase:
        self.db.execute(self.table.insert(genre.dict()))
        self.db.commit()
        return await self.get_all()

    async def find_genre(self, uuid: UUID) -> GenreBase:
        return self.db.query(self.table).filter(self.table.columns.id == uuid).first()

    async def find_genre_by_name(self, name: str) -> GenreBase:
        return self.db.query(self.table).filter(self.table.columns.name.ilike(f'%{name}%')).all()

    async def delete_genre(self, uuid: UUID) -> GenreBase:
        query = self.table.delete().where(self.table.columns.id == uuid)
        self.db.execute(query)
        self.db.commit()
        return await self.get_all()

    async def update_genre(self, uuid, genre: GenreUpdate) -> GenreBase:
        query = self.table.update().where(self.table.columns.id == uuid).values(genre.dict())
        self.db.execute(query)
        self.db.commit()
        return await self.find_genre(uuid)
