from src.modules.items.items_operations import ListItemsQuery
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
        
        n = len(descriptions)
        res = [{'desc': descriptions[idx]} for idx in range(0, n)]      

        return res

    def list(params: ListItemsQuery, filters):
        filters = [] #params.filters

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
                           .offset(params.offset) \
                           .limit(params.limit)
                        #    .order_by(order) \
          
        res = [row.__dict__ for row in result]
        for item in res:
            item['preco'] = round(item['preco'], 2)
        
        return res

    def list_sample(params: ListItemsQuery, filters):
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
                           .offset(params.offset) \
                           .limit(params.limit)
                        #    .order_by(order) \
          
        res = [row.__dict__ for row in result]
        for item in res:
            item['preco'] = round(item['preco'], 2)
        
        return res


    def list_items_with_values(params: ListItemsQuery, filters):
        if params.description:
            filters.append(ItemModel.original.__eq__(params.description))

        if params.unit_measure:
            filters.append(ItemModel.dsc_unidade_medida.__eq__(params.unit_measure))

        result = db_session.query(ItemModel) \
                           .filter(and_(*filters)) \
                           .offset(params.offset) \
                           .limit(params.limit)

        res = [row.__dict__ for row in result]
        for item in res:
            item['preco'] = round(item['preco'], 2)

        return res
