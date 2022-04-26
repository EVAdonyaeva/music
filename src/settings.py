import os


DEBUG: bool = bool(int(os.getenv('DEBUG', '1')))
SERVICE_NAME: str = 'songs-service'
SERVICE_PORT: int = int(os.getenv('SERVICE_PORT', '8087'))

# Swagger
STATIC_PATH: str = '/static/flask-swagger'
OPEN_API_PATH: str = '/api/songs/swagger/doc.json'

PROJECT_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SENTRY_DSN: str = os.getenv('SENTRY_DSN', 'localhost')

MONGODB_HOST: str = os.environ['MONGODB_HOST']
MONGODB_PORT: int = os.getenv('MONGODB_PORT', 27017)
MONGO_DB: str = os.environ['MONGO_DB']
MONGO_USER: str = os.environ['MONGO_USER']
MONGO_PASSWORD: str = os.environ['MONGO_PASSWORD']
MONGO_CONNECTION_POOL_MAXSIZE: int = os.getenv('MONGO_CONNECTION_POOL_MAXSIZE', 100)
