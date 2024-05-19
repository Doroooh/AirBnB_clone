#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user_profile import UserProfile
from models.state_entity import StateEntity
from models.city_entity import CityEntity
from models.place_entity import PlaceEntity
from models.amenity_entity import AmenityEntity
from models.review_entity import ReviewEntity


class StorageManager:
    """Represents an abstracted storage engine.

    This class stores and retrieves objects in a JSON file.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def __get_all(self):
        """Return the dictionary __objects."""
        return StorageManager.__objects

    def __set_new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        StorageManager.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save_objects(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = StorageManager.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(StorageManager.__file_path, "w") as f:
            json.dump(objdict, f)

    def load_objects(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(StorageManager.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.__set_new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
