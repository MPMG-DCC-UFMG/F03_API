from src.modules.items.items_operations import ListItemsQueryParams
from src.modules.items.item import ItemModel
from src.db.database import db_session
from sqlalchemy import and_, desc, asc

class ItemsRepository:

    def find_by_id(id:str):
        result = db_session.query(ItemModel).get(id)
        return result.__dict__

    def list(params: ListItemsQueryParams):

        filters = []
        # Ideia: passar a construção dessa lista filters para o construtor da classe ListItemsQueryParams.

        # filtros demográficos
        if bool(params.city):
            filters.append(ItemModel.municipio.__eq__(params.city))
        if bool(params.region):
            filters.append(ItemModel.regiao.__eq__(params.region))

        # filtros relacionados aos itens
        if bool(params.description):
            filters.append(ItemModel.original.ilike("%" + params.description + "%"))
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
            filters.append(ItemModel.vlr_unitario_cotado <= params.max_homolog_price)
        if bool(params.min_homolog_price):
            filters.append(ItemModel.vlr_unitario_cotado >= params.min_homolog_price)

        # filtros relacionados aos licitantes
        if bool(params.bidder_name):
            filters.append(ItemModel.nome_homologado.__eq__(params.bidder_name))
        if bool(params.bidder_document):
            filters.append(ItemModel.num_cpf_cnpj_homologado.__eq__(params.bidder_document))
        

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

        filters.append(ItemModel.item_ruido == 0) # Recupera apenas os itens que não são ruído.
        order = desc(params.sort) if params.order == "desc" else asc(params.sort)
        result = db_session.query(ItemModel).filter(and_(*filters)).order_by(order)[params.offset:params.offset+params.limit]
        return [ row.__dict__ for row in result ]
