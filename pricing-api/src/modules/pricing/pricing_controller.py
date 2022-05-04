from fastapi import APIRouter, Depends
from src.modules.pricing.pricing_operations import PricingQuery
from src.modules.pricing.pricing_service import PricingsService as service
from .pricing import Pricing
from typing import List
from src.modules.utils.utils import (
    get_params_values,
    check_params_values,
    get_group_by_columns
)

pricing_router = APIRouter()

@pricing_router.post('/', description='Get the price according query params', )
async def get_pricing(params: PricingQuery) -> List[dict]:
  check_params_values(params)
  filters = get_params_values(params)
  group_by_columns = get_group_by_columns(params.group_by_description,
                                          params.group_by_unit_metric,
                                          params.group_by_year)#,
                                          #params.group_by_cluster)
  return service.get(params, filters, group_by_columns)
