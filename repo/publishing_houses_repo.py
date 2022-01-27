from uuid import UUID
from fastapi.params import Depends
from sqlalchemy.orm import Session
from models.publishing_houses import publishing_house_table
from db.base import get_db
from schemas.publishing_houses import PublishingHouseBase, PublishingHouseUpdate


class PublishingHouseRepo:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        self.table = publishing_house_table

    async def get_all(self, offset: int = 0, limit: int = 100) -> PublishingHouseBase:
        return self.db.query(self.table).offset(offset).limit(limit).all()

    async def create_publishing_house(self, publishing_house: PublishingHouseBase) -> PublishingHouseBase:
        self.db.execute(self.table.insert(publishing_house.dict()))
        self.db.commit()
        return await self.get_all()

    async def find_publishing_house(self, uuid: UUID) -> PublishingHouseBase:
        return self.db.query(self.table).filter(self.table.columns.id == uuid).first()

    async def find_publishing_house_by_name(self, name: str) -> PublishingHouseBase:
        return self.db.query(self.table).filter(self.table.columns.name.ilike(f'%{name}%')).all()

    async def delete_publishing_house(self, uuid: UUID) -> PublishingHouseBase:
        query = self.table.delete().where(self.table.columns.id == uuid)
        self.db.execute(query)
        self.db.commit()
        return await self.get_all()

    async def update_publishing_house(self, uuid, publishing_house: PublishingHouseUpdate) -> PublishingHouseBase:
        query = self.table.update().where(self.table.columns.id == uuid).values(publishing_house.dict())
        self.db.execute(query)
        self.db.commit()
        return await self.find_publishing_house(uuid)
