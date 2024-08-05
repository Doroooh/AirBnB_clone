#!/usr/bin/python3

""" The class amenity """
from models.base_model import BaseModel

class Amenity(BaseModel):
    """ The class amenity will inherit the BaseModel
        Public class attribute
            name: (string) - the amenity name
    """
    
    name = ""
    
    def __init__(self, *args, **kwargs):
        """ Initializing Amenity
            Args:
                *args: The list of strings
                **kwargs: The dictionary of strings
        """
        super().__init__(*args, **kwargs)
