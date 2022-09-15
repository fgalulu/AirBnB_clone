#!/usr/bin/python3
"""
Serializes instance to JSON file and deserializes JSON file file to instance
"""

import json


class FileStorage:
    """

    """
    _file_path = 'file.json'
    _objects = {}

    def all(self):
        """returns the dictionary objects"""
        return self._objects

    def new(self, obj):
        """
        sets in _objects the obj with key
        """
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            self._objects[key] = obj

    def save(self):
        """
        serialize _objects to JSON file.
        """
        my_dict = {}
        for key in self._objects:
            my_dict[key] = self._objects[key].to_dict()
        with open(self._file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        """
        deserialize the JSON file to _objects
        """
        try:
            with open(self._file_path, 'r') as f:
                json_object = json.load(f)
            for key in json_object:
                self._objects[key] = classes[jo[key]["__class__"
                                                ]](**json_object[key])
        except:
            pass

