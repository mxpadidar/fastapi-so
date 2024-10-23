import sqlalchemy as sa

from core.database import mapper_registry

users = sa.Table(
    "users",
    mapper_registry.metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("email", sa.String, unique=True, nullable=False),
    sa.Column("first_name", sa.String, nullable=False),
    sa.Column("last_name", sa.String, nullable=False),
    sa.Column("password", sa.String, nullable=False),
    sa.Column("is_active", sa.Boolean, nullable=False, default=True),
    schema="account",
)
