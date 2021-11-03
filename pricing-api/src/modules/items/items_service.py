from src.modules.items.items_operations import ListItemsQueryParams
from src.modules.items.items_repository import ItemsRepository as repository
from fastapi import FastAPI, HTTPException


class ItemsService:

    def list(params: ListItemsQueryParams):

        if (bool(params.after) or bool(params.before)) and (bool(params.year) or bool(params.month)):
            raise HTTPException(status_code=422, detail="Não é possível realizar consultas com período e " +
                                "ano/mês de exercício definidos. Favor especificar apenas um período ou ano/mês" +
                                "de exercício desejado.")

        if (bool(params.month) and not bool(params.year)):
            raise HTTPException(status_code=422, detail="Necessário especificar o ano de exercício para " +
                                "realizar a consulta")

        if (bool(params.min_amount) and not bool(params.max_amount)) or (not bool(params.min_amount) and bool(params.max_amount)):
            raise HTTPException(status_code=422, detail="Ao buscar pela quantidade de itens cotados, é" +
                                "necessário especificar um valor mínimo e máximo.")

        if (bool(params.min_price) and not bool(params.max_price)) or (not bool(params.min_price) and bool(params.max_price)):
            raise HTTPException(status_code=422, detail="Ao buscar pelo valor, é" +
                                "necessário especificar um valor mínimo e máximo.")

        if (bool(params.min_homolog_price) and not bool(params.max_homolog_price)) or (not bool(params.min_homolog_price) and bool(params.max_homolog_price)):
            raise HTTPException(status_code=422, detail="Ao buscar pelo valor homologado, é" +
                                "necessário especificar um valor mínimo e máximo.")

        items = repository.list(params)
        return items

    def find_by_id(id: str):
        item = repository.find_by_id(id)
        return item
