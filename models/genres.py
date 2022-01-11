from sqlalchemy import Column, String
from db.base import Base, PrimaryKeyMixin


class GenreModel(Base, PrimaryKeyMixin):
    __tablename__ = 'genres'

    name = Column(String, nullable=False)
