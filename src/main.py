import json
import socket
from contextvars import ContextVar
from datetime import datetime

from flasgger import Swagger
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

import settings
from api import api_bp
from utils.logging.logger import JsonStdOutLogger


def init_app() -> Flask:
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config.from_file("config.json", load=json.load)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.before_request_funcs = dict(api=[set_context_vars, logging_data])
    app.after_request_funcs = dict(api=[logging])
    app.swagger = Swagger(app)
    print(app.url_map)
    return app


TRACE_ID = ContextVar('TRACE_ID', default='None')

logger = JsonStdOutLogger('api-logger')


# sentry_sdk.init(
#     dsn=settings.SENTRY_DSN,
#     integrations=[FlaskIntegration()]
# )


def logging_data():
    from flask import request
    request.headers.environ['time_start'] = datetime.now()


def set_context_vars():
    from flask import request
    TRACE_ID.set(request.headers.get('X-TRACE-ID', 'unknown'))


def logging(response):
    from flask import request

    if 'swagger' not in request.path:
        log_data: dict = {
            'client_ip':           request.remote_addr,
            'request_time':        abs((datetime.now() - request.headers.environ['time_start']).total_seconds()),
            'trace_id':            TRACE_ID.get(),
            'request_path':        request.path,
            'request_http_method': request.method,
            'request_headers':     logger.get_dump_data(dict(request.headers)),
            'request_data':        logger.get_dump_data(json.loads(request.data) if request.data else {}),
            'request_query':       logger.get_dump_data(request.args if request.args else {}),
            'response_code':       int(response.status_code),
            'response_data':       logger.get_dump_data(response.json if response.json else {}),
            'service_type':        settings.SERVICE_NAME,
            'server_host':         socket.gethostname(),
        }
        logger.service_log(data=log_data)
    return response


if __name__ == '__main__':
    app: Flask = init_app()
    app.run(host='0.0.0.0', port=settings.SERVICE_PORT, debug=settings.DEBUG)
