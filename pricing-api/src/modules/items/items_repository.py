from src.modules.items.items_operations import ListItemsQueryParams

class ItemsRepository:
    
    def find_by_id(id:str):
        return {"id": 1, "description": "máscara pff2", "units_of_measures": ["unidade", "pacote"]}
    
    def list(params: ListItemsQueryParams):
        return [{"id": 1, "description": "máscara pff2", "units_of_measures": ["unidade", "pacote"]}]