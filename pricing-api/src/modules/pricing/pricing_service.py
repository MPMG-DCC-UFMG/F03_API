from typing import List
from src.modules.pricing.pricing_operations import PricingQuery
from src.modules.pricing.pricing_repository import PricingRepository as repository

class PricingsService:

    def get(params: PricingQuery, filters, group_by_columns):
        return repository.get(params, filters, group_by_columns)
