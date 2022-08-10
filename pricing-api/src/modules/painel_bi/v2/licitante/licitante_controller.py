from fastapi import APIRouter, Depends

from src.modules.painel_bi.v1.licitante.licitante_operations import LicitanteQueryParams
from src.modules.painel_bi.v1.licitante.licitante_service import LicitanteService as service


licitante_router = APIRouter()


@licitante_router.get('/{id}', description='Buscar licitante por ID', )
async def get_licitante(id: str):
  return service.find_by_id(id)
  
@licitante_router.get('/', description='Buscar licitante por ID', )
async def search(params: LicitanteQueryParams = Depends()) -> str:
  return service.search(params.q)


