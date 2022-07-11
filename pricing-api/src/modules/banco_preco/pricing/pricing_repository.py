import os

from dotenv import load_dotenv

from src.db.database import es
from src.modules.banco_preco.pricing.pricing_operations import PricingQuery
from src.modules.banco_preco.utils.utils import Pageable
from src.modules.banco_preco.utils.utils import get_princing_query

load_dotenv()
ES_INDEX_ITEM = os.environ.get('ES_INDEX_ITEM')

class PricingRepository:

    def get(params: PricingQuery, group_by_columns, pageable: Pageable):
        QUERY = get_princing_query(params.dict(), group_by_columns, pageable)
        # print(f'QUERY: {QUERY}\n')
        
        result = es.search(index=ES_INDEX_ITEM,
                           body=QUERY,
                        #    filter_path=['hits.hits._source.id_item'],
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
            
            bucket['max_preco'] = a['max_preco']['value']
            bucket['min_preco'] = a['min_preco']['value']
            bucket['avg_preco'] = a['avg_preco']['value']
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
