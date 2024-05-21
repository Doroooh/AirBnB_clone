#!/usr/bin/python3
"""defining the location interpreter"""
import json
import os.path
from ..base_model import BaseModel
from ..user import User
from ..state import State
from ..place import Place
from ..amenity import Amenity
from ..city import City
from ..review import Review
"""import models"""

class FileStorage:
    """This is serializing instances to a JSON file
    and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}
    """the private class attributes"""

    def all(self):
        """this is the public instance attributes or the method to return dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """The public instance sets in __objects
        the obj with mykey <obj class name>.id"""
        mykey = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[mykey] = obj

    def save(self):
        """the public instance method to serialize
        __objects to JSON file"""
        dict_temp = {}
        for mykey, value in FileStorage.__objects.items():
            dict_temp[mykey] = value.to_dict()
            with open(FileStorage.__file_path, "w") as f:
                f.write(json.dumps(dict_temp))

    def reload(self):
        """it deserializes
        the JSON file to __objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                dict_temp = json.loads(f.read())
                for mykey, value in dict_temp.items():
                    obj = eval(value['__class__'])(**value)
                    FileStorage.__objects[mykey] = obj
