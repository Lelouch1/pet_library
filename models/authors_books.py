from sqlalchemy import Column, ForeignKey, Table

from db.base import Base

product_tag_table = Table(
    'authors_books',
    Base.metadata,
    Column('book_id', ForeignKey('books.id', ondelete='CASCADE'), primary_key=True),
    Column('author_id', ForeignKey('authors.id', ondelete='CASCADE'), primary_key=True),
)
