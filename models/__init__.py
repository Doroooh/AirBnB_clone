#!/usr/bin/python3
"""It defines interpreter location"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity

if __name__ == "__main__":
    storage = FileStorage()
    storage.reload()
