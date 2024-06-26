#!/usr/bin/python3
"""
class FileStorage serializes instances to a JSON
file and deserializes JSON file to instances
"""
import json
import os.path as path
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity


class FileStorage:
    """class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dictionary = {}
        with open(self.__file_path, mode="w", encoding='UTF-8') as f:
            for key, value in self.__objects.items():
                new_dictionary[key] = value.to_dict()
            json.dump(new_dictionary, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if path.isfile(self.__file_path):
            with open(self.__file_path, mode="r", encoding='UTF-8') as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
