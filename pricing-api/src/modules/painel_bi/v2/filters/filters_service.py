from src.modules.painel_bi.v2.filters.filters_repository import FiltersRepository as repository

class FiltersService:

    def get_filters():
        return repository.get_filters()
