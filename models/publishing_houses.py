from sqlalchemy import Column, String
from db.base import Base, DefaultColumnsMixin


class PublishingHouseModel(DefaultColumnsMixin, Base):
    __tablename__ = 'publishing_houses'

    name = Column(String, nullable=False)
