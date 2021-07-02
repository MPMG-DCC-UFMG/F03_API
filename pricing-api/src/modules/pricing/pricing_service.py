from typing import List
from src.modules.pricing.pricing_operations import PricingQueryParams
from src.modules.pricing.pricing_repository import PricingRepository as repository

class PricingsService:

    def get(params: PricingQueryParams):
        return repository.get(params)
