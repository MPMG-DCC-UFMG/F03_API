from typing import List

from fastapi import APIRouter

from src.modules.banco_preco.items.items_operations import ListItemsQuery
from src.modules.banco_preco.items.items_service import ItemsService as service
from src.modules.banco_preco.utils.utils import Pageable
from .item_schema import Item as ItemSchema

items_router = APIRouter()

@items_router.post('/', description='List items based on query params', response_model=List[ItemSchema])
async def list_items(params: ListItemsQuery, page: int = 0, size: int = 10, sort: str = "id_item", order: str = "desc", search_type: str = "smart") -> List[dict]:
  if page < 0:
    page = 0
  pageable = Pageable(page, size, sort, order, search_type)
  return service.list(params, pageable)

@items_router.post('/sample/', description='List items based on query params')
async def list_items_sample(params: ListItemsQuery, page: int = 0, size: int = 10, sort: str = "id_item", order: str = "desc", search_type: str = "smart"):
  if page < 0:
    page = 0
  pageable = Pageable(page, size, sort, order, search_type)
  return service.list_sample(params, pageable)

@items_router.post('/sample_overprice/', description='List items which have evidences of overpricing')
async def list_items_sample_overprice(params: ListItemsQuery, page: int = 0, size: int = 10, sort: str = "id_item", order: str = "desc", search_type: str = "smart"):
  if page < 0:
    page = 0
  pageable = Pageable(page, size, sort, order, search_type)
  return service.list_sample_overprice(params, pageable)

@items_router.post('/overprice/', description='List items which have evidences of overpricing')
async def list_items_overprice(params: ListItemsQuery, page: int = 0, size: int = 10, sort: str = "id_item", order: str = "desc", search_type: str = "smart"):
  if page < 0:
    page = 0
  pageable = Pageable(page, size, sort, order, search_type)
  return service.list_overprice(params, pageable)

@items_router.get('/{id}', description='Find item by ID', )
async def get_item(id: str):
  return service.find_by_id(id)

@items_router.get('/autocomplete/', description='Complete description', )
async def get_descriptions(desc: str):
  return service.autocomplete_description(desc)
