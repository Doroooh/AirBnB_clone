#!/usr/bin/python3
"""the unittest for place"""


from models.place import Place
import pep8
import os
import unittest


class Test_Place(unittest.TestCase):
    """the unittest for class Place"""

    def test_docstring(self):
        """Checking for docstring"""
        self.assertTrue(len(Place.__doc__) > 1)
        self.assertTrue(len(Place.__init__.__doc__) > 1)
        self.assertTrue(len(Place.__str__.__doc__) > 1)
        self.assertTrue(len(Place.save.__doc__) > 1)
        self.assertTrue(len(Place.to_dict.__doc__) > 1)

    def test_pep8(self):
        """test pep8"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")

    def setUp(self):
        """to test Setup"""

        pass

    def tearDown(self):
        """test the resets"""

        try:
            os.remove("file.json")
        except:
            pass

    def test_init_arg(self):
        """passing arg to a new instance"""
        b1 = Place(23)
        self.assertEqual(type(b1).__name__, "Place")
        self.assertFalse(hasattr(b1, "23"))

    def test_init_kwarg(self):
        """Pass kwargs into the instance"""
        b1 = Place(name="Nairobi")
        self.assertEqual(type(b1).__name__, "Place")
        self.assertTrue(hasattr(b1, "name"))
        self.assertFalse(hasattr(b1, "id"))
        self.assertFalse(hasattr(b1, "created_at"))
        self.assertFalse(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "__class__"))

    def test_str_method(self):
        """printing accurately"""
        b1 = Place()
        b1printed = b1.__str__()
        self.assertEqual(b1printed,
                         "[Place] ({}) {}".format(b1.id, b1.__dict__))

    def test_before_todict(self):
        """instance before using to_dict conversion"""
        b1 = Place()
        b1_dict = b1.__dict__
        self.assertEqual(type(b1).__name__, "Place")
        self.assertTrue(hasattr(b1, '__class__'))
        self.assertEqual(str(b1.__class__),
                         "<class 'models.place.Place'>")
        self.assertTrue(type(b1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['id']), 'str')

    def test_after_todict(self):
        """instance after using to_dict conversion"""
        my_model = Place()
        new_model = Place()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, Place)
        self.assertEqual(type(my_model).__name__, "Place")
        self.assertEqual(test_dict['__class__'], "Place")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
        self.assertNotEqual(my_model.id, new_model.id)

    def test_hasattribute(self):
        """Test if instance of BaseModel is correctly made"""
        b1 = Place()
        self.assertTrue(hasattr(b1, "__init__"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "id"))
