from typing import List

from abc import abstractmethod
from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import Column, Table
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import declarative_mixin
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'postgresql://admin:admin@localhost:5434/pet-library'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@as_declarative()
class Base:
    @classmethod
    @abstractmethod  # unfortunately, using metaclass=ABCMeta leads to conflicts, so this only for IDE autocompletion
    def get_primary_key(cls) -> List[str]:
        ...

    @classmethod
    def get_table(cls) -> Table:
        return cls.metadata.tables[cls.__tablename__]


@declarative_mixin
class DefaultColumnsMixin:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    @classmethod
    def get_primary_key(cls) -> List[str]:
        return ['id']


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()