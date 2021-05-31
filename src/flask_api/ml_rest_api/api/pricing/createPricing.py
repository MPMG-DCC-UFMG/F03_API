"""This module implements the CreatePricing class."""
from typing import Dict
from aniso8601 import parse_date, parse_datetime
from flask import request
from flask_restx import Resource, Model, fields
from ml_rest_api.api.restx import api, FlaskApiReturnType
from ml_rest_api.ml_trained_model.wrapper import trained_model_wrapper
from api.utils import build_api_model


ns = api.namespace(  # pylint: disable=invalid-name
    "pricing",
    description="Price an item"
)

@ns.route("/create", methods=['POST'])
class CreatePricing(Resource):
    """Implements the /pricing/create POST method."""

    model_sample: Dict =  {
	   "description": "Gasolina comum",
	   "years": [2012],
    }

    @staticmethod
    @api.expect(build_api_model(model_sample, "pricing_request"))
    @api.doc(
        responses={
            200: "Success",
            400: "Input Validation Error",
            500: "Server Not Ready"
        }
    )
    def post() -> FlaskApiReturnType:
        """
            Create a pricing object given an item description and the year to
            be considered.
        """

        pricing_request = dict(request.json)

        try:
            # TODO: pricing = ...
            return groups, 200
        except:
            return "Input Validation Error", 400
