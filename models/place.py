#!/usr/bin/python3
"""Place module for the project."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defining the Place class."""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 
