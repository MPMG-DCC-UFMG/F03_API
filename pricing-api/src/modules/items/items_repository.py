from src.modules.items.items_operations import ListItemsQueryParams
from src.modules.items.item import ItemModel
from src.db.database import db_session
from sqlalchemy import and_

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
            filters.append(ItemModel.ilike("%" + params.description + "%"))
        if (params.group):
            filters.append(ItemModel.grupo == params.group)

        result = db_session.query(ItemModel).filter(and_(*filters))[params.offset:params.offset+params.limit]
        return [ row.__dict__ for row in result ]