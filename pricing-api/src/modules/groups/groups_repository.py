from src.modules.groups.groups_operations import ListGroupsQueryParams
from src.modules.groups.group import GroupModel
from src.db.database import db_session
class GroupsRepository:
    
    def find_by_id(id:str):
        return {"id": 1, "name": "xpto_1", "units_of_measures": ["unidade", "dúzia"]}

    
    def list(params: ListGroupsQueryParams):
        rows = db_session.query(GroupModel)[params.offset:params.limit]
        return list(map(lambda x: x.__dict__, rows))