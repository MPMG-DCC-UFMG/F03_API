from src.modules.charts.charts_operations import ChartsQueryParams
from src.modules.items.item import ItemModel
from src.db.database import db_session

from sqlalchemy import and_
from collections import defaultdict
import numpy as np

class ChartsRepository:

    def get_aggregate(params: ChartsQueryParams):
        filters = params.filters

        if params.description:
            filters.append(ItemModel.original.__eq__(params.description))

        if params.unit_measure:
            filters.append(
                ItemModel.dsc_unidade_medida.__eq__(params.unit_measure))

        result = db_session.query(ItemModel) \
                           .filter(and_(*filters)) \
                           .offset(params.offset) \
                           .limit(params.limit)

        res = [row.__dict__ for row in result]

        pivot = defaultdict(list)
        pivot2 = defaultdict(list)
        for item in res:
            pivot2[item['data']].append(item['preco'])
            pivot[item['data']].append(item['qtde_item'])
        
        dict_x = [{'data': k, 'qtde_item': sum(values)} for k, values in pivot.items()]
        dict_y = [{'data': k, 'mean_preco': round(np.mean(values), 2), 'median_preco': round(np.median(values),2)} for k, values in pivot2.items()]
            
        return [{**dx, **dy} for dx, dy in zip(dict_x, dict_y)]
