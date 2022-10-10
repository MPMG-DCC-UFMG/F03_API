from fastapi import APIRouter, Depends
from src.modules.banco_preco.charts.charts_operations import ChartsQueryParams
from src.modules.banco_preco.charts.charts_service import ChartsService as service
from typing import List

charts_router = APIRouter()

@charts_router.get('/', description='Get the aggregated results according query params', )
async def get_aggregate(params: ChartsQueryParams = Depends()) -> List[dict]:
  return service.get_aggregate(params)
