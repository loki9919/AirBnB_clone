#!/usr/bin/python3
"""test State"""
import unittest
import pep8
from models.state import State


class Teststate(unittest.TestCase):
    
    def test_pep8_state(self):
        """test that the State module conforms to PEP8"""
        pep8_style = pep8.StyleGuide(quiet=True)
        result = pep8_style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "found code style errors (and warnings)")

    def test_class(self):
        """test class"""
        state = State()
        self.assertEqual(state.__class__.__name__, "State")
