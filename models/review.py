#!/usr/bin/python3
""" Review module for my  project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Reviews the  class, storing the review information from the customers """
    place_id = ""
    user_id = ""
    text = ""
