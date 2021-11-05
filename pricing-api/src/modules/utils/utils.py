from src.modules.items.item import ItemModel
from fastapi import FastAPI, HTTPException


def get_params_values(params):

    filters = []

    # filtros demográficos
    if bool(params.city):
        filters.append(ItemModel.municipio.__eq__(params.city))
    if bool(params.region):
        filters.append(ItemModel.regiao.__eq__(params.region))

    # filtros relacionados aos itens
    if bool(params.description):
        filters.append(ItemModel.original.ilike(
            "%" + params.description + "%"))
    if bool(params.group):
        filters.append(ItemModel.grupo.__eq__(params.group))
    if bool(params.body):
        filters.append(ItemModel.orgao.__eq__(params.body))
    if bool(params.modality):
        filters.append(ItemModel.modalidade.__eq__(params.modality))
    if bool(params.payment_method):
        filters.append(ItemModel.forma_pagamento.__eq__(params.payment_method))
    if bool(params.max_amount):
        filters.append(ItemModel.qtde_item_homologado <= params.max_amount)
    if bool(params.min_amount):
        filters.append(ItemModel.qtde_item_homologado >= params.min_amount)
    if bool(params.max_price):
        filters.append(ItemModel.vlr_unitario <= params.max_price)
    if bool(params.min_price):
        filters.append(ItemModel.vlr_unitario >= params.min_price)
    if bool(params.max_homolog_price):
        filters.append(ItemModel.vlr_unitario_cotado <=
                       params.max_homolog_price)
    if bool(params.min_homolog_price):
        filters.append(ItemModel.vlr_unitario_cotado >=
                       params.min_homolog_price)

    # filtros relacionados aos licitantes
    if bool(params.bidder_name):
        filters.append(ItemModel.nome_homologado.__eq__(params.bidder_name))
    if bool(params.bidder_document):
        filters.append(ItemModel.num_cpf_cnpj_homologado.__eq__(
            params.bidder_document))

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

    if (bool(params.min_price) and not bool(params.max_price)) or (not bool(params.min_price) and bool(params.max_price)):
        raise HTTPException(status_code=422, detail="Ao buscar pelo valor, é" +
                            "necessário especificar um valor mínimo e máximo.")

    if (bool(params.min_homolog_price) and not bool(params.max_homolog_price)) or (not bool(params.min_homolog_price) and bool(params.max_homolog_price)):
        raise HTTPException(status_code=422, detail="Ao buscar pelo valor homologado, é" +
                            "necessário especificar um valor mínimo e máximo.")
