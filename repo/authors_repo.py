from uuid import UUID
from fastapi.params import Depends
from sqlalchemy.orm import Session
from models.authors import author_table
from db.base import get_db
from schemas.authors_schema import AuthorBase, AuthorUpdate


class AuthorRepo:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        self.table = author_table

    async def get_all(self, offset: int = 0, limit: int = 100) -> AuthorBase:
        return self.db.query(self.table).offset(offset).limit(limit).all()

    async def create_author(self, author: AuthorBase) -> AuthorBase:
        self.db.execute(self.table.insert(author.dict()))
        self.db.commit()
        return await self.get_all()

    async def find_author(self, uuid: UUID) -> AuthorBase:
        return self.db.query(self.table).filter(self.table.columns.id == uuid).first()

    async def find_author_by_name(self, name: str) -> AuthorBase:
        return self.db.query(self.table).filter(self.table.columns.name.ilike(f'%{name}%')).all()

    async def delete_author(self, uuid: UUID) -> AuthorBase:
        query = self.table.delete().where(self.table.columns.id == uuid)
        self.db.execute(query)
        self.db.commit()
        return await self.get_all()

    async def update_author(self, uuid, author: AuthorUpdate) -> AuthorBase:
        query = self.table.update().where(self.table.columns.id == uuid).values(author.dict())
        self.db.execute(query)
        self.db.commit()
        return await self.find_author(uuid)
