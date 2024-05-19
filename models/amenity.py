#!/usr/bin/python3
"""this is defining my Amenity class."""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Represents the amenity.

    Attributes:
        name (str): This is the name of the amenity.
    """

    name = ""
