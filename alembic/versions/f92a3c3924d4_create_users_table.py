"""create users table

Revision ID: f92a3c3924d4
Revises:
Create Date: 2024-10-24 02:09:44.931659

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "f92a3c3924d4"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # create account schema
    op.execute("CREATE SCHEMA IF NOT EXISTS account")

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("fname", sa.String(), nullable=True),
        sa.Column("lname", sa.String(), nullable=True),
        sa.Column("gender", sa.String(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("password_hash", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        schema="account",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users", schema="account")
    # ### end Alembic commands ###

    # drop account schema
    op.execute("DROP SCHEMA IF EXISTS account")
