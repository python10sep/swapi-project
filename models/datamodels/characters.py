"""

"""

from pydantic import BaseModel, validator
from models.basemodel import Base

from typing import List, Optional


class Character_(Base):
    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    homeworld: str

    species: Optional[List[str]]
    starships: Optional[List[str]]
    films: Optional[List[str]]
    vehicles: Optional[List[str]]

    @validator("height")
    def height_validation(cls):
        if isinstance(cls.height, str):
            height = int(cls.height)
            height = height / 100
            cls.height = height
            return cls.height
        else:
            raise ValueError('height cannot be converted')
