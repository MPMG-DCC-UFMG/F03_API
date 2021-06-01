from src.modules.items.items_operations import ListItemsQueryParams
from src.modules.items.items_repository import ItemsRepository as repository

class ItemsService:

    def list(params: ListItemsQueryParams):
        items = repository.list(params)
        return items

    def find_by_id(id: str):
        item = repository.find_by_id(id)
        return item
