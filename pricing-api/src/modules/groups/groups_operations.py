from typing import Optional
from fastapi import APIRouter, Query

class ListGroupsQueryParams:
    def __init__(
        self,
        limit: int = Query(15, description="Query limit"),
        offset: int = Query(0, description="Query offset"),
        sort: Optional[str] = Query(None,description="The sorting attribute"),
        name: Optional[str] = Query(None, description="Group name"),
        first_token: Optional[str] = Query(None, description="Group first token"),
        unit:  Optional[str] = Query(None, description="Group unit of measure"),
    ):
        self.limit = limit
        self.offset = offset
        self.sort = sort
        self.name = name
        self.first_token = first_token
        self.unit = unit
class GetGroupByFirstToken:
    def __init__(
        self,
        first_token: str = Query('seringa', description='First token')
    ):
        self.first_token = first_token