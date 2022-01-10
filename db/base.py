from typing import List

from abc import abstractmethod

from sqlalchemy import Column, DateTime, Table, Integer
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import declarative_mixin
from sqlalchemy.sql import func


@as_declarative()
class Base:
    @classmethod
    @abstractmethod  # unfortunately, using metaclass=ABCMeta leads to conflicts, so this only for IDE autocompletion
    def get_primary_key(cls) -> List[str]:
        ...

    @classmethod
    def get_table(cls) -> Table:
        return cls.metadata.tables[cls.__tablename__]


class PrimaryKeyMixin:
    id = Column(Integer, primary_key=True)

    @classmethod
    def get_primary_key(cls) -> List[str]:
        return ['id']


@declarative_mixin
class DefaultColumnsMixin(PrimaryKeyMixin):
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now(), nullable=False)