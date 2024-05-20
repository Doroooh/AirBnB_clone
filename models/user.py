#!/usr/bin/python3
from models.base_model import BaseModel

class UserProfile(BaseModel):
    """Defines a UserProfile object.

    This class represents a user's profile information, including their email,
    password, first name, and last name.

    Attributes:
        email (str): The email address associated with the user's account.
        password (str): The hashed password for the user's account.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """

    email_address = ""
    hashed_password = ""
    given_name = ""
    family_name = "
