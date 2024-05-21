#!/usr/bin/python3
"""interpreator location"""
from models.base_model import BaseModel
"""import models"""

class Review(BaseModel):
""" managing consumer Reviews"""
    place_id = ""
    user_id = ""
    text = ""
