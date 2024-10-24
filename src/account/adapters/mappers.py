from account.adapters.tables import account_users_table
from account.domain.entities.user import User
from core.database import mapper_registry


def start_mappers():

    mapper_registry.map_imperatively(User, account_users_table)
