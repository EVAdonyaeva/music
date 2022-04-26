from functools import wraps
from typing import Callable

from flask import jsonify
from flask import request
from marshmallow import Schema
from marshmallow import ValidationError


def validate_request(f: Callable, schema: Schema):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            # Validate request body against schema data types
            request.validated_data = schema.load(request.json)
        except ValidationError as err:
            # Return a nice message if validation fails
            return jsonify(err.messages), 400

        return f(*args, **kwargs)

    return decorated_function
