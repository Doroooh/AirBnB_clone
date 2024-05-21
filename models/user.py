#!/usr/bin/python3
"""This defines the classe user module """
from models.base_model import BaseModel

class User(BaseModel):
    """This is the class defining various attributes of a user"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''


#!/usr/bin/python3
"""location interpreter"""
from models.base_model import BaseModel
"""import models"""

class User(BaseModel):
    """It manages the users, that is consumers"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
