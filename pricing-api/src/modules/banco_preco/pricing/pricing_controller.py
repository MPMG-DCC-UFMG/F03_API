from typing import List

from fastapi import APIRouter

from src.modules.banco_preco.pricing.pricing_operations import PricingQuery
from src.modules.banco_preco.pricing.pricing_service import PricingsService as service
from src.modules.banco_preco.utils.utils import (
    get_group_by_columns,
    Pageable
)

pricing_router = APIRouter()


@pricing_router.post('/', description='Get the price according query params', )
async def get_pricing(params: PricingQuery, page: int = 0, size: int = 10, sort: str = "id_item", order: str = "desc", search_type: str = "smart"):
    if page < 0:
        page = 0
    pageable = Pageable(page, size, sort, order, search_type)
    group_by_columns = get_group_by_columns(params.group_by_description,
                                            params.group_by_unit_metric,
                                            params.group_by_year)
    return service.get(params, group_by_columns, pageable)
