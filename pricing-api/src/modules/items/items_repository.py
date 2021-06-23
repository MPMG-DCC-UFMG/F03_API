from src.modules.items.items_operations import ListItemsQueryParams
from src.modules.items.item import ItemModel
from src.db.database import db_session
from sqlalchemy import and_, desc, asc

class ItemsRepository:
    
    def find_by_id(id:str):
        result = db_session.query(ItemModel).get(id)
        return result.__dict__
    
    def list(params: ListItemsQueryParams):

        filters = []
        # Ideia: passar a construção dessa lista filters para o construtor da classe ListItemsQueryParams.
        if (params.county):
            filters.append(ItemModel.municipio == params.county)   
        if (params.year):
            filters.append(ItemModel.ano.in_(params.year))
        if (params.description):
            filters.append(ItemModel.original.ilike("%" + params.description + "%"))
        if (params.group):
            filters.append(ItemModel.grupo == params.group)
        if (params.before):
            filters.append(ItemModel.data <= params.before)
        if (params.after):
            filters.append(ItemModel.data >= params.after)
        filters.append(ItemModel.item_ruido == 0) # Recupera apenas os itens que não são ruído.
        order = desc(params.sort) if params.order == "desc" else asc(params.sort)
        result = db_session.query(ItemModel).filter(and_(*filters)).order_by(order)[params.offset:params.offset+params.limit]
        return [ row.__dict__ for row in result ]