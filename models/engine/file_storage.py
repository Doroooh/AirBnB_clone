#!/usr/bin/python3
#!/usr/bin/env python3
""" The Class FileStorage that serialize the instances to a JSON file
    and deserialize the JSON file to an instance """

import json
from os import read
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os.path


class FileStorage:
    """ 
    The class FileStorage to seriliaze and deserialize the instances to JSON
        __file_path: the path of the json file
        __objects: a dictionnary of all objects"
    """
    def __init__(self):
        """ initializing the FileStorage
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """ Will return the dictionary of all the objects """
        return self.__objects

    def new(self, obj):
        """ To set in __objects the object (obj) with the key <obj class name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serialize the  __objects to JSON file (path: __file_path)
            dictionary: empty dictionary
                Open dictionary in write mode
                dump dictionary in the file fl
        """
        dictionary = {}
        with open(self.__file_path, 'w') as fl:
            for obj in self.__objects.values():
                key = obj.__class__.__name__ + "." + obj.id
                dictionary[key] = obj.to_dict()
            json.dump(dictionary, fl)

    def reload(self):
        """deserialize JSON file to __objects
        (only if JSON file (__file_path) exists
        otherwise, do nothing.
        If file, fl is non-existent, no exception should be raised)
            Opening in read mode"
            loading fl and reading it
            """
        try:
            with open(self.__file_path, 'r') as fl:
                my_dict = json.load(fl)
            for key, value in my_dict.items():
                """the for loop will utilise the key value pair to run items in my_dict (my_dict.items())
                creating a dictionary of key and value"""
                new_obj = key.split('.')
                class_name = new_obj[0]
                """new_obj is equal to key.split('.')[0]
                    this will split key, taking first key part"""
                self.new(eval("{}".format(class_name))(**value))
                """the if statement creates a new object with class name of the new_obj and value"""
        except FileNotFoundError:
            pass
