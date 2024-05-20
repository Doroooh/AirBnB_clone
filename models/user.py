#!/usr/bin/python3
"""This defines the classe user module """
from models.base_model import BaseModel

class User(BaseModel):
    """This is the class defining various attributes of a user"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
