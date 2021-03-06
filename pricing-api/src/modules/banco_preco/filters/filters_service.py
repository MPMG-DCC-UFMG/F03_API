from src.modules.banco_preco.filters.filters_operations import ListFiltersQueryParams
from src.modules.banco_preco.filters.filters_repository import FilterRepository as repository

class FilterService:
    def list(params: ListFiltersQueryParams):
        filtered_values = repository.list(params)
        return filtered_values

    def autocomplete_bidder_name(bidder_name: str):
        item = repository.autocomplete_bidder_name(bidder_name)
        return item
