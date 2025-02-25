#!/usr/bin/python3
""" the unittest for amenity """

from models.amenity import Amenity
import pep8
import os
import unittest

class Test_Amenity(unittest.TestCase):
    """the unittest for class Amenity"""

    def test_docstring(self):
        """Checking for docstring"""
        self.assertTrue(len(Amenity.__doc__) > 1)
        self.assertTrue(len(Amenity.__init__.__doc__) > 1)
        self.assertTrue(len(Amenity.__str__.__doc__) > 1)
        self.assertTrue(len(Amenity.save.__doc__) > 1)
        self.assertTrue(len(Amenity.to_dict.__doc__) > 1)

    def test_pep8(self):
        """testing the pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def setUp(self):
        """ to setup the test"""
        pass

    def tearDown(self):
        """Resetting tests"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_init_arg(self):
        """passing in an arg to the new instance"""
        b1 = Amenity(23)
        self.assertEqual(type(b1).__name__, "Amenity")
        self.assertFalse(hasattr(b1, "23"))

    def test_init_kwarg(self):
        """To pass the kwargs into an instance"""
        b1 = Amenity(name="AC")
        self.assertEqual(type(b1).__name__, "Amenity")
        self.assertTrue(hasattr(b1, "name"))
        self.assertFalse(hasattr(b1, "id"))
        self.assertFalse(hasattr(b1, "created_at"))
        self.assertFalse(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "__class__"))

    def test_str_method(self):
        """Testing to see if every method is accurately printing"""
        b1 = Amenity()
        b1printed = b1.__str__()
        self.assertEqual(b1printed,
                         "[Amenity] ({}) {}".format(b1.id, b1.__dict__))

    def test_before_todict(self):
        """Testing the instances before using the to_dict conversion"""
        b1 = Amenity()
        b1_dict = b1.__dict__
        self.assertEqual(type(b1).__name__, "Amenity")
        self.assertTrue(hasattr(b1, '__class__'))
        self.assertEqual(str(b1.__class__),
                         "<class 'models.amenity.Amenity'>")
        self.assertTrue(type(b1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['id']), 'str')

    def test_after_todict(self):
        """Testing the instances after using the to_dict conversion"""
        my_model = Amenity()
        new_model = Amenity()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, Amenity)
        self.assertEqual(type(my_model).__name__, "Amenity")
        self.assertEqual(test_dict['__class__'], "Amenity")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
        self.assertNotEqual(my_model.id, new_model.id)

    def test_hasattribute(self):
        """Testing if the instance of the BaseModel is correctly made"""
        b1 = Amenity()
        self.assertTrue(hasattr(b1, "__init__"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "id"))
