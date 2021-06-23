from src.modules.groups.groups_operations import ListGroupsQueryParams
from src.modules.groups.group import GroupModel
from src.db.database import db_session
from sqlalchemy import and_, desc

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

        if (bool(params.sort)):
            sort_statement = getattr(GroupModel, params.sort)
            rows = db_session.query(GroupModel).filter(and_(*filters)).order_by(desc(sort_statement))[params.offset:params.offset+params.limit]
        else:
            rows = db_session.query(GroupModel).filter(and_(*filters))[params.offset:params.offset+params.limit]

        return list(map(lambda x: x.__dict__, rows))
