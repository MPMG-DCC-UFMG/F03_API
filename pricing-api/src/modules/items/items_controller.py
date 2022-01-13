from fastapi import APIRouter, Depends
from src.modules.items.items_operations import ListItemsQueryParams
from src.modules.items.items_service import ItemsService as service
from .item_schema import Item as ItemSchema
from typing import List

items_router = APIRouter()

@items_router.get('/', description='List items based on query params', response_model=List[ItemSchema])
async def list_items(params: ListItemsQueryParams = Depends()) -> List[dict]:
  return service.list(params)

@items_router.get('/sample/', description='List items based on query params', )
async def list_items_sample(params: ListItemsQueryParams = Depends()) -> List[dict]:
  return service.list_sample(params)

@items_router.get('/{id}', description='Find item by ID', )
async def get_item(id: str):
  return service.find_by_id(id)

@items_router.get('/autocomplete/', description='Complete description', )
async def get_descriptions(desc: str):
  return service.autocomplete_description(desc)
