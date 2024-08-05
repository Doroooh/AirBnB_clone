#!/usr/bin/python3

""" The class City """
from models.base_model import BaseModel


class City(BaseModel):
    """ The class City that inherits BaseModel
        Public class attribute
            state_id: (str) - State.id
            name: (str) - City name
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Initializing City
            Args:
                *args: list of strings
                **kwargs: dictionary of strings"""
        super().__init__(*args, **kwargs)
