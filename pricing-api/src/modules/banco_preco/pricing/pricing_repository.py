import os

from dotenv import load_dotenv

from src.db.database import es
from src.modules.banco_preco.pricing.pricing_operations import PricingQuery
from src.modules.banco_preco.utils.utils import (
    get_item_query_smart,
    get_item_query_anywhere,
    get_item_query_exact,
    get_princing_query,
    Pageable
)

load_dotenv()
ES_INDEX_ITEM = os.environ.get('ES_INDEX_ITEM')

class PricingRepository:

    def get(params: PricingQuery, group_by_columns, pageable: Pageable):
        
        search_type = pageable.get_search_type()        
        QUERY = get_princing_query(params.dict(), group_by_columns, pageable, search_type)
        
        result = es.search(index=ES_INDEX_ITEM,
                           body=QUERY,
                           request_timeout=60,
                           ignore=[400, 404])

        if "aggregations" not in result:
            return []
        

        arr = result['aggregations']['group_by_script']['buckets']
        data = []
        for a in arr:
            a_split = a['key'].split('__!@#$%__')
            bucket = {}
            for i, gc in enumerate(group_by_columns):
                bucket[gc] = a_split[i]
            
            bucket['max_preco'] = a['stats_preco']['max']
            bucket['min_preco'] = a['stats_preco']['min']
            bucket['avg_preco'] = a['stats_preco']['avg']
            bucket['std_preco'] = a['stats_preco']['std_deviation']
            bucket['sum_qtde_item'] = a['sum_qtde_item']['value']
            data.append(bucket)
            
        res = {
            # total de itens
            # "total": result['aggregations']['all_buckets']['count'],
            "pageSize": pageable.get_size(),  # qtd de itens por página
            "currentPage": pageable.get_page(),  # página atual
            "data": data  # dados
        }
        return res
