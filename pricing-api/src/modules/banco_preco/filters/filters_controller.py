from fastapi import APIRouter, Depends
from src.modules.banco_preco.filters.filters_operations import ListFiltersQueryParams
from src.modules.banco_preco.filters.filters_service import FilterService as service
from .filter_schema import Filter as FilterSchema
from typing import List

filter_router = APIRouter()

@filter_router.get('/', description='List all created groups based on query params', response_model=List[str])
async def list_filters(params: ListFiltersQueryParams = Depends()) -> List[str]:
  return service.list(params)

@filter_router.get('/autocomplete/', description='Complete bidder name', )
async def get_bidder_names(bidder_name: str):
  return service.autocomplete_bidder_name(bidder_name)
