from src.modules.groups.groups_operations import ListGroupsQueryParams
from src.modules.groups.group import GroupModel
from src.db.database import db_session
from sqlalchemy import and_, desc, asc

class GroupsRepository:

    def find_by_id(id:str):
        result = db_session.query(GroupModel).get(id)
        return result.__dict__

    def list(params: ListGroupsQueryParams):
        filters = []

        if (bool(params.name)):
            filters.append(GroupModel.grupo.__eq__(params.name))
        if (bool(params.first_token)):
            filters.append(GroupModel.primeiro_termo.__eq__(params.first_token))
        if (bool(params.unit)):
            filters.append(GroupModel.dsc_unidade_medida.__eq__(params.unit))

        if not params.noise:
            filters.append(GroupModel.ruido == 0)

        sort_statement = params.sort
        order = desc(sort_statement) if params.order == "desc" else asc(sort_statement)
        rows = db_session.query(GroupModel) \
                         .filter(and_(*filters)) \
                         .offset(params.offset) \
                         .limit(params.limit)
                        #  .order_by(order) \

        return list(map(lambda x: x.__dict__, rows))
