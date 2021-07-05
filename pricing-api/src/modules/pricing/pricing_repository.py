from sqlalchemy.sql.functions import count
from src.modules.pricing.pricing_operations import PricingQueryParams
from src.modules.items.item import ItemModel
from src.db.database import db_session
from sqlalchemy.sql import func
from sqlalchemy import and_, cast, desc, Float

class PricingRepository:

    def get(params: PricingQueryParams):
        # TODO: Obter estatísticas para listas arbitrárias de itens
        filters = []
        if (not params.group) and (not params.description): # Talvez seja melhor explicitar esse requerimento em outro lugar (como na classe Params), ou com outra resposta.
            return []
        if params.year:
            filters.append(ItemModel.ano.in_(params.year))
        if params.description:
            filters.append(ItemModel.original.ilike("%" + params.description + "%")) # TODO: Melhorar a busca por descrição.
        if params.group:
            filters.append(ItemModel.grupo.__eq__(params.group))
        if params.units_of_measure:
            filters.append(ItemModel.dsc_unidade_medida.in_(params.units_of_measure))
        filters.append(ItemModel.item_ruido == 0) # Recupera apenas os itens que não são ruído.

        result = db_session.query(ItemModel.dsc_unidade_medida, ItemModel.ano, func.avg(cast(ItemModel.preco, Float)).label('mean'), func.max(cast(ItemModel.preco, Float)).label('max'), func.min(cast(ItemModel.preco, Float)).label('min'), func.count().label('count')) \
            .filter(and_(*filters)) \
            .group_by(ItemModel.dsc_unidade_medida, ItemModel.ano) \
            .order_by(desc('count'))

        return [ row for row in result ]
