from typing import List

from .client import db_client
from .models.song import Song


def songs_count() -> int:
    return db_client.songs.count_documents({})


def get_paginated_song_list(page: int, limit: int) -> List[Song]:
    return db_client.songs.find().skip(limit * (page - 1)).limit(limit)
