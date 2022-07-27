from typing import List
from src.modules.painel_bi.v1.licitante.licitante_repository import LicitanteRepository as repository
from src.modules.painel_bi.v1.utils.utils import Pageable

class LicitanteService:

    def search(query: str):
        return repository.search(query)

    def find_by_id(id_licitante: str):
        item = repository.find_by_id(id_licitante)
        return item