from typing import List
from src.modules.pricing.pricing_operations import PricingQueryParams
from src.modules.pricing.pricing_repository import PricingRepository as repository
from .utils import check_params_values

class PricingsService:

    def get(params: PricingQueryParams):
        check_params_values(params)
        return repository.get(params)

    def get_items(params: PricingQueryParams):
        check_params_values(params)
        return repository.get_items(params)

    def get_groups(params: PricingQueryParams):
        check_params_values(params)
        return repository.get_groups(params)
