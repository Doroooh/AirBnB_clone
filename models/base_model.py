#!/usr/bin/python3
"""defining interpreter location"""
from datetime import datetime
from uuid import uuid4
import models
"""import modules"""

class BaseModel:
    """defines the attributes for the other classes"""

    def __init__(self, *args, **kwargs):
        """"constructor with the public instance attributes"""
        if kwargs:
            for mykey, value in kwargs.items():
                if mykey in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if mykey not in ['__class__']:
                    setattr(self, mykey, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """defining print"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """updating public instance attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """it returns the dictionary that contains all the mykeys/values of
        __dict__ of the instance"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return(my_dict)
