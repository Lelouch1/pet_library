from uuid import UUID
from pydantic import BaseModel


class PublishingHouse(BaseModel):
    name: str

    class Config:
        orm_mode = True


class PublishingHouseBase(PublishingHouse):
    id: UUID


class PublishingHouseUpdate(PublishingHouse):
    ...
