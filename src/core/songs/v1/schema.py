from decimal import Decimal

from pydantic import BaseModel
from pydantic import Field


class SongItemInList(BaseModel):
    artist: str = Field(description='Artist')
    title: str = Field(description='Title')
    difficulty: Decimal = Field(description='Difficulty')
    level: int = Field(description='Level')
    released: str = Field(description='Released date')
