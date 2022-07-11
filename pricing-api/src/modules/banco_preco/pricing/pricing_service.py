from typing import List
from src.modules.banco_preco.pricing.pricing_operations import PricingQuery
from src.modules.banco_preco.pricing.pricing_repository import PricingRepository as repository
from src.modules.banco_preco.utils.utils import Pageable

class PricingsService:

    def get(params: PricingQuery, group_by_columns, pageable: Pageable):
        return repository.get(params, group_by_columns, pageable)
