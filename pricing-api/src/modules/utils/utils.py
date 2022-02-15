from src.modules.items.item import ItemModel
from fastapi import FastAPI, HTTPException


import random
import datetime

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

    # filtros relacionados aos itens
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

    # filtros relacionados à licitação
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

    # filtros de data
    if bool(params.year):
        filters.append(ItemModel.ano.in_(params.year))
    if bool(params.month):
        filters.append(ItemModel.mes.in_(params.month))
    if bool(params.before):
        filters.append(ItemModel.data <= params.before)
    if bool(params.after):
        filters.append(ItemModel.data >= params.after)
    if bool(params.first_token):
        filters.append(ItemModel.primeiro_termo.__eq__(params.first_token))

    # Recupera apenas os itens que não são ruído.

    return filters


def get_elasticsearch_query(description):

    QUERY = {
        "match": {
          "original": {
              "query": description,
              "minimum_should_match": "50%",
              "analyzer": "analyzer_plural_acentos"
            }
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

    if (bool(params.month) and not bool(params.year)):
        raise HTTPException(status_code=422, detail="Necessário especificar o ano de exercício para " +
                            "realizar a consulta")

    if (bool(params.min_amount) and not bool(params.max_amount)) or (not bool(params.min_amount) and bool(params.max_amount)):
        raise HTTPException(status_code=422, detail="Ao buscar pela quantidade de itens cotados, é" +
                            "necessário especificar um valor mínimo e máximo.")

    if (bool(params.min_homolog_price) and not bool(params.max_homolog_price)) or (not bool(params.min_homolog_price) and bool(params.max_homolog_price)):
        raise HTTPException(status_code=422, detail="Ao buscar pelo valor homologado, é" +
                            "necessário especificar um valor mínimo e máximo.")

def generate_random_date():
    
    start_date = datetime.date(2014, 1, 1)
    end_date = datetime.date(2021, 12, 31)
    
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = str(start_date + datetime.timedelta(days=random_number_of_days))    
    return random_date
