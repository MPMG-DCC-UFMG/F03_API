from src.modules.painel_bi.v1.filter.filter_repository import FilterRepository as repository

class FilterService:

    def get_filters():
        return repository.get_filters()
