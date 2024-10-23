from account.entities.user import User
from account.orm.tables import users
from core.database import mapper_registry


def start_mappers():

    mapper_registry.map_imperatively(User, users)
