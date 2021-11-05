from src.modules.filters.filters_operations import ListFiltersQueryParams
from src.modules.items.item import ItemModel
from src.db.database import db_session
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

        query = db_session\
            .query(column)\
            .distinct()\
            .filter(and_(*filters))\
            .order_by(desc(params.column))\
            .offset(params.offset)\
            .limit(params.limit)

        return [x[0] for x in query.all()]
