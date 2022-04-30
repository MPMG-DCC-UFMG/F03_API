from typing import List
from src.modules.pricing.pricing_operations import PricingQuery
from src.modules.pricing.pricing_repository import PricingRepository as repository
from src.modules.utils.utils import Pageable

class PricingsService:

    def get(params: PricingQuery, group_by_columns, pageable: Pageable):
        return repository.get(params, group_by_columns, pageable)
