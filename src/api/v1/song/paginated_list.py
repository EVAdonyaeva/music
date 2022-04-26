from http import HTTPStatus
from typing import Any
from typing import Dict

from flasgger import swag_from
from flask import jsonify
from flask import request
from marshmallow import Schema
from marshmallow import ValidationError
from marshmallow import fields

from core.songs.v1.get import get_paginated_songs
from core.songs.v1.get import get_songs_count

from . import song_bp


class PaginatedSongListRequest(Schema):
    page = fields.Integer(required=True, default=1, description='Page number')
    limit = fields.Integer(required=True, default=10, description='Number of songs per page')


class PaginatedSongListResponse(Schema):
    count = fields.Integer(required=True, default=1, description='Page number')
    songs = fields.Integer(required=True, default=10, description='Number of songs per page')


@song_bp.route('/list', methods=["GET"])
@swag_from({
    'request':   {
        'schema': PaginatedSongListRequest,
    },
    'responses': {
        HTTPStatus.OK: {
            'schema': PaginatedSongListResponse,
        }
    }
}, validation=True)
def paginated_song_list():
    """
    Returns a list of songs with pagination.
    :return:
    """
    request_data: Dict[str, Any] = request.json
    try:
        # Validate request body against schema data types
        validated_request: Dict[str, Any] = PaginatedSongListRequest().load(request_data)
    except ValidationError as err:
        # Return a nice message if validation fails
        return jsonify(err.messages), 400

    response = dict(
        count=get_songs_count(),
        songs=get_paginated_songs(
            limit=validated_request['limit'],
            page=validated_request['page'],
        ))

    try:
        # Validate request body against schema data types
        validated_response: Dict[str, Any] = PaginatedSongListResponse().load(response)
    except ValidationError as err:
        # Return a nice message if validation fails
        return jsonify(err.messages), 400

    return jsonify(validated_response), 200
