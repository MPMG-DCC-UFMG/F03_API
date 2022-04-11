from src.modules.groups.groups_operations import ListGroupsQuery
from src.modules.groups.groups_repository import GroupsRepository as repository

class GroupsService:

    def list(params: ListGroupsQuery):
        groups = repository.list(params)
        return groups

    def find_by_id(id: str):
        group = repository.find_by_id(id)
        return group
