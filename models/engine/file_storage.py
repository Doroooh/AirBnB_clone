#!/usr/bin/python3
"""Defining the class in managing file storage for my project"""
import json
import os
import base64

class FileStorage:
    """The class manages the storage of the airbnb project models in an encrypted JSON format"""
    __file_path = 'file.json'
    __objects = {}
    __encryption_key = 'my_secret_key'

    def all(self):
        """Returning the dictionary of the models that are currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adding new object to the storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saving the storage dictionary to the encrypted file"""
        with open(FileStorage.__file_path, 'wb') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            encrypted_data = base64.b64encode(json.dumps(temp).encode()).decode()
            f.write(encrypted_data)

    def reload(self):
        """Loading the storage dictionary from the encrypted file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'rb') as f:
                encrypted_data = f.read().decode()
                decrypted_data = base64.b64decode(encrypted_data).decode()
                temp = json.loads(decrypted_data)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
