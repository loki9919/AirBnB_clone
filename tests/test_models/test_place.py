#!/usr/bin/python3
"""Test Place"""
import unittest
import pep8
from models.base_model import BaseModel
from models.place import Place


class Testplace(unittest.TestCase):

    def test_pep8_place(self):
        """test that the Amenity module conforms to PEP8"""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "found code style errors (and warnings)")

    def test_class(self):
        place = Place()
        self.assertEqual(place.__class__.__name__, "Place")

    def test_father(self):
        place = Place()
        self.assertTrue(issubclass(place.__class__, BaseModel))
