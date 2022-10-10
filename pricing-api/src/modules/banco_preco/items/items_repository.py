import os

from warnings import warn

from dotenv import load_dotenv

from src.db.database import es
from src.modules.banco_preco.items.items_operations import ListItemsQuery
from src.modules.banco_preco.utils.utils import (
    get_item_query,
    get_overprincing_query,
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

        QUERY = get_item_query(params.dict(), pageable.get_search_type())
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

        QUERY = get_item_query(params.dict(), pageable.get_search_type())        
        fields = ['id_item', 'original', 'original_dsc', 'dsc_unidade_medida', 'data',
                  'id_licitacao', 'modalidade', 'tipo_licitacao', 'nome_vencedor', 'orgao', 
                  'num_processo', 'num_modalidade', 'municipio', 'qtde_item', 'preco']
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

    def list_sample_overprice(params: ListItemsQuery, pageable: Pageable):

        QUERY = get_overprincing_query(params.dict(), pageable, pageable.get_search_type())
        result = es.search(index=ES_INDEX_ITEM,
                           body=QUERY,
                           request_timeout=60,
                           ignore=[400, 404])
        
        if "aggregations" not in result:
            return []
        
        aggr = result['aggregations']['group_by_grupo-agg']['buckets']
        data = []
        for a in aggr:
            bucket = {}
            bucket_data = []
            bucket['group_by_grupo'] = a['key']
            bucket['group_size'] = a['stats_preco']['count']
            bucket['avg_preco'] = a['stats_preco']['avg']
            bucket['min_preco'] = a['stats_preco']['min']
            bucket['max_preco'] = a['stats_preco']['max']
            bucket['std_preco'] = a['stats_preco']['std_deviation']
            for i in a['top_grupo_hits']['hits']['hits']:
                bucket_data.append(i['_source'])
            bucket['data'] = bucket_data
            data.append(bucket)
                 
        res = {
            # max(101, result["hits"]["total"]["value"]),  # total de itens
            # "total": result['aggregations']['all_buckets']['count'],
            "pageSize": pageable.get_size(),  # qtd de itens por página
            "currentPage": pageable.get_page(),  # página atual
            "data": data  # dados
        }       
        return res
    
    def list_overprice(params: ListItemsQuery, pageable: Pageable):

        QUERY = get_item_query(params.dict(), pageable.get_search_type())
        BODY = {
            "size": 0,
            'query': QUERY,
            'aggs': {
                "group_by_cluster": {
                    "terms": {
                        "field": "grupo_unidade_medida.keyword", 
                        "order": {"_key": "asc" }, 
                        "size": 999999
                    },
                    "aggs": {
                        "stats_preco": {"extended_stats": {"field": "preco"}}
                    }
                }
            }
        }
        
        result = es.search(index=ES_INDEX_ITEM,
                           body=BODY,
                           request_timeout=60,
                           ignore=[400, 404])

        if "aggregations" not in result:
            return []
        
        arr = result['aggregations']['group_by_cluster']['buckets']
        groups = {}
        for a in arr:
            if ((a['stats_preco']['count'] > 10) and ('-1' not in a['key'])):
                groups[a['key']] = {
                    'group_size': a['stats_preco']['count'],
                    'avg_preco': a['stats_preco']['avg'],
                    'min_preco': a['stats_preco']['min'],
                    'max_preco': a['stats_preco']['max'],
                    'std_preco': a['stats_preco']['std_deviation'],
                    'threshold': a['stats_preco']['avg'] + a['stats_preco']['std_deviation']
                }
        
        QUERY['bool']['must'].append({
                "terms": {"grupo_unidade_medida.keyword": list(groups.keys())}
            })
        
        fields = ['id_item', 'original', 'original_dsc', 'dsc_unidade_medida', 'data',
                  'grupo_unidade_medida', 'id_licitacao', 'modalidade', 'tipo_licitacao', 
                  'nome_vencedor', 'orgao', 'num_processo', 'num_modalidade', 'municipio', 
                  'qtde_item', 'preco']
        BODY = {
            "track_total_hits": True, 
            "from": pageable.get_page() * pageable.get_size(),
            "size": pageable.get_size(),
            'query': QUERY,
            'sort': {
                "_script": {
                    "type": "number",
                    "script": {
                        "lang": "painless",
                        "source": "return doc['preco'].value - params.values[doc['grupo_unidade_medida.keyword'].value]['threshold'];",
                        "params": {"values":  groups}
                    },
                    "order": pageable.get_order()
                }
            }
        }
                
        result = es.search(index=ES_INDEX_ITEM,
                           body=BODY,
                           _source_includes=fields,
                           request_timeout=60,
                           ignore=[400, 404])

        if "hits" not in result:
            return {}
        
        hits = result['hits']['hits']
        data = [item['_source'] for item in hits]
        for item in data:
            item['group_data'] = groups[item['grupo_unidade_medida']]
        
        res = {
            "total": result["hits"]["total"]["value"],
            "pageSize": pageable.get_size(),  # qtd de itens por página
            "currentPage": pageable.get_page(),  # página atual
            "data": data  # dados
        }
        return res

