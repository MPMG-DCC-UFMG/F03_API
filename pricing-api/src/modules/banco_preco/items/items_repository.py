import os

from warnings import warn

from dotenv import load_dotenv

from src.db.database import es
from src.modules.banco_preco.items.items_operations import ListItemsQuery
from src.modules.banco_preco.utils.utils import (
    get_item_query_smart,
    get_item_query_anywhere,
    get_item_query_exact,
    get_autocomplete_query,
    get_id_query,
    Pageable
)

load_dotenv()
ES_INDEX_ITEM = os.environ.get('ES_INDEX_ITEM')

class ItemsRepository:

    def find_by_id(id: str):
        QUERY = get_id_query(id)
        result = es.search(index=ES_INDEX_ITEM,
                           query=QUERY,
                           request_timeout=20)

        if "hits" not in result:
            return []

        hits = result["hits"]["hits"]
        return [item['_source'] for item in hits]

    def autocomplete_description(desc: str):
        QUERY = get_autocomplete_query(desc)
        result = es.search(index=ES_INDEX_ITEM,
                           suggest=QUERY,
                           filter_path=['suggest.suggest-exact'],
                           request_timeout=20)

        if "suggest" not in result:
            return []

        hits = result["suggest"]["suggest-exact"][0]['options']
        descriptions = [d['text'] for d in hits]
        
        n = len(descriptions)
        res = [{'desc': descriptions[idx]} for idx in range(0, n)]
        return res

    def list(params: ListItemsQuery, pageable: Pageable):

        aux = pageable.get_search_type()
        
        if aux == "smart":
            QUERY = get_item_query_smart(params.dict())
        
        elif aux == "anywhere":
            QUERY = get_item_query_anywhere(params.dict())
        
        else aux == "exact":
            QUERY = get_item_query_exact(params.dict())

        result = es.search(index=ES_INDEX_ITEM,
                           query=QUERY,
                           from_= pageable.get_page() * pageable.get_size(),
                           size= pageable.get_size(),
                           sort=[{pageable.get_sort(): pageable.get_order()}, "_score"],
                           filter_path='hits.hits._source',
                           request_timeout=20,
                           ignore=[400, 404])

        if "hits" not in result:
            return []

        hits = result["hits"]["hits"]
        return [item['_source'] for item in hits]

    def list_sample(params: ListItemsQuery, pageable: Pageable):

        aux = pageable.get_search_type()
        
        if aux == "smart":
            QUERY = get_item_query_smart(params.dict())
        
        elif aux == "anywhere":
            QUERY = get_item_query_anywhere(params.dict())
        
        else aux == "exact":
            QUERY = get_item_query_exact(params.dict())

        
        fields = ['id_item', 'original', 'original_dsc', 'dsc_unidade_medida', 'grupo', 'data',
                  'modalidade', 'tipo_licitacao', 'nome_vencedor', 'orgao',
                  'municipio', 'qtde_item', 'preco']
        result = es.search(index=ES_INDEX_ITEM,
                           query=QUERY,
                           from_=pageable.get_page() * pageable.get_size(),
                           size=pageable.get_size(),
                           sort=[{pageable.get_sort(): pageable.get_order()}, "_score"],
                           _source_includes=fields,
                           filter_path='hits',
                           track_total_hits=True,
                           request_timeout=20,
                           ignore=[400, 404])

        if "hits" not in result:
            return {}

        hits = result["hits"]["hits"]        
        res = {
            # max(101, result["hits"]["total"]["value"]),  # total de itens
            "total": result["hits"]["total"]["value"],
            "pageSize": pageable.get_size(),  # qtd de itens por página
            "currentPage": pageable.get_page(),  # página atual
            "data": [item['_source'] for item in hits]  # dados
        }        
        return res


    def list_items_with_values(params: ListItemsQuery):
        warn('This service is deprecated.', DeprecationWarning, stacklevel=1)
        # if params.description:
        #     filters.append(ItemModel.original.__eq__(params.description))
        #
        # if params.unit_measure:
        #     filters.append(ItemModel.dsc_unidade_medida.__eq__(params.unit_measure))
        #
        # result = db_session.query(ItemModel) \
        #                    .filter(and_(*filters)) \
        #                    .offset(params.offset) \
        #                    .limit(params.limit)
        #
        # res = [row.__dict__ for row in result]
        # for item in res:
        #     item['preco'] = round(item['preco'], 2)
        #
        # return res
