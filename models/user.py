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
