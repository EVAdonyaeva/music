from mongoengine import DateField
from mongoengine import DecimalField
from mongoengine import IntField
from mongoengine import StringField

from . import BaseDocument


class Song(BaseDocument):
    artist = StringField(max_length=200, required=True)
    title = StringField(max_length=200, required=True)
    difficulty = DecimalField(required=True)
    level = IntField(required=True)
    released = DateField(required=True)
    max_rating = DecimalField(required=True)
    min_rating = DecimalField(required=True)
    average_rating = DecimalField(required=True)

    meta = {
        'indexes': [
            '#artist',
            '#title',
        ]
    }
