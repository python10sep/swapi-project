"""

"""

from pydantic import BaseModel
from models.basemodel import Base

from typing import List, str, Optional


class Character(Base):
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
