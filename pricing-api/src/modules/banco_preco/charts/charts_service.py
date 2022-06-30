from typing import List
from src.modules.banco_preco.charts.charts_operations import ChartsQueryParams
from src.modules.banco_preco.charts.charts_repository import ChartsRepository as repository

class ChartsService:

    def get_aggregate(params: ChartsQueryParams):
        values = repository.get_aggregate(params)
        return values
