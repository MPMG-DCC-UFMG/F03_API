from fastapi import APIRouter, Depends
from src.modules.items.items_operations import ListItemsQueryParams
from src.modules.items.items_service import ItemsService as service
items_router = APIRouter()

@items_router.get('/', description='List items based on query params', )
async def list_items(params: ListItemsQueryParams = Depends()):
  return service.list(params)

@items_router.get('/{id}', description='Find item by ID', )
async def get_item(id: str):
  return service.find_by_id(id)