#!/usr/bin/python3

""" This is the BaseModel defining all the common methods for other classes """
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """ The Base class for all models """

    def __init__(self, *args, **kwargs):
        """ This is instantiating a new object
            Args:
                *args: the variable length argument list not used
                **kwargs: the key or value pair of attributes
            """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    if key != "__class__":
                        setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """ Return the string representation of the object """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__)

    def save(self):
        """ updating the public instance attribute
        updated_at with current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returning a dictionary containing all the keys/values of __dict__ of the instance """
        new_dict = dict(self.__dict__)
        new_dict["created_at"] = self.created_at.isoformat(sep='T')
        new_dict["updated_at"] = self.updated_at.isoformat(sep='T')
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
