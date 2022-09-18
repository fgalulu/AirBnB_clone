#!/usr/bin/python3
"""
Serializes instance to JSON file and deserializes JSON file file to instance
"""

import json
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel, "User": User}


class FileStorage:
    """
    This class serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """
        sets in _objects the obj with key
        """
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            self.__objects[key] = obj

    def save(self):
        """
        serialize _objects to JSON file.
        """
        my_dict = {}
        for key in self.__objects:
            my_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        """
        deserialize the JSON file to _objects
        """
        try:
            with open(self.__file_path, encoding="UTF-8") as f:
                json_object = json.load(f)
            for key, value in json_object.items():
                self.__objects[key] = classes[value["__class__"]](**value)
        except FileNotFoundError:
            pass
