"""This module implements the Item class."""
from flask_restx import Resource
from flask import request
from ml_rest_api.api.restx import api, FlaskApiReturnType
from .item_service import GetItems, GetItemByDescription, GetItemById, GetItemsByDescription, GetItemsByFirstToken

#TODO: SQLAlchemy?
#TODO: Change request methods or parameter containers

@api.default_namespace.route("/item", defaults={'item_id': None})
@api.default_namespace.route("/item/<string:item_id>")
class Item(Resource):
    """Implements the /item GET method."""

    @staticmethod
    @api.doc(
        responses={
            200: "Success",
            400: "Bad Request"
        }
    )
    def get(item_id) -> FlaskApiReturnType:
        """
        Returns Item information.
        """
        params = request.args.to_dict()
        if not params: # Use request body params if there are no URL params
            body = request.get_json(silent=True)
            params = body if body is not None else dict()
        
        if item_id:
            item = GetItemById(item_id)
            return item, 200
        
        # TODO: Extract a single Item Service query method and add filters programatically

        if "first_token" in params: # List items by first token
            items = GetItemsByFirstToken(**params)
            return items, 200
        elif "description" in params: 
            if "year" in params: # Get item by its exact description and year
                item = GetItemByDescription(**params)
                return item, 200
            else: # List items by description
                items = GetItemsByDescription(**params) 
                return items, 200
        else: # List all items
            items = GetItems(**params)
            return items, 200