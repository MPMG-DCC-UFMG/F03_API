from typing import Optional
from fastapi import APIRouter, Query

class ListGroupsQueryParams:
    def __init__(
        self,
        limit: int = Query(15, description="Query limit"),
        offset: int = Query(0, description="Query offset"),
        sort: Optional[str] = Query(None,description="Atributo de ordenação"),
        order: Optional[str] = Query("desc",description="Critério de ordenação", regex="^asc|desc$"),
        name: Optional[str] = Query(None, description="Nome do grupo"),
        first_token: Optional[str] = Query(None, description="Primeiro termo"),
        unit:  Optional[str] = Query(None, description="Unidade de medida"),
    ):
        self.limit = limit
        self.offset = offset
        self.sort = sort
        self.order = order
        self.name = name
        self.first_token = first_token
        self.unit = unit

class GetGroupByFirstToken:
    def __init__(
        self,
        first_token: str = Query('seringa', description='First token')
    ):
        self.first_token = first_token
