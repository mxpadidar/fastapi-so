import sqlalchemy as sa

from core.database import mapper_registry

shared_files_table = sa.Table(
    "files",
    mapper_registry.metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("bucket", sa.String, nullable=False),
    sa.Column("name", sa.String, nullable=False, unique=True),
    sa.Column("size", sa.Integer, nullable=False),
    sa.Column("mime_type", sa.String, nullable=False),
    sa.Column("is_used", sa.Boolean, nullable=False, default=False),
    sa.Column("metadata", sa.JSON, nullable=True),
    sa.Column("url", sa.String, nullable=False),
    sa.Column("created_at", sa.DateTime(timezone=True), default=sa.func.now()),
    schema="shared",
)
