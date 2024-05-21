#!/usr/bin/python3
""" To test suits for base model"""

import os
import re
import json
import uuid
import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Testing attributes of base model
    """

    def setUp(self):
        """
        the classes that are needed for the testing
        """
        pass

    def test_basic(self):
        """
        Testing basic imputs for BaseModel class
        """
        my_model = BaseModel()
        my_model.name = "HAWI"
        my_model.number = 98
        self.assertEqual([my_model.name, my_model.number],
                         ["HAWI", 98])

    def test_datetime(self):
        """
        Testing the correct datetime format
        """
        pass
    
    def test_datetime(self):
        """
        Testing the correct datetime format
        """
        pass


if __name__ == '__main__':
    unittest.main()
