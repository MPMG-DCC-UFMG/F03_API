from sqlalchemy.sql.functions import count
from src.modules.pricing.pricing_operations import PricingQueryParams
from src.modules.items.item import ItemModel
from src.db.database import db_session
from sqlalchemy.sql import func
from sqlalchemy import and_, cast, desc, Float
from .utils import get_params_values

class PricingRepository:

    def get(params: PricingQueryParams):
        # TODO: Obter estatísticas para listas arbitrárias de itens
        filters = get_params_values(params)
        filters.append(ItemModel.item_ruido == 0) # Recupera apenas os itens que não são ruído.
        order = desc(params.sort) if params.order == "desc" else asc(params.sort)
        result = db_session.query(ItemModel.dsc_unidade_medida, ItemModel.ano, func.avg(cast(ItemModel.preco, Float)).label('mean'), func.max(cast(ItemModel.preco, Float)).label('max'), func.min(cast(ItemModel.preco, Float)).label('min'), func.count().label('count')) \
            .filter(and_(*filters)) \
            .group_by(ItemModel.dsc_unidade_medida, ItemModel.ano) \
            .order_by(order)[params.offset:params.offset+params.limit]

        return [ row for row in result ]

    def get_items(params: PricingQueryParams):
        # TODO: Obter estatísticas para listas arbitrárias de itens
        filters = get_params_values(params)
        filters.append(ItemModel.item_ruido == 0) # Recupera apenas os itens que não são ruído.
        order = desc(params.sort) if params.order == "desc" else asc(params.sort)
        result = db_session.query(ItemModel.original_dsc, ItemModel.dsc_unidade_medida, ItemModel.ano, func.avg(cast(ItemModel.preco, Float)).label('mean'), func.max(cast(ItemModel.preco, Float)).label('max'), func.min(cast(ItemModel.preco, Float)).label('min'), func.count().label('count')) \
            .filter(and_(*filters)) \
            .group_by(ItemModel.original_dsc, ItemModel.dsc_unidade_medida, ItemModel.ano) \
            .order_by(order)[params.offset:params.offset+params.limit]

        return [ row for row in result ]

    def get_groups(params: PricingQueryParams):
        # TODO: Obter estatísticas para listas arbitrárias de itens
        filters = get_params_values(params)
        filters.append(ItemModel.item_ruido == 0) # Recupera apenas os itens que não são ruído.
        order = desc(params.sort) if params.order == "desc" else asc(params.sort)
        result = db_session.query(ItemModel.grupo, ItemModel.dsc_unidade_medida, ItemModel.ano, func.avg(cast(ItemModel.preco, Float)).label('mean'), func.max(cast(ItemModel.preco, Float)).label('max'), func.min(cast(ItemModel.preco, Float)).label('min'), func.count().label('count')) \
            .filter(and_(*filters)) \
            .group_by(ItemModel.grupo, ItemModel.dsc_unidade_medida, ItemModel.ano) \
            .order_by(order)[params.offset:params.offset+params.limit]

        return [ row for row in result ]
