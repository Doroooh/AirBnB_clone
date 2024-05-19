#!/usr/bin/python3
"""Defining the City class."""
from models.base_model import BaseModel

class City(BaseModel):
    """this represents the a city.

    Attributes:
        state_id (str): This is the state id.
        name (str): city name.
    """

    state_id = ""
    name = ""
