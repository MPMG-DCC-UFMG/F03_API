from src.modules.items.items_operations import ListItemsQueryParams
from src.modules.items.item import ItemModel
from src.modules.utils.utils import (
    get_elasticsearch_query,
    get_autocomplete_query
)
from src.db.database import db_session, es
from sqlalchemy import and_, desc, asc
from sqlalchemy.orm import load_only

class ItemsRepository:

    def find_by_id(id: str):
        result = db_session.query(ItemModel).get(id)
        return result.__dict__

    def autocomplete_description(desc: str):

        QUERY = get_autocomplete_query(desc)
        result = es.search(index="f03-item", suggest=QUERY,
                           filter_path=['suggest.suggest-exact'],
                           request_timeout=20)

        if "suggest" not in result:
            return []

        hits = result["suggest"]["suggest-exact"][0]['options']
        descriptions = [d['text'] for d in hits]

        return descriptions

    def list(params: ListItemsQueryParams):
        filters = params.filters

        # Recupera apenas os itens que não são ruído.
        if params.description:
            QUERY = get_elasticsearch_query(params.description)
            result = es.search(index="f03-item", query=QUERY,
                               filter_path=['hits.hits._source.id_item'],
                               request_timeout=20, ignore=[400, 404], size=500)

            if "hits" not in result:
                return []

            hits = result["hits"]["hits"]
            ids = [d["_source"]["id_item"] for d in hits]
            filters.append(ItemModel.id_item.in_(ids))

        order = desc(params.sort) if params.order == "desc" else asc(params.sort)
        result = db_session.query(ItemModel) \
                           .filter(and_(*filters)) \
                           .order_by(order) \
                           .offset(params.offset) \
                           .limit(params.limit)

        return [row.__dict__ for row in result]

    def list_sample(params: ListItemsQueryParams):
        filters = params.filters

        # Recupera apenas os itens que não são ruído.
        if params.description:
            QUERY = get_elasticsearch_query(params.description)
            result = es.search(index="f03-item", query=QUERY,
                               filter_path=['hits.hits._source.id_item'],
                               request_timeout=20, ignore=[400, 404], size=500)

            if "hits" not in result:
                return []

            hits = result["hits"]["hits"]
            ids = [d["_source"]["id_item"] for d in hits]
            filters.append(ItemModel.id_item.in_(ids))

        fields = ['original', 'original_dsc', 'dsc_unidade_medida', 'grupo', 'data',
                  'modalidade', 'tipo_licitacao', 'nome_vencedor', 'orgao',
                  'municipio', 'qtde_item', 'preco']
        order = desc(params.sort) if params.order == "desc" else asc(params.sort)
        result = db_session.query(ItemModel) \
                           .filter(and_(*filters)) \
                           .options(load_only(*fields)) \
                           .order_by(order) \
                           .offset(params.offset) \
                           .limit(params.limit)

        return [row.__dict__ for row in result]
