#!/usr/bin/python3
"""
BaseModel  that defines all common attributes foor other classes.
"""
import uuid
from datetime import datetime

time_format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel():
    """Defines comman attributes for other classes."""
    def __init__(self, *args, **kwargs):
        if  kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setatrr(self, key, value)
            self.created_at = datetime.strptime(kwargs['created_at'],
                    time_format)
            self.updated_at = datetime.strptime(kwargs['updated_at'],
                    time_format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the BaseModel"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                       self.__dict__)
    def save(self):
        """
        Updates the current public instance attribute
        updated_at with the current datetime.
        """
        self.updated_at = datetime.utcnow()


    def to_dict(self):
        """
        returns a dictionary containing all keys/values of ___dict___
        """
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time_format)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time_format)
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
