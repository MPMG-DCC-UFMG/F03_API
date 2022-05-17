from typing import List

from fastapi import APIRouter

from src.modules.items.items_operations import ListItemsQuery
from src.modules.items.items_service import ItemsService as service
from src.modules.utils.utils import Pageable
from .item_schema import Item as ItemSchema

items_router = APIRouter()

@items_router.post('/', description='List items based on query params', response_model=List[ItemSchema])
async def list_items(params: ListItemsQuery, page: int = 0, size: int = 10, sort: str = "id_item", order: str = "desc") -> List[dict]:
  pageable = Pageable(page, size, sort, order)
  return service.list(params, pageable)

@items_router.post('/sample/', description='List items based on query params', )
async def list_items_sample(params: ListItemsQuery, page: int = 0, size: int = 10, sort: str = "id_item", order: str = "desc") -> List[dict]:
  pageable = Pageable(page, size, sort, order)
  return service.list_sample(params, pageable)

@items_router.get('/{id}', description='Find item by ID', )
async def get_item(id: str):
  return service.find_by_id(id)

@items_router.get('/autocomplete/', description='Complete description', )
async def get_descriptions(desc: str):
  return service.autocomplete_description(desc)
