from src.modules.groups.groups_operations import ListGroupsQueryParams

class GroupsRepository:
    
    def find_by_id(id:str):
        return {"id": 1, "name": "xpto_1", "units_of_measures": ["unidade", "dúzia"]}
    
    def list(params: ListGroupsQueryParams):
        return [{"id": 1, "name": "xpto_1", "units_of_measures": ["unidade", "dúzia"]}]