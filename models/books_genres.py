from sqlalchemy import Column, ForeignKey, Table

from db.base import Base

product_tag_table = Table(
    'books_genres',
    Base.metadata,
    Column('book_id', ForeignKey('books.id', ondelete='CASCADE'), primary_key=True),
    Column('genre_id', ForeignKey('genres.id', ondelete='CASCADE'), primary_key=True),
)
