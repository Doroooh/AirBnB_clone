#!/usr/bin/python3
"""the unittest for city"""

from models.city import City
import pep8
import os
import unittest


class Test_City(unittest.TestCase):
    """the unittest for class City"""

    def test_docstring(self):
        """Checking for docstring"""
        self.assertTrue(len(City.__doc__) > 1)
        self.assertTrue(len(City.__init__.__doc__) > 1)
        self.assertTrue(len(City.__str__.__doc__) > 1)
        self.assertTrue(len(City.save.__doc__) > 1)
        self.assertTrue(len(City.to_dict.__doc__) > 1)

    def test_pep8(self):
        """testing the pep8"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def setUp(self):
        """To setup the test"""
        pass

    def tearDown(self):
        """to reset the tests"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_init_arg(self):
        """pass arg to the new instance"""
        b1 = City(23)
        self.assertEqual(type(b1).__name__, "City")
        self.assertFalse(hasattr(b1, "23"))

    def test_init_kwarg(self):
        """Pass kwargs to instance"""
        b1 = City(name="Nairobi")
        self.assertEqual(type(b1).__name__, "City")
        self.assertTrue(hasattr(b1, "name"))
        self.assertFalse(hasattr(b1, "id"))
        self.assertFalse(hasattr(b1, "created_at"))
        self.assertFalse(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "__class__"))

    def test_str_method(self):
        """check if every method prints accurately"""
        b1 = City()
        b1printed = b1.__str__()
        self.assertEqual(b1printed,
                         "[City] ({}) {}".format(b1.id, b1.__dict__))

    def test_before_todict(self):
        """Instances before using the to_dict conversion"""
        b1 = City()
        b1_dict = b1.__dict__
        self.assertEqual(type(b1).__name__, "City")
        self.assertTrue(hasattr(b1, '__class__'))
        self.assertEqual(str(b1.__class__),
                         "<class 'models.city.City'>")
        self.assertTrue(type(b1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['id']), 'str')

    def test_after_todict(self):
        """instances after using the to_dict conversion"""
        my_model = City()
        new_model = City()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, City)
        self.assertEqual(type(my_model).__name__, "City")
        self.assertEqual(test_dict['__class__'], "City")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
        self.assertNotEqual(my_model.id, new_model.id)

    def test_hasattribute(self):
        """Check if instance of BaseModel is correctly made"""
        b1 = City()
        self.assertTrue(hasattr(b1, "__init__"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "id"))
