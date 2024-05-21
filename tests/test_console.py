#!/usr/bin/python3
"""The unittest for Console"""

from console import HBNBCommand
import sys
import unittest
from unittest.mock import create_autospec

class Test_Console(unittest.TestCase):
    """The console Unittest"""

    def setUp(self):
        """Setting up the STDIN and STDOUT"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create(self, server=None):
        """Creating the HBNBCommand"""
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_quit(self):
        """Testing the quit command in my project"""
        xit = self.create()
        self.assertTrue(xit.onecmd("quit"))
