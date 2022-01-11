from sqlalchemy import Column, String
from db.base import Base, PrimaryKeyMixin


class AuthorModel(Base, PrimaryKeyMixin):
    __tablename__ = 'authors'

    name = Column(String, nullable=False)
