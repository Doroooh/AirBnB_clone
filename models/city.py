#!/usr/bin/python3
"""defining interpreter location"""
from models.base_model import BaseModel
"""import models"""

class City(BaseModel):
    """This is the main class inherited of BaseModel that will manage Cities"""
    state_id = ""
    name = ""
