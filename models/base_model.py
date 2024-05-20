#!/usr/bin/python3
"""Defines the base class for all the models used in this HBNB- AirBnB clone project."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """The base class for all the HBNB models."""

    def __init__(self, *args, **kwargs):
        """Instantiate the new model."""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    kwargs[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == '__class__':
                    del kwargs[key]
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returning the string representation of the instance."""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """the updates updated_at with current time when instance is changed."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert the instance into dict format."""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = (str(type(self)).split('.')[-1]).split('\'')[0]
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
