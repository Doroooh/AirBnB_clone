#!/usr/bin/python3
"""unittest for the users"""

from models.user import User
import pep8
import os
import unittest


class Test_User(unittest.TestCase):
    """Unittest for  class User"""

    def test_docstring(self):
        """Checking for docstring"""
        self.assertTrue(len(User.__doc__) > 1)
        self.assertTrue(len(User.__init__.__doc__) > 1)
        self.assertTrue(len(User.__str__.__doc__) > 1)
        self.assertTrue(len(User.save.__doc__) > 1)
        self.assertTrue(len(User.to_dict.__doc__) > 1)

    def test_pep8(self):
        """test pep8"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "pep8")

    def setUp(self):
        """the test setup"""
        pass

    def tearDown(self):
        """the test reset"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_init_arg(self):
        """test for passing in arg to new instance"""
        b1 = User(23)
        self.assertEqual(type(b1).__name__, "User")
        self.assertFalse(hasattr(b1, "23"))

    def test_init_kwarg(self):
        """test for passing kwargs into the instance"""
        b1 = User(name="Silver")
        self.assertEqual(type(b1).__name__, "User")
        self.assertTrue(hasattr(b1, "name"))
        self.assertFalse(hasattr(b1, "id"))
        self.assertFalse(hasattr(b1, "created_at"))
        self.assertFalse(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "__class__"))

    def test_str_method(self):
        """Testing for accurate printing"""
        b1 = User()
        b1printed = b1.__str__()
        self.assertEqual(b1printed,
                         "[User] ({}) {}".format(b1.id, b1.__dict__))

    def test_before_todict(self):
        """instances before using to_dict conversion"""
        b1 = User()
        b1_dict = b1.__dict__
        self.assertEqual(type(b1).__name__, "User")
        self.assertTrue(hasattr(b1, '__class__'))
        self.assertEqual(str(b1.__class__),
                         "<class 'models.user.User'>")
        self.assertTrue(type(b1_dict['created_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['updated_at']), 'datetime.datetime')
        self.assertTrue(type(b1_dict['id']), 'str')

    def test_after_todict(self):
        """instances after using to_dict conversion"""
        my_model = User()
        new_model = User()
        test_dict = my_model.to_dict()
        self.assertIsInstance(my_model, User)
        self.assertEqual(type(my_model).__name__, "User")
        self.assertEqual(test_dict['__class__'], "User")
        self.assertTrue(type(test_dict['__class__']), 'str')
        self.assertTrue(type(test_dict['created_at']), 'str')
        self.assertTrue(type(test_dict['updated_at']), 'str')
        self.assertTrue(type(test_dict['id']), 'str')
        self.assertNotEqual(my_model.id, new_model.id)

    def test_hasattribute(self):
        """Testing if the instance of the BaseModel is made correctly"""
        b1 = User()
        self.assertTrue(hasattr(b1, "__init__"))
        self.assertTrue(hasattr(b1, "created_at"))
        self.assertTrue(hasattr(b1, "updated_at"))
        self.assertTrue(hasattr(b1, "id"))
