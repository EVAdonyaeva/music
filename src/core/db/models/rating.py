from mongoengine import StringField

from . import BaseDocument


class Rating(BaseDocument):
    song_id = StringField(max_length=200, required=True)
    rating = StringField(max_length=200, required=True)
#    user_id = StringField(required=True)  seems that user can add rating to song only once
