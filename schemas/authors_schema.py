from uuid import UUID
from pydantic import BaseModel


class Author(BaseModel):
    name: str

    class Config:
        orm_mode = True


class AuthorBase(Author):
    id: UUID


class AuthorUpdate(Author):
    ...
