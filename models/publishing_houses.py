from sqlalchemy import Column, String
from db.base import Base, PrimaryKeyMixin


class PublishingHouseModel(Base, PrimaryKeyMixin):
    __tablename__ = 'publishing_houses'

    name = Column(String, nullable=False)
