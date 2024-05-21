#!/usr/bin/python3
"""File Storage UnitTests"""

import os
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import models
import pep8


class TestFileStorage(unittest.TestCase):
    """Test cases for class FileStorage"""

    def test_docstring(self):
        """Checking if docstring does exists"""
        self.assertTrue(len(FileStorage.__doc__) > 1)
        self.assertTrue(len(FileStorage.all.__doc__) > 1)
        self.assertTrue(len(FileStorage.new.__doc__) > 1)
        self.assertTrue(len(FileStorage.save.__doc__) > 1)
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)

    def test_pep8(self):
        """Pep8 Test"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def setUp(self):
        """Setting up testing environment to not change previous file storage"""
        self.file_path = models.storage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.rename(self.file_path, 'test_storage')

    def tearDown(self):
        """Removing JSON file after test cases run"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        if os.path.exists('test_storage'):
            os.rename('test_storage', self.file_path)

    def test_instantiation(self):
        """Testing if instantiation is proper"""
        temp_storage = FileStorage()
        self.assertIsInstance(temp_storage, FileStorage)

    def test_saves_new_instance(self):
        """Tests the created file"""
        b1 = BaseModel()
        models.storage.new(b1)
        models.storage.save()
        file_exist = os.path.exists(self.file_path)
        self.assertTrue(file_exist)

    def test_all(self):
        """Tests the  method"""
        temp_storage = FileStorage()
        temp_dict = temp_storage.all()
        self.assertIsNotNone(temp_dict)
        self.assertEqual(type(temp_dict), dict)

    def test_new(self):
        """Testing new method"""
        temp_storage = FileStorage()
        temp_dict = temp_storage.all()
        hawi = User()
        hawi.id = 972
        hawi.name = "hawi"
        temp_storage.new(hawi)
        class_name = hawi.__class__.__name__
        mykey = "{}.{}".format(class_name, str(hawi.id))
        self.assertIsNotNone(temp_dict[mykey])

    def test_reload(self):
        """Testing reload method"""
        temp_storage = FileStorage()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as f:
            for item in f:
                self.assertEqual(item, "{}")
        self.assertIs(temp_storage.reload(), None)


if __name__ == '__main__':
    unittest.main()
