from fastapi import APIRouter, Depends
from src.modules.groups.groups_operations import ListGroupsQueryParams
from src.modules.groups.groups_service import GroupsService as service
groups_router = APIRouter()

@groups_router.get('/', description='List all created groups based on query params', )
async def list_groups(params: ListGroupsQueryParams = Depends()):
  return service.list(params)

@groups_router.get('/{id}', description='Find group by their ID', )
async def get_group(id: str):
  return service.find_by_id(id)