from mongoengine import connect

from settings import MONGO_CONNECTION_POOL_MAXSIZE
from settings import MONGO_DB
from settings import MONGO_PASSWORD
from settings import MONGO_USER
from settings import MONGODB_HOST
from settings import MONGODB_PORT
from utils.logging.logger import JsonStdOutLogger


# Connecting to MongoDB
db_client = connect(
    host=MONGODB_HOST,
    port=MONGODB_PORT,
    username=MONGO_USER,
    password=MONGO_PASSWORD,
    db=MONGO_DB,
    maxPoolSize=MONGO_CONNECTION_POOL_MAXSIZE,
)

db_logger = JsonStdOutLogger('db-logger')
