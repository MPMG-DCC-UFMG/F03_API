from flask import request
from flask_restx import Resource
from ml_rest_api.api.restx import api, FlaskApiReturnType
from .group_service import GetGroupByName, GetGroups, GetGroupsByItem

@api.default_namespace.route("/group", defaults={'group_name': None})
@api.default_namespace.route("/group/<string:group_name>")
class Group(Resource):

    """Implements the /group GET method."""
    @staticmethod
    @api.doc(
        responses={
            200: "Success",
            400: "Bad Request"
        }
    )
    def get(group_name) -> FlaskApiReturnType:
        """
        Returns group information.
        """
        if group_name:
            group = GetGroupByName(group_name)
            return group, 200
        
        params = request.args.to_dict()
        if not params: # Use request body params if there are no URL params
            body = request.get_json(silent=True) 
            params = body if body is not None else dict()
        
        if "item" in params:
            groups = GetGroupsByItem(**params)
            return groups, 200
        else:
            groups = GetGroups(**params)
            return groups, 200
        
        
