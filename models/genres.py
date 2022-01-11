from sqlalchemy import Column, String
from db.base import Base, DefaultColumnsMixin


class GenreModel(DefaultColumnsMixin, Base):
    __tablename__ = 'genres'

    name = Column(String, nullable=False)
