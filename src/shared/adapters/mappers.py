from core.database import mapper_registry
from shared.adapters import tables
from shared.domain import entities


def start_shared_mappers():
    mapper_registry.map_imperatively(entities.File, tables.shared_files_table)
