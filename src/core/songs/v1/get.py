from decimal import Decimal
from typing import Dict
from typing import List
from typing import Union

from core.db.song import get_paginated_song_list
from core.db.song import songs_count

from .schema import SongItemInList


def get_paginated_songs(page: int, limit: int) -> List[Dict[str, Union[str, Decimal, int]]]:
    """
    Get paginated song list
    :param page:
    :param limit:
    :return:
    """
    return [
        SongItemInList(
            artist=song.artist,
            title=song.title,
            difficulty=song.difficulty,
            level=song.level,
            released=song.released,
        ).dict()
        for song in get_paginated_song_list(
            page=page,
            limit=limit,
        )
    ]


def get_songs_count() -> int:
    return songs_count()
