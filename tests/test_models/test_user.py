#!/usr/bin/python3

import unittest
import pep8
from models.user import User


class Testuser(unittest.TestCase):
    """Test User"""
    def test_pep8_user(self):
        """Test that the User module conforms to PEP8"""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "found code style errors (and warnings)")

    def test_User(self):
        """
        Test attributes of Class Use
        """
        my_user = User()
        my_user.first_name = 'lokmane'
        my_user.last_name = 'rouijel'
        my_user.email = 'lokmanerouijel@gmail.com'
        self.assertEqual(my_user.first_name, 'lokmane')
        self.assertEqual(my_user.last_name, 'rouijel')
        self.assertEqual(my_user.email, 'lokmanerouijel@gmail.com')
