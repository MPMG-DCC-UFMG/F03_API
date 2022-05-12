import os

from dotenv import load_dotenv

from src.db.database import es
from src.modules.pricing.pricing_operations import PricingQuery
from src.modules.utils.utils import Pageable
from src.modules.utils.utils import get_princing_query, get_item_query

load_dotenv()
ES_INDEX_ITEM = os.environ.get('ES_INDEX_ITEM')


class PricingRepository:

    def get(params: PricingQuery, group_by_columns, pageable: Pageable):
        QUERY = get_princing_query(params.dict(), group_by_columns)
        # print(f'QUERY: {QUERY}\n')
        
        result = es.search(index=ES_INDEX_ITEM,
                           body=QUERY,
                           #filter_path=['hits.hits._source.id_item'],
                           #from_=pageable.get_page() * pageable.get_size(),
                           #size=0,
                           #sort=[{pageable.get_sort(): pageable.get_order()}, "_score"],
                           request_timeout=60,
                           ignore=[400, 404])

        if "aggregations" not in result:
            return []
        
        if len(group_by_columns) == 1:
            first_key = result["aggregations"][group_by_columns[0] +
                                               "-agg"]["buckets"][0]["key"]
        elif len(group_by_columns) == 2:
            first_key = result["aggregations"][group_by_columns[0] +
                                               "-agg"]["buckets"][0]["key"]
            second_key = result["aggregations"][group_by_columns[0] +
                                                "-agg"]["buckets"][0][group_by_columns[1]+"-agg"]["buckets"][0]["key"]
        elif len(group_by_columns) == 3:
            first_key = result["aggregations"][group_by_columns[0] +
                                               "-agg"]['buckets'][0]["key"]
            second_key = result["aggregations"][group_by_columns[0] +
                                                "-agg"]["buckets"][0][group_by_columns[1]+"-agg"]["buckets"][0]["key"]
            third_key = result["aggregations"][group_by_columns[0] +
                                               "-agg"]['buckets'][0][group_by_columns[1]+"-agg"]["buckets"][0][group_by_columns[2]+"-agg"]["buckets"][0]["key"]
        
        print(first_key, second_key, third_key)
        hits = result["aggregations"][group_by_columns[0]+"-agg"]['buckets']
        return hits
