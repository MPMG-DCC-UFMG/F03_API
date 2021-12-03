from src.modules.items.items_operations import ListItemsQueryParams
from src.modules.items.item import ItemModel
from src.db.database import db_session, es
from sqlalchemy import and_, desc, asc
from sqlalchemy.orm import load_only

class ItemsRepository:

    def find_by_id(id:str):
        result = db_session.query(ItemModel).get(id)
        return result.__dict__

    def list(params: ListItemsQueryParams):
        filters = params.filters
        filters.append(ItemModel.item_ruido == 0) # Recupera apenas os itens que não são ruído.

        QUERY = {
            "_source": False,
            "query": {
                "bool": {
                  "must": {
                    "match": {
                      "original": params.description
                    }
                  }
                }
            }
        }

        if params.description:
            result = es.search(index="item", body=QUERY)
            hits = result["hits"]["hits"]
            ids = [int(d["_id"]) for d in hits]
            filters.append(ItemModel.item_id.in_(ids))
            params.reset_description() # para evitar de ser filtrado novamente

        # TODO: retornar os ids dos itens

        # TODO: buscar os itens na tabela do druid que possuem os id retornados
        # pelo elasticsearch

        order = desc(params.sort) if params.order == "desc" else asc(params.sort)
        result = db_session.query(ItemModel).filter(and_(*filters)).order_by(order)
        result = result[params.offset:params.offset+params.limit]
        return [ row.__dict__ for row in result ]

    def list_sample(params: ListItemsQueryParams):
        filters = params.filters
        filters.append(ItemModel.item_ruido == 0) # Recupera apenas os itens que não são ruído.

        fields = ['original', 'original_dsc', 'dsc_unidade_medida', 'grupo', 'data', \
                  'modalidade', 'tipo_licitacao', 'nome_vencedor', 'orgao', \
                  'municipio', 'qtde_item', 'preco']
        order = desc(params.sort) if params.order == "desc" else asc(params.sort)
        result = db_session.query(ItemModel).filter(and_(*filters)).options(load_only(*fields)).order_by(order)[params.offset:params.offset+params.limit]

        return [ row.__dict__ for row in result ]
