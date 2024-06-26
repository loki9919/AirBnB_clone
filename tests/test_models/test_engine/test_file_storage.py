#!/usr/bin/python3
"""Test File Storage"""
import unittest
import pep8
import json
from uuid import uuid4
from datetime import datetime
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class TestFileStorage(unittest.TestCase):
    """test the FileStorage"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Betty"
        cls.user.last_name = "Bar"
        cls.user.email = "aibnb@mail.com"
        cls.storage = FileStorage()
        cls.path = "file.json"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user
        """ if delete the file """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_FileStorage(self):
        """tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """test docstring"""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_documentation(self):
        """test documentation, created and not empty"""
        self.assertTrue(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertTrue(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertTrue(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertTrue(FileStorage.reload.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_all(self):
        """tests if all works in File Storage"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """test when new is created"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = "123455"
        user.name = "Betty"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_reload_filestorage(self):
        """tests reload"""
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except Exception:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except Exception:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)

    def test_save(self):
        """testing the save method"""
        bm = BaseModel()
        bm.save()
        self.assertTrue(os.path.exists(self.path))
        bm.name = "Testing"
        bm.number = 1
        bm.save()
        self.assertTrue(os.path.exists(self.path))
        dic = {}
        with open('file.json', 'r') as fjson:
            dic = json.loads(fjson.read())
        bm_key = bm.__class__.__name__ + '.' + bm.id
        self.assertDictEqual(bm.to_dict(), dic[bm_key])


if __name__ == "__main__":
    unittest.main()
