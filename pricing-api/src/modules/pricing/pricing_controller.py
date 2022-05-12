from typing import List

from fastapi import APIRouter

from src.modules.pricing.pricing_operations import PricingQuery
from src.modules.pricing.pricing_service import PricingsService as service
from src.modules.utils.utils import (
    check_params_values,
    get_group_by_columns,
    Pageable
)

pricing_router = APIRouter()


@pricing_router.post('/', description='Get the price according query params', )
async def get_pricing(params: PricingQuery, page: int = 0, size: int = 10, sort: str = "id_item", order: str = "desc") -> List[dict]:
    pageable = Pageable(page, size, sort, order)
    check_params_values(params)
    # filters = get_params_values(params)
    group_by_columns = get_group_by_columns(params.group_by_description,
                                            params.group_by_unit_metric,
                                            params.group_by_year)# ,
                                            #params.group_by_cluster)
    return service.get(params, group_by_columns, pageable)
