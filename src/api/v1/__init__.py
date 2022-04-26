from flask import Blueprint

from .song import song_bp


v1_bp = Blueprint('v1', __name__)

v1_bp.register_blueprint(song_bp, url_prefix='/song')
