from typing import Dict
from aniso8601 import parse_date, parse_datetime
from flask_restx import Resource, Model, fields
from ml_rest_api.api.restx import api


def build_api_model(model_sample, name) -> Model:
    """
    Returns a Flask-RESTX Api Model based on the sample dict returned by the
    trained model wrapper. This will be used to validate input and automatically
    generate the Swagger prototype.
    """
    fields_classes_map: Dict = {
        "str": fields.String,
        "int": fields.Integer,
        "float": fields.Float,
        "bool": fields.Boolean,
        "datetime": fields.DateTime,
        "date": fields.Date,
    }
    model_dict: Dict = {}

    if model_sample:
        for key, value in model_sample.items():
            fields_class: fields.Raw = fields_classes_map.get(
                type(value).__name__, fields.String
            )
            if type(value).__name__ == "str":
                try:
                    parse_date(value)
                    fields_class = fields.Date
                except ValueError:
                    pass
                try:
                    parse_datetime(value)
                    fields_class = fields.DateTime
                except ValueError:
                    pass
            model_dict[key] = fields_class(example=value, readonly=True,
                                           required=True)

    return api.model(name, model_dict)
