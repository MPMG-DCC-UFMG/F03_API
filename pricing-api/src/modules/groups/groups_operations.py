from typing import Optional
from fastapi import APIRouter, Query
from pydantic import BaseModel

class ListGroupsQuery(BaseModel):
    limit: int = Query(15, description="Query limit")
    offset: int = Query(0, description="Query offset")
    sort: Optional[str] = Query(None,description="Atributo de ordenação")
    order: Optional[str] = Query("desc",description="Critério de ordenação", regex="^asc|desc$")
    name: Optional[str] = Query(None, description="Nome do grupo")
    first_token: Optional[str] = Query(None, description="Primeiro termo")
    unit:  Optional[str] = Query(None, description="Unidade de medida")
    noise: Optional[bool] = Query(False, description="Apresentar grupos de ruídos")


class GetGroupByFirstToken(BaseModel):
    first_token: str = Query('seringa', description='First token')

