from src.modules.banco_preco.utils.utils import get_group_query
from src.modules.banco_preco.groups.groups_operations import ListGroupsQuery
from src.modules.banco_preco.groups.group import GroupModel
from src.db.database import db_session, es
from sqlalchemy import and_, desc, asc

from dotenv import load_dotenv
import os

load_dotenv()

ES_INDEX_ITEM = os.environ.get('ES_INDEX_ITEM')



class GroupsRepository:

    def find_by_id(id: str):
        result = db_session.query(GroupModel).get(id)
        return result.__dict__

    def list(params: ListGroupsQuery):
        query = get_group_query(params.dict())

        result = es.search(index=ES_INDEX_ITEM,
                           body=query,
                           request_timeout=20,
                           ignore=[400, 404],
                           size=500)

        if "hits" not in result:
            return []

        hits = result["hits"]["hits"]

        return hits
