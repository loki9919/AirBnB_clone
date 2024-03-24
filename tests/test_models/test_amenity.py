#!/usr/bin/python3
"""Test Amenity"""
import unittest
import pep8
from models.base_model import BaseModel
from models.amenity import Amenity


class Testamenity(unittest.TestCase):

    def test_pep8_conformance_amenity(self):
        """test that the Amenity module conforms to PEP8"""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "found code style errors (and warnings)")

    def test_class(self):
        amenity = Amenity()
        self.assertEqual(amenity.__class__.__name__, "Amenity")

    def test_father(self):
        amenity = Amenity()
        self.assertTrue(issubclass(amenity.__class__, BaseModel))
