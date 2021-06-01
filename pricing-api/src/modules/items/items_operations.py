from typing import Optional
from fastapi import Query

class ListItemsQueryParams:
    def __init__(
        self,
        limit: int = Query(0, description="Query limit"),
        offset: int = Query(15, description="Query offset"),
        sort: Optional[str] = Query(None,description="The sorting attribute"),
        description: Optional[str] = Query(None, description="Item name"),
    ):
        self.limit = limit
        self.offset = offset
        self.sort = sort
        self.description = description