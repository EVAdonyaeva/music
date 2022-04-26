import uuid
from datetime import datetime

from mongoengine import DateTimeField
from mongoengine import Document
from mongoengine import StringField


class BaseDocument(Document):
    id = StringField(required=True, default=lambda: str(uuid.uuid4()))
    created_at = DateTimeField(required=True, default=lambda: datetime.utcnow())
