from uuid import uuid4

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy import Column, String, Table
from db.base import Base

publishing_house_table = Table(
    'publishing_houses',
    Base.metadata,
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid4),
    Column('name', String, nullable=False)
)

