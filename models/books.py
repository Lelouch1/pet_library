from sqlalchemy import Column, String, SmallInteger, Integer, Float, ForeignKey
from db.base import Base, DefaultColumnsMixin
from sqlalchemy.dialects.postgresql import UUID


class BookModel(DefaultColumnsMixin, Base):
    __tablename__ = 'books'

    name = Column(String, nullable=False)
    year = Column(SmallInteger, nullable=False)
    page_count = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    publishing_house = Column(UUID, ForeignKey('publishing_houses.id', ondelete='cascade'), nullable=False)
