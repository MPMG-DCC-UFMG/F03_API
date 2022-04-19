from fastapi import APIRouter, Depends
from src.modules.items.items_operations import ListItemsQuery
from src.modules.items.items_service import ItemsService as service
from .item_schema import Item as ItemSchema
from typing import List
from src.modules.utils.utils import get_params_values, check_params_values, Pageable

items_router = APIRouter()

@items_router.post('/', description='List items based on query params', response_model=List[ItemSchema])
async def list_items(params: ListItemsQuery, page: int = 0, size: int = 10, sort: str = "id", order: str = "desc") -> List[dict]:
  filters = get_params_values(params)
  pageable = Pageable(page, size, sort, order)
  return service.list(params, filters, pageable)

@items_router.post('/sample/', description='List items based on query params', )
async def list_items_sample(params: ListItemsQuery) -> List[dict]:
  filters = get_params_values(params)
  return service.list_sample(params, filters)

@items_router.post('/match/', description='List items based on query params (applying exact match)', response_model=List[ItemSchema])
async def list_items_with_values(params: ListItemsQuery) -> List[dict]:
  filters = get_params_values(params)
  return service.list_items_with_values(params, filters)

@items_router.get('/{id}', description='Find item by ID', )
async def get_item(id: str):
  return service.find_by_id(id)

@items_router.get('/autocomplete/', description='Complete description', )
async def get_descriptions(desc: str):
  return service.autocomplete_description(desc)
