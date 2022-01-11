from sqlalchemy import Column, String
from db.base import Base, DefaultColumnsMixin


class AuthorModel(DefaultColumnsMixin, Base):
    __tablename__ = 'authors'

    name = Column(String, nullable=False)
