"""first migration

Revision ID: 4726778712a4
Revises: 
Create Date: 2022-01-12 15:01:44.548731

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4726778712a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'authors',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'genres',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'publishing_houses',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'books',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('year', sa.SmallInteger(), nullable=False),
        sa.Column('page_count', sa.Integer(), nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('publishing_house', postgresql.UUID(), nullable=False),
        sa.ForeignKeyConstraint(('publishing_house',), ['publishing_houses.id'], ondelete='cascade'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'authors_books',
        sa.Column('book_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('author_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.ForeignKeyConstraint(('author_id',), ['authors.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(('book_id',), ['books.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('book_id', 'author_id')
    )
    op.create_table(
        'books_genres',
        sa.Column('book_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('genre_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.ForeignKeyConstraint(('book_id',), ['books.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(('genre_id',), ['genres.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('book_id', 'genre_id')
    )


def downgrade():
    op.drop_table('books_genres')
    op.drop_table('authors_books')
    op.drop_table('books')
    op.drop_table('publishing_houses')
    op.drop_table('genres')
    op.drop_table('authors')