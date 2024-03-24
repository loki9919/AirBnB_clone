#!/usr/bin/python3
"""
defines all common attributes or methods for other classes
"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Class BaseModel"""
    def __init__(self, *args, **kwargs):
        """constructor of a BaseModel"""
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    my_form = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(value, my_form))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """string representation method"""
        name = self.__class__.__name__
        id = self.id
        my_dict = str(self.__dict__)
        return f"[{name}] ({id}) {my_dict}"

    def save(self):
        """updates the public instance attribute updated_at with
        the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        keys = self.__dict__.copy()
        keys['__class__'] = self.__class__.__name__
        keys["created_at"] = keys["created_at"].isoformat()
        keys["updated_at"] = keys["updated_at"].isoformat()
        return keys
