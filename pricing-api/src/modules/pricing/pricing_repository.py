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
        # TODO
        # exemplo de query gerada:
        # {
        #    "query":{
        #       "bool":{
        #          "must":[
        #
        #          ]
        #       }
        #    },
        #    "aggs":{
        #       "group_by_description-agg":{
        #          "terms":{
        #             "field":"original.keyword"
        #          },
        #          "aggs":{
        #             "group_by_unit_metric-agg":{
        #                "terms":{
        #                   "field":"dsc_unidade_medida.keyword"
        #                },
        #                "aggs":{
        #                   "group_by_year-agg":{
        #                      "terms":{
        #                         "field":"ano.keyword"
        #                      },
        #                      "aggs":{
        #                         "group_by_cluster-agg":{
        #                            "terms":{
        #                               "field":"grupo.keyword"
        #                            },
        #                            "aggs":{
        #                               "max_preco":{
        #                                  "max":{
        #                                     "field":"preco"
        #                                  }
        #                               }
        #                            }
        #                         }
        #                      }
        #                   }
        #                }
        #             }
        #          }
        #       }
        #    }
        # }
        result = es.search(index=ES_INDEX_ITEM,
                           body=QUERY,
                           #filter_path=['hits.hits._source.id_item'],
                           from_=pageable.get_page() * pageable.get_size(),
                           size=pageable.get_size(),
                           sort=[{pageable.get_sort(): pageable.get_order()}, "_score"],
                           request_timeout=60,
                           ignore=[400, 404])

        print(result)
        if "hits" not in result:
            return []

        hits = result["hits"]["hits"]
        #ids = [d["_source"]["id_item"] for d in hits]
        # filters.append(ItemModel.id_item.in_(ids))

        # Recupera apenas os itens que não são ruído.
        # if params.group_by_cluster:
        #     filters.append(ItemModel.item_ruido == 0)

        # columns = group_by_columns
        # order = desc(params.sort) if params.order == "desc" else asc(params.sort)
        # result = db_session.query(*columns,
        #                          func.round(func.avg(cast(ItemModel.preco, Float)),2).label('mean'),
        #                          func.round(func.max(cast(ItemModel.preco, Float)),2).label('max'),
        #                          func.round(func.min(cast(ItemModel.preco, Float)),2).label('min'),
        #                          func.count().label('count')) \
        #     .filter(and_(*filters)) \
        #     .group_by(*columns) \
        #     .order_by(order) \
        #     .offset(params.offset) \
        #     .limit(params.limit)
        
        return hits #[ row for row in result ]
