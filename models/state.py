#!/usr/bin/python3
"""Defining State class."""
from models.base_model import BaseModel

class State(BaseModel):
    """Represents the state where project is at

    Attributes:
        name (str): Name of state.
    """

    name = ""
