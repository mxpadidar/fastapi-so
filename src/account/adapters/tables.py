import sqlalchemy as sa

from core.database import mapper_registry

account_users_table = sa.Table(
    "users",
    mapper_registry.metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("email", sa.String, unique=True, nullable=False),
    sa.Column("fname", sa.String),
    sa.Column("lname", sa.String),
    sa.Column("gender", sa.String),
    sa.Column("is_active", sa.Boolean, nullable=False, default=True),
    sa.Column("password_hash", sa.String, nullable=False),
    schema="account",
)
