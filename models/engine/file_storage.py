#!/usr/bin/python3

import json
from os.path import path

class FileStorage:
    """class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        objects_dict = {obj: obj.to_dict() for obj in FileStorage.__objects.values()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objects_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                ser_obj = json.load(file)
                for key, value in ser_obj.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = globals()[class_name](**value)
