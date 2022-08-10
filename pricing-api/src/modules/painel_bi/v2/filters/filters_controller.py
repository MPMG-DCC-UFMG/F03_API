from typing import List

from fastapi import APIRouter, Depends

from src.modules.painel_bi.v2.filters.filters_service import FiltersService as service


filters_router = APIRouter()


 
@filters_router.get('/', description='Buscar licitante por ID', )
async def get_filters():
  return service.get_filters()


