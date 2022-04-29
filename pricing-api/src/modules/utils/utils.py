import datetime

from pydantic import BaseModel
from sqlalchemy import Date

from src.modules.items.item import ItemModel
from fastapi import FastAPI, HTTPException


def get_params_values(params):
    filters = []

    # filtros demográficos
    if bool(params.city):
        filters.append(ItemModel.municipio.in_(params.city))
    if bool(params.microregion):
        filters.append(ItemModel.microrregiao.in_(params.microregion))
    if bool(params.mesoregion):
        filters.append(ItemModel.mesorregiao.in_(params.mesoregion))
    if bool(params.plan_region):
        filters.append(ItemModel.regiao_planejamento.in_(params.plan_region))
    if bool(params.imediate_region):
        filters.append(ItemModel.regiao_imediata.in_(params.imediate_region))
    if bool(params.inter_region):
        filters.append(ItemModel.regiao_intermediaria.in_(params.inter_region))

    # # filtros relacionados aos itens
    if bool(params.group):
        filters.append(ItemModel.grupo.__eq__(params.group))
    if bool(params.object_nature):
        filters.append(ItemModel.natureza_objeto.__eq__(params.object_nature))
    if bool(params.max_amount):
        filters.append(ItemModel.qtde_item <= params.max_amount)
    if bool(params.min_amount):
        filters.append(ItemModel.qtde_item >= params.min_amount)
    if bool(params.max_homolog_price):
        filters.append(ItemModel.preco <= params.max_homolog_price)
    if bool(params.min_homolog_price):
        filters.append(ItemModel.preco >= params.min_homolog_price)

    # # filtros relacionados à licitação
    if bool(params.modality):
        filters.append(ItemModel.modalidade.__eq__(params.modality))
    if bool(params.procurement_type):
        filters.append(ItemModel.tipo_licitacao.__eq__(
            params.procurement_type))
    if bool(params.body):
        filters.append(ItemModel.orgao.__eq__(params.body))
    if bool(params.body_type):
        filters.append(ItemModel.tipo_orgao.__eq__(params.body_type))
    if bool(params.bidder_type):
        filters.append(ItemModel.tipo_vencedor.__eq__(params.bidder_type))

    # filtros relacionados aos licitantes
    if bool(params.bidder_name):
        filters.append(ItemModel.nome_vencedor.__eq__(params.bidder_name))
    if bool(params.bidder_document):
        filters.append(ItemModel.cnpj_vencedor.__eq__(params.bidder_document))

    # # filtros de data
    if bool(params.year):
        filters.append(ItemModel.ano.in_(params.year))
    if bool(params.month):
        filters.append(ItemModel.mes.in_(params.month))
    if bool(params.before):
        filters.append(ItemModel.data <= str(params.before))
    if bool(params.after):
        filters.append(ItemModel.data >= str(params.after))
    if bool(params.first_token):
        filters.append(ItemModel.primeiro_termo.__eq__(params.first_token))

    # Recupera apenas os itens que não são ruído.

    return filters


def get_range(params, min_field, max_field):
    l = {}
    if params[min_field]:
        l["gte"] = params[min_field]
    if params[max_field]:
        l["lte"] = params[max_field]
    return l


terms_translation = {
    "city": "municipio",
    "microregion": "microrregiao",
    "mesoregion": "mesoregion",
    "plan_region": "regiao_planejamento",
    "imediate_region": "regiao_imediata",
    "inter_region": "regiao_intermediaria",
    "year": "ano",
    "month": "mes",
}

term_translation = {
    "description": "original",
    "unit_measure": "dsc_unidade_medida",
    "group": "grupo",
    "first_token": "primeiro_termo",
    "body": "orgao",
    "body_type": "tipo_orgao",
    "modality": "original",
    "procurement_type": "tipo_licitacao",
    "bidder_name": "nome_vencedor",
    "bidder_type": "tipo_vencedor",
    "bidder_document": "tipo_licitacao",
    "object_nature": "natureza_objeto"
}


def get_item_query(params: dict):
    print(params)
    filters = []
    for param in params:
        value = params[param]
        if not value:
            continue
        if param in terms_translation:
            portuguese_name = terms_translation[param]
            filters.append({"terms": {portuguese_name: value}})
        elif param in term_translation:
            portuguese_name = term_translation[param]
            filters.append({"term": {portuguese_name: value}})

    if params["before"]:
        pass
    if params["after"]:
        pass

    if params["min_amount"] or params["max_amount"]:
        l = get_range(params, min_field="min_amount", max_field="max_amount")
        filters.append({"range": {"qtde_item": l}})
    if params["min_homolog_price"] or params["max_homolog_price"]:
        l = get_range(params, min_field="min_homolog_price", max_field="max_homolog_price")
        filters.append({"range": {"preco": l}})

    QUERY = {
        "bool": {
            "must": [*filters],
        }
    }

    return QUERY


def get_autocomplete_query(description):
    QUERY = {
        "suggest-exact": {
            "prefix": description,
            "completion": {
                "field": "original_prep",
                "skip_duplicates": True,
                "size": 5
            }
        }
    }

    return QUERY


def get_id_query(id: str):
    QUERY = {
        "bool": {
            "must": [
                {"term": {"id_item": id}}
            ]
        }
    }

    return QUERY


def get_group_query(params):
    query = {
        "query": {
            "match_none": {}
        }
    }

    return query


def get_group_by_columns(group_by_description, group_by_unit_metric, group_by_year,
                         group_by_cluster):
    columns = []

    if group_by_description:
        columns.append(ItemModel.original)
    if group_by_unit_metric:
        columns.append(ItemModel.dsc_unidade_medida)
    if group_by_year:
        columns.append(ItemModel.ano)
    if group_by_cluster:
        columns.append(ItemModel.grupo)

    if len(columns) == 0:
        columns.append(ItemModel.original)

    columns = tuple(columns)
    return columns


def check_params_values(params):
    if (bool(params.after) or bool(params.before)) and (bool(params.year) or bool(params.month)):
        raise HTTPException(status_code=422, detail="Não é possível realizar consultas com período e " +
                                                    "ano/mês de exercício definidos. Favor especificar apenas um período ou ano/mês" +
                                                    "de exercício desejado.")

    # if (bool(params.month) and not bool(params.year)):
    #     raise HTTPException(status_code=422, detail="Necessário especificar o ano de exercício para " +
    #                         "realizar a consulta")

    if (bool(params.min_amount) and not bool(params.max_amount)) or (
            not bool(params.min_amount) and bool(params.max_amount)):
        raise HTTPException(status_code=422, detail="Ao buscar pela quantidade de itens cotados, é" +
                                                    "necessário especificar um valor mínimo e máximo.")

    if (bool(params.min_homolog_price) and not bool(params.max_homolog_price)) or (
            not bool(params.min_homolog_price) and bool(params.max_homolog_price)):
        raise HTTPException(status_code=422, detail="Ao buscar pelo valor homologado, é" +
                                                    "necessário especificar um valor mínimo e máximo.")


class Pageable:
    def __init__(self, page: int, size: int, sort: str, order: str):
        self._page = page
        self._size = size
        self._sort = sort
        self._order = order

    def get_page(self):
        return self._page

    def get_size(self):
        return self._size

    def get_sort(self):
        return self._sort

    def get_order(self):
        return self._order

    def __str__(self):
        return str({
            "page": self._page,
            "size": self._size,
            "sort": self._sort,
            "order": self._order
        })
