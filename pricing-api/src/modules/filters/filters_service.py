from src.modules.filters.filters_operations import ListFiltersQueryParams
from src.modules.filters.filters_repository import FilterRepository as repository

class FilterService:
    def list(params: ListFiltersQueryParams):
        filtered_values = repository.list(params)
        return filtered_values
