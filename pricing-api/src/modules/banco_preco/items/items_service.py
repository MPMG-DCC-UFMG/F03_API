from src.modules.banco_preco.items.items_operations import ListItemsQuery
from src.modules.banco_preco.items.items_repository import ItemsRepository as repository
from src.modules.banco_preco.utils.utils import Pageable


class ItemsService:
    def list(params: ListItemsQuery, pageable: Pageable):
        items = repository.list(params, pageable)
        return items

    def list_sample(params: ListItemsQuery, pageable: Pageable):
        items = repository.list_sample(params, pageable)
        return items

    def list_items_with_values(params: ListItemsQuery):
        items = repository.list_items_with_values(params)
        return items

    def find_by_id(id: str):
        item = repository.find_by_id(id)
        return item

    def autocomplete_description(desc: str):
        item = repository.autocomplete_description(desc)
        return item
