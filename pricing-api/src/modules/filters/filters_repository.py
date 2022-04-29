from src.modules.filters.filters_operations import ListFiltersQueryParams
from src.modules.items.item import ItemModel
from src.db.database import db_session, es
from sqlalchemy import and_, desc, asc, func

class FilterRepository:
    def list(params: ListFiltersQueryParams):
        filters = []
        column = getattr(ItemModel, params.column)

        if params.prefix:
            prefix = f"{params.prefix}%"
            filters.append(column.ilike(prefix))
        if params.contains:
            contains = f"%{params.contains}%"
            filters.append(column.ilike(contains))

        query = db_session \
            .query(column) \
            .distinct() \
            .filter(and_(*filters)) \
            .order_by(desc(params.column)) \
            .offset(params.offset) \
            .limit(params.limit)

        return [x[0] for x in query.all() if x[0] != None]

    def autocomplete_bidder_name(bidder_name: str):

        QUERY = {
            "suggest-exact": {
                "prefix": bidder_name,
                "completion": {
                    "field": "nome_vencedor",
                    "skip_duplicates": True,
                    "size": 5
                }
            }
        }

        result = es.search(index="f03-item", suggest=QUERY,
                           filter_path=['suggest.suggest-exact'],
                           request_timeout=20)

        if "suggest" not in result:
            return []

        hits = result["suggest"]["suggest-exact"][0]['options']
        descriptions = [d['text'] for d in hits]

        n = len(descriptions)
        res = [{'bidder_name': descriptions[idx]} for idx in range(0, n)]
        
        return res
