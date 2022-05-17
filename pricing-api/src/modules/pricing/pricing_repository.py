import os

from dotenv import load_dotenv

from src.db.database import es
from src.modules.pricing.pricing_operations import PricingQuery
from src.modules.utils.utils import Pageable
from src.modules.utils.utils import get_princing_query

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
                           size=0,
                           ignore=[400, 404])

        if "aggregations" not in result:
            return []
        
        res = []
        if len(group_by_columns) == 1:
            for a in result['aggregations'][group_by_columns[0] + '-agg']['buckets']:
                res.append({
                    group_by_columns[0]: a['key'],
                    'max_preco': a['max_preco']['value'],
                    'min_preco': a['min_preco']['value'],
                    'avg_preco': a['avg_preco']['value'],
                    'sum_qtde_item': a['sum_qtde_item']['value']                    
                })
        elif len(group_by_columns) == 2:
            for a in result['aggregations'][group_by_columns[0] + '-agg']['buckets']:
                for b in a[group_by_columns[1] + '-agg']['buckets']:
                    res.append({
                        group_by_columns[0]: a['key'],
                        group_by_columns[1]: b['key'],
                        'max_preco': b['max_preco']['value'],
                        'min_preco': b['min_preco']['value'],
                        'avg_preco': b['avg_preco']['value'],
                        'sum_qtde_item': b['sum_qtde_item']['value']                    
                    })
        elif len(group_by_columns) == 3:
            for a in result['aggregations'][group_by_columns[0] + '-agg']['buckets']:
                for b in a[group_by_columns[1] + '-agg']['buckets']:
                    for c in b[group_by_columns[2] + '-agg']['buckets']:
                        res.append({
                            group_by_columns[0]: a['key'],
                            group_by_columns[1]: b['key'],
                            group_by_columns[2]: c['key'],
                            'max_preco': c['max_preco']['value'],
                            'min_preco': c['min_preco']['value'],
                            'avg_preco': c['avg_preco']['value'],
                            'sum_qtde_item': c['sum_qtde_item']['value']
                        })
        return res
