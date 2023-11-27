"""add book model for test scraper

Revision ID: 884548465ac4
Revises: b8908d6b76f0
Create Date: 2023-11-27 20:22:52.631435

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import fastapi_users_db_sqlalchemy


# revision identifiers, used by Alembic.
revision: str = "884548465ac4"
down_revision: Union[str, None] = "b8908d6b76f0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "books",
        sa.Column("title", sa.String(length=200), nullable=False),
        sa.Column("author", sa.String(length=100), nullable=False),
        sa.Column("publish_year", sa.Integer(), nullable=True),
        sa.Column("number_of_pages", sa.Integer(), nullable=True),
        sa.Column("annotation", sa.String(length=1000), nullable=True),
        sa.Column("cover", sa.String(), nullable=True),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("books")
    # ### end Alembic commands ###
