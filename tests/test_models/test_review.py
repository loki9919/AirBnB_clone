#!/usr/bin/python3
"""test Review"""
import unittest
import pep8
from models.base_model import BaseModel
from models.review import Review


class Testreview(unittest.TestCase):

    def test_pep8_review(self):
        """Test that the Review module conforms to PEP8"""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "found code style errors (and warnings)")

    def test_class(self):
        rev = Review()
        self.assertEqual(rev.__class__.__name__, "Review")

    def test_father(self):
        rev = Review()
        self.assertTrue(issubclass(rev.__class__, BaseModel))
