from src.modules.items.items_operations import ListItemsQuery
from src.modules.items.items_repository import ItemsRepository as repository
from fastapi import FastAPI, HTTPException


class ItemsService:

    def list(params: ListItemsQuery, filters):
        items = repository.list(params, filters)
        return items

    def list_sample(params: ListItemsQuery, filters):
        items = repository.list_sample(params, filters)
        return items

    def list_items_with_values(params: ListItemsQuery, filters):
        items = repository.list_items_with_values(params, filters)
        return items

    def find_by_id(id: str):
        item = repository.find_by_id(id)
        return item

    def autocomplete_description(desc: str):
        item = repository.autocomplete_description(desc)
        return item
