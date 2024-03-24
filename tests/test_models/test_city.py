#!/usr/bin/python3
"""test City"""

import unittest
import pep8
from models.base_model import BaseModel
from models.city import City


class Testcity(unittest.TestCase):

    def test_pep8_city(self):
        """test that the City module conform to PEP8"""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "found code style errors (and warnings)")

    def test_class(self):
        """test class"""
        city = City()
        self.assertEqual(city.__class__.__name__, "City")

    def test_father(self):
        """test inheritance"""
        city = City()
        self.assertTrue(issubclass(city.__class__, BaseModel))
