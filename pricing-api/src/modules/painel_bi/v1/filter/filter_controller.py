from typing import List

from fastapi import APIRouter, Depends

from src.modules.painel_bi.v1.filter.filter_service import FilterService as service


filter_router = APIRouter()


 
@filter_router.get('/', description='Buscar licitante por ID', )
async def get_filters():
  return service.get_filters()


