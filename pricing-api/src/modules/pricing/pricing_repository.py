from sqlalchemy.sql.functions import count
from src.modules.pricing.pricing_operations import PricingQueryParams
from src.modules.items.item import ItemModel
from src.modules.utils.utils import get_elasticsearch_query
from src.db.database import db_session, es
from sqlalchemy.sql import func
from sqlalchemy import and_, cast, desc, Float


class PricingRepository:

    def get(params: PricingQueryParams):
        # TODO: Obter estatísticas para listas arbitrárias de itens
        filters = params.filters
        filters.append(ItemModel.item_ruido == 0) # Recupera apenas os itens que não são ruído.

        if params.description:
            QUERY = get_elasticsearch_query(params.description)
            result = es.search(index="f03-itens", query=QUERY, from_=params.offset,
                               size=params.limit, filter_path=['hits.hits._source.id_item'],
                               request_timeout=10, ignore=[400, 404])

            if "hits" not in result:
                return []

            hits = result["hits"]["hits"]
            ids = [d["_source"]["id_item"] for d in hits]
            filters.append(ItemModel.id_item.in_(ids))

        columns = params.group_by_columns
        order = desc(params.sort) if params.order == "desc" else asc(params.sort)
        result = db_session.query(*columns, func.avg(cast(ItemModel.preco, Float)).label('mean'), func.max(cast(ItemModel.preco, Float)).label('max'), func.min(cast(ItemModel.preco, Float)).label('min'), func.count().label('count')) \
            .filter(and_(*filters)) \
            .group_by(*columns) \
            .order_by(order)

        return [ row for row in result ]
