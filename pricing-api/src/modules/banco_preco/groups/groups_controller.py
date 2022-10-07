from fastapi import APIRouter
from src.modules.banco_preco.groups.groups_operations import ListGroupsQuery
from src.modules.banco_preco.groups.groups_service import GroupsService as service
from .group_schema import Group as GroupSchema
from typing import List

groups_router = APIRouter()

@groups_router.post('/', description='List all created groups based on query params')
async def list_groups(params: ListGroupsQuery) -> List[dict]:
  return service.list(params)

@groups_router.get('/{id}', description='Find group by ID', )
async def get_group(id: str):
  return service.find_by_id(id)
