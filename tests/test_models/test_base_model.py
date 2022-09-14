#!/usr/bin/python3
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """
    """
    def test_to_dict(self):
        """
        Test conversion of object attributes to dictionanry.
        """
        my_model = BaseModel()
        my_model.name = "Alx"
        my_model.message = "C is fun"
        m_dict = the_model.to_dict()
        self.assertEqual(m_dict["__class__"], "BaseModel")
        self.assertEqual(m_dict["message"], "C is fun")

    def test_save(self):
        """
        test save model
        """
        my_model = BaseModel()
        created_at_1 = my_model.created_at
        updated_at_1 = may_model.updated_at
        my_model.save()
        created_at_2 = my_model.created_at
        updated_at_2 = may_model.updated_at
        self.assertEqual(created_at_1, created_at_2)
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_str(self):
        """
        test string represenattion
        """
        my_model = BaseModel()
        string = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(string, str(my_model))
